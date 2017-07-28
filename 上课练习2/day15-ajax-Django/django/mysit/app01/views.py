from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.

def dbhandle(request):
    #request        用户请求的所有内容
    #request.POST   用户已POST方式提交
    #request.GET    用户已GET方式提交


    #增
    '''
    # 1.models.userinfo.objects.create(username='alex',password='123',age='1212')
    # 2. dic ={"username":'eric',"password":'123',"age":123123}
        models.userinfo.objects.create(**dic)
    '''
    #删
    #models.userinfo.objects.filter(username='eric').delete()

    #改
    #models.userinfo.objects.all().update(age=123)

    #查
    #models.userinfo.objects.all()                   #获取所有
    #models.userinfo.objects.filter(age=19)          #根据条件 查找
    #models.userinfo.objects.filter(age=19).first()  #查找age=19的第一个结果


    #user_list_obj = models.userinfo.objects.all()
    #queryset,list

    # for line in user_list_obj:
    #     print(line.username,line.password,line.age)


    #return HttpResponse('ok')
    if request.method == "POST":
        print(request.POST)

        models.userinfo.objects.create(username=request.POST['username'],
                                        password=request.POST['password'],
                                        age=request.POST['age']
                                        )
    user_list_obj = models.userinfo.objects.all()
    return render(request,'t1.html', {'li':user_list_obj})



def home(request):
    #return("asdasd")
    return HttpResponse('App01.home')

def news(request,nid1,nid2):
    nid = nid1 + nid2
    return HttpResponse(nid)

def page(request,n1,n2):
    nid = n1 + n2
    return HttpResponse(nid)