from django.contrib.auth.models import User #User model
from django.contrib.auth.password_validation import validate_password # django의 기본 패스워드 검증 도구

from rest_framework import serializers 
from rest_framework.authtoken.models import Token #Token model
from rest_framework.validators import UniqueValidator # email 중복 방지 검증 도구
from django.contrib.auth import authenticate # Django의 기본 authenticate 함수, DefaultAuthBackend인 TokenAuth 방식 유저 인증
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset = User.objects.all())], # email 중복 검증
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],  #비밀번호에 대한 검증
    )

    password2 = serializers.CharField(write_only=True, required=True) # 비밀번호 확인을 위한 필드

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self,data): # 비밀번호 일치 확인 여부 함수
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password" : "Password fields didn't match."})
        
        return data
    
    def create(self, validated_data): # CREATE method 요청에 대해 create 메소드를 오버라이딩, 유저를 생성하고 토큰 생성
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],                 
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only = True)
    #wirte_only 옵션을 통해 client -> server 방향의 역직렬화는 가능 , server -> client 방향의 직렬화는 불가능

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials"}
        )
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nickname","image")

