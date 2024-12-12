from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


# 회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],  # 이메일에 대한 중복 검증
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],  # 비밀번호에 대한 검증
    )
    password2 = serializers.CharField(  # 비밀번호 확인을 위한 필드
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

    # 회원가입 시리얼라이저


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],  # 이메일에 대한 중복 검증
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],  # 비밀번호에 대한 검증
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user


from django.contrib.auth import authenticate


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)  # 해당 유저의 토큰을 불러옴
            return token
        raise serializers.ValidationError(  # 가입된 유저가 없을 경우
            {"error": "Unable to log in with provided credentials."}
        )
