from django.forms import ValidationError
from rest_framework import serializers

from users.models import CustomUser, User

class SignupSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields=['username','email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        password = self.validated_data['password']
        # password2 = self.validated_data['password2']
        email = self.validated_data['email']
        username = self.validated_data['username']

        # if password != password2:
        #     raise ValidationError({'error':'both passwords need to match'})

        if CustomUser.objects.filter(email).exists():
            raise serializers.ValidationError({'error':'User with such email already exists'})

        account = CustomUser(username,email)
        account.set_password(password)
        account.save()

        return account