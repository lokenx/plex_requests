import datetime
import logging

from django.utils import timezone
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import generics, permissions, serializers
from config.models import Config

logger = logging.getLogger(__name__)


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        conf = Config.objects.get()

        today = timezone.now()
        week_ago = today - datetime.timedelta(days=7)
        requested_since = Movie.objects.filter(requested_by=self.request.user).filter(created__gte=week_ago).count()

        # If you're an admin user or approvals aren't required set to true, also checks limits
        if self.request.user.is_staff or conf.requests_approval == False:
            logger.info('The user {} requested {} ({}) and was'.format(self.request.user, self.request.data['title'], self.request.data['year']))
            serializer.save(requested_by=self.request.user, approved=True, pending=False)
        elif conf.limit_movie == 0 or requested_since < conf.limit_movie:
            logger.info('The user {} requested {} ({})'.format(self.request.user, self.request.data['title'], self.request.data['year']))
            serializer.save(requested_by=self.request.user, approved=False, pending=True)
        else:
            logger.info('{} requested a movie beyond their weekly limit.'.format(self.request.user))
            content = {'error': "You've exceeded your weekly limit for movie requests"}
            raise serializers.ValidationError(content)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAdminUser,)
