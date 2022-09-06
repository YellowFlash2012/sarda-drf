from rest_framework import serializers

from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    launched = serializers.BooleanField()

    # add new movie
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance relates to the old value of the field
        instance.name = validated_data.get('name', instance.name)

        instance.description = validated_data.get('description', instance.description)

        instance.launched = validated_data.get('launched', instance.launched)

        instance.save()

        return instance