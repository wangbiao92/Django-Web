from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from .models import user
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(required=False)
    headImg = forms.ImageField(required=False)
@csrf_exempt
def index(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            print(request.FILES)
            #获取表单信息request.FILES是个字典
            User = user(headImg=request.FILES['file'])
            #保存在服务器
            User.save()
            return HttpResponse('upload ok!')
    return render(request, 'blog/index.html')

# Create your views here.
# def index(request):
#     return render(request, 'blog/index.html')