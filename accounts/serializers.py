from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('user_id', 'username', )
        read_only_fields = ('user_id', 'username', )

