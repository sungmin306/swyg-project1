from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import Post
from .serializers import PostSerializer 
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination   # 페이지 분할해서 request
from collections import OrderedDict # 페이지 분할해서  request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
#from rest_framework.authentication import JWTAuthentication
# Create your views here.


# #목록보여주기
# @api_view(['GET'])
# def get_api(request):
#     posts = Post.objects.all()
#     serailized_posts= PostSerializer(posts, many=True)
#     return Response(serailized_posts.data)

# #주문하기(Create)
# @api_view(['POST'])
# def post_api(request):
#     if request.method == 'GET':
#         return HttpResponse(status=200)
#     if request.method == 'POST':
#         serializer = PostSerializer(data = request.data, many=True)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data ,status=200)
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

class PostPageNumberPagination(PageNumberPagination):
    page_size = 6
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('postList', data),
            ('pageCnt', self.page.paginator.num_pages), # 총 페이지수
            ('curPage', self.page.number), # 현재 페이지 
        ]))
#@csrf_exempt
class PostViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication] # 권한
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # 권한
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPageNumberPagination
    #serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

