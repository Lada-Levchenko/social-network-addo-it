from rest_framework import serializers

from .models import User


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    date_of_birth = serializers.DateField()
    avatar = serializers.URLField(allow_blank=True)
    bio = serializers.CharField(max_length=None, min_length=None, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'confirm_password',
                  'date_of_birth', 'avatar', 'bio')

    def create(self, validated_data):
        password = validated_data.get('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        if password and confirm_password and password == confirm_password:
            instance = User.objects.create(**validated_data)
            instance.set_password(password)
            instance.save()

            return instance

    def validate(self, data):
        if data['password']:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data


class UserDetailSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(allow_null=True, required=False)
    avatar = serializers.URLField(allow_blank=True, required=False)
    bio = serializers.CharField(max_length=None, min_length=None, allow_blank=True, required=False)

    class Meta:
        model = User
        exclude = ('password',)
        read_only_fields = ('email',)
