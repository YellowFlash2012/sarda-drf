

from django.forms import ValidationError
from rest_framework import serializers

from watchlist_app.models import Movie, Review, StreamingPlatform

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    # "reviews" here refers to related_name in models
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"
        # fields=["id", "name", "description"]
        # exclude = ["name"]

    # validation - field-level validation
    # _name if the name of the field to be validated
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value

    # validation - object-level validation
    def validate(self, data):
        if data['name'] == data["description"]:
            raise ValidationError("name and description should be different")
        return data

# validators
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
    
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     launched = serializers.BooleanField()

    # add new movie
    # def create(self,validated_data):
    #     return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
        # instance relates to the old value of the field
        # instance.name = validated_data.get('name', instance.name)

        # instance.description = validated_data.get('description', instance.description)

        # instance.launched = validated_data.get('launched', instance.launched)

        # instance.save()

        # return instance

    # validation - field-level validation
    # _name if the name of the field to be validated
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

    # validation - object-level validation
    # def validate(self, data):
    #     if data['name'] == data["description"]:
    #         raise ValidationError("name and description should be different")

class StreamingPlatformSerializer(serializers.ModelSerializer):

    # "movie" refers to related_name in models
    movie = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = "__all__"