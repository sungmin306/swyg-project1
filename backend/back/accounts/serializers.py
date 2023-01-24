# from .models import User
# from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email = validated_data['email'],
#             nickname = validated_data['nickname'],
#             password = validated_data['password']
#         )
#         return user
#     class Meta:
#         model = User
#         fields = ['nickname', 'email', 'password']

# from rest_framework import serializers
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import User
# #from .serializer import SignupSirializer, SigninSirializer

# from rest_framework import generics, status
# from rest_framework.response import Response

# # class SignupView(generics.CreateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = SignupSirializer
# class SignupSirializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required = True,
#     ),
#     password = serializers.CharField(
#         required=True,
#         write_only = True,
#     )
#     password2 = serializers.CharField(write_only = True, required=True)
    
#     class Meta:
#         model = User
#         fields = ('email','password','password2','username')
    
#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError({
#                 "password" : "Pass word fields didn't match"
#             })
        
#         return data

#     def create(self, validated_data):
#         user = User.objects.create(
#             username = validated_data['username'],
#             email = validated_data['email']
#         )
#         token = RefreshToken.for_user(user)
#         user.set_password(validated_data['password'])
#         user.refreshtoken = token
#         user.save()

#         return user