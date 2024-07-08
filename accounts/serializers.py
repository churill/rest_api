from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.ModelSerializer):
    input_password = serializers.CharField(max_length=20, write_only=True)
    confirm_password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('user_id', 'username', 'input_password', 'confirm_password', 'site_id')
        # read_only_fields = ('user_id', 'username',)
        extra_kwargs = {
            'input_password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }

    def validate(self, attrs):
        password = attrs.get('input_password')
        confirm_password = attrs.get('confirm_password')

        if not self.instance:
            if password:
                if not confirm_password or password != confirm_password:
                    raise serializers.ValidationError(
                        '確認用パスワードが異なります。'
                    )
        else:
            if not password or not confirm_password:
                raise serializers.ValidationError(
                    'パスワードが設定されていません。'
                )
            elif password != confirm_password:
                raise serializers.ValidationError(
                    '確認用パスワードが異なります。'
                )

        super(CustomUserSerializer, self).validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('input_password', None)
        _ = validated_data.pop('confirm_password', None)
        user = get_user_model().objects.create_user(
            password=make_password(password),
            **validated_data
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('input_password', None)
        _ = validated_data.pop('confirm_password', None)
        hash_password = make_password(password) if password else instance['password']
        user = get_user_model().objects.update(
            password=hash_password,
            **validated_data,
            defaults=instance
        )
        user.save()
        return user
