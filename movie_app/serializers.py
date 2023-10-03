from movie_app.models import Movies
from rest_framework import serializers


class MoviesSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if len(value) > 255:
            raise serializers.ValidationError('Title should have 255 max or less Character')
        return value

    def validate_genre(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('Genre should under 100 or less Character')
        return value

    def validate_director(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('Director should under 100 or less Character')
        return value

    class Meta:
        model = Movies
        fields = '__all__'
