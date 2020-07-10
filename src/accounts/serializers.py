from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """Basic User Serializer """

    password_2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'date_joined',
            'password', 'password_2'
        )
        extra_kwargs = {
            'password_2': {'write_only': True}
        }

    def save(self):
        """User save to database if password==password_2"""

        user = get_user_model()(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password_2 = self.validated_data['password_2']

        if password != password_2:
            raise serializers.ValidationError(
                {'password': "Password must match"}
            )
        else:
            user.set_password(password)
            user.save()
            return user
