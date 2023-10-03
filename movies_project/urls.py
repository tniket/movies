from django.contrib import admin
from django.urls import path, include
from movie_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', views.MovieListGV.as_view(), name='movie_list'),
    path('api/movies/<int:pk>/', views.MovieView.as_view(), name='movie_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
