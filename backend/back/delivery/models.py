from django.db import models
from django.contrib.auth.models import User
#from django.conf import settings
# user = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE, default = '')
# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null = False, max_length=100) #제목
    people_num = models.IntegerField() # 모집인원
    waiting_time = models.IntegerField(blank = True, null = True) # 소요시간
    place = models.CharField(max_length=100) #분배장소
    food_category = models.IntegerField()
    kakaourl= models.CharField(null= True, blank = True, max_length=50)
    # 커피/디저트 = 0 , 패스트푸드 = 1 도시락 = 2 아시안 = 3 분식 = 4 한식 = 5 중식 = 6 일식 = 7 양식 = 8
    content =  models.CharField(max_length = 500 ) # 본문 내용
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, default = '')
    
    def __str__(self):
        return self.title
    