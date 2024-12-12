from django.db import models
from django.contrib.auth.models import User


class PPT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User 모델과의 FK 관계
    title = models.CharField(max_length=255)  # 제목
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜
    is_public = models.BooleanField(default=True)  # 공개 여부
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    file_path = models.FileField(upload_to='ppt_output/')  # PPT 파일 경로
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True, blank=True)  # 썸네일 이미지 경로

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저와의 관계
    ppt = models.ForeignKey(PPT, on_delete=models.CASCADE)  # PPT와의 관계
    added_at = models.DateTimeField(auto_now_add=True)  # 추가된 시간

    def __str__(self):
        return f"{self.user.username} - {self.ppt.title}"

    class Meta:
        unique_together = ('user', 'ppt')  # 유저는 하나의 PPT만 장바구니에 담을 수 있도록