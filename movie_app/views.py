from movie_app.models import Movies
from movie_app.serializers import MoviesSerializer
from movie_app.pagination import MyPagination
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class MovieListGV(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    search_fields = ('genre', 'director')
    pagination_class = MyPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    search_fields = ('genre', 'director')
    pagination_class = MyPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

