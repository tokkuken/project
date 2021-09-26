from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.http import Http404
from .models import database

st = 0
ans = 1
def index(request):
    if request.method == "GET":
        try:
            loginuser = request.session['username']
            target = database.objects.get(username = loginuser)
            ans = target.answer
            sco = target.score
            param = {"username":loginuser,'st':st,"answer":ans,"score":sco}
            return render(request,'vote.html',param)
        except:
            message = {"message":""}
            return render(request,'index.html',message)
    else:
        print("post")
        loginuser = request.POST.get("username")
        password = request.POST.get("password")
        if database.objects.filter(username=loginuser).exists():
            target = database.objects.get(username = loginuser)
            if password == target.password:
                target = database.objects.get(username = loginuser)
                ans = target.answer
                sco = target.score
                param = {"username":loginuser,'st':st,"answer":ans,"score":sco}
                request.session['username'] = loginuser
                return render(request,'vote.html',param)
            else:
                message = {"message":"ユーザ名かパスワードが違います"}
                return render(request,'index.html',message)
        else:
                message = {"message":"ユーザ名かパスワードが違います"}
                return render(request,'index.html',message)

def signup(request):
    if request.method == "GET":
        return render(request,'signup.html')
    else:
        loginuser = request.POST.get("username")
        password = request.POST.get("password")
        cla_ss = request.POST.get("class")
        request.session['username'] = loginuser
        me = database.objects.create(username = loginuser, password = password , answer = "0", score = "0", course = cla_ss)
        param = {"username":loginuser,'st':st,"socre":0,"answer":0}
        return render(request,'vote.html',param)


def post(request):
    global st
    if st == 0:
        answer = request.POST.get('answer')
        loginuser = request.session['username']
        target = database.objects.get(username = loginuser)
        target.answer = answer   
        target.save()
        target = database.objects.get(username = loginuser)
        ans = target.answer
        sco = target.score
        param = {"username":loginuser,'st':st,"answer":ans,"score":sco}
        return render(request,'vote.html',param)
    else:
        loginuser = request.session['username']
        target = database.objects.get(username = loginuser)
        ans = target.answer
        sco = target.score
        param = {"username":loginuser,'st':st,"answer":ans,"score":sco}
        return render(request,'vote.html',param)

def answer(request):
    global ans
    users = database.objects.all()
    try:
        loginuser = request.session['username']
        if loginuser == "admin":
            return render(request,'answers.html',{'users':users,'answer':ans})
        else:
            return HttpResponse("管理者権限がありません")
    except:
        message = {"message":"回答を見るには管理者アカウントでログイン"}
        return render(request,'index.html',message)

def scorelist(request):
    users = database.objects.all()
    try:
        loginuser = request.session['username']
        if loginuser == "admin":
            return render(request,'scorelist.html',{'users':users})
        else:
            return HttpResponse("管理者権限がありません")
    except:
        message = {"message":"回答を見るには管理者アカウントでログイン"}
        return render(request,'index.html',message)

def score(request):
    global ans
    users = database.objects.all()
    try:
        loginuser = request.session['username']
        if loginuser == "admin":
            for user in users:
                print(user.course)
                target = database.objects.get(username = user.username)
                answer = target.answer
                print(answer,ans)
                if int(answer) == int(ans):
                    target.score = int(target.score) +  int(target.sourse)
                else:
                    target.score = int(target.score)  - (int(target.course) -1)*2
                target.save()
            return render(request,'scorelist.html',{'users':users})            
        else:
            return HttpResponse("管理者権限がありません")
    except:
        message = {"message":"管理者アカウントでログイン"}
        return render(request,'index.html',message)


def start(request):
    global st
    st = 0
    loginuser = request.session['username']
    param = {"answer":ans,'st':st}
    return render(request,'master.html',param)

def stop(request):
    global st
    global ans
    st = 1
    loginuser = request.session['username']
    param = {"answer":ans,'st':st}
    return render(request,'master.html',param)

def logout(request):
    request.session.clear()
    message = {"message":"ログアウトしました"}
    return render(request,'index.html',message)

def master(request):
    global ans
    param = {"answer":ans,'st':st}
    if request.method == "GET":
        try:
            loginuser = request.session['username']
            if loginuser == "admin":
                print(loginuser)
                return render(request,'master.html',param)
            else:
                return HttpResponse("管理者権限がありません")
        except:
            message = {"message":"回答を見るには管理者アカウントでログイン"}
            return render(request,'index.html',message)
    else:
        ans = request.POST.get('answer')
        param['answer'] = ans
        return render(request,'master.html',param)

# Create your views here.