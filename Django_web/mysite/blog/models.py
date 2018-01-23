from django.db import models
from django.contrib.auth.models import User
#
# # Create your models here.
#
# # 新建一个Category 分类数据库表, key为name，数据类型char，值的最大长度150
# class Category(models.Model):
#     name = models.CharField(max_length=150)
#
# # 标签数据库
# class Tag(models.Model):
#     name = models.CharField(max_length=150)
#
#
# class Post(models.Model):
#     # 文章标题较短 char字符
#     title = models.CharField(max_length=150)
#     # 内容较多，用text
#     body = models.TextField()
#     created_time = models.DateTimeField()
#     modified_time = models.DateTimeField()
#     # 摘要可以为空
#     excerpt = models.CharField(max_length=150, blank=True)
#
#     # 数据库表间的联系，ForeignKey一对多，ManyToManyField多对多
#     category = models.ForeignKey('Category',on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag, blank=True)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)

class user(models.Model):
    username = models.CharField(max_length=20)
    headImg = models.ImageField(upload_to='mysite/upload/')