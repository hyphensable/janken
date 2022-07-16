from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
import random
import re
from janken.models import Janken
# Create your views here.

class RankingListView(ListView):
    model = Janken
    paginate_by = 10
    template_name = 'janken/ranking.html'
    queryset = Janken.objects.order_by('-win')
    
def result(request):
    return render(request, "janken/result.html")

def janken(request):
    return render(request, "janken/janken.html")

def janken2(request):
    g=request.POST["g"]
    c=request.POST["c"]
    p=request.POST["p"]
    win=request.POST["win"]
    user=request.POST["userName"]
    enemy=random.randint(0,2)
    #0グー,1チョキ,2パー
    if enemy==0:
        if str(g)=="グー":
            result={
                "enemy":"グー",
                "win":str(win),
                "userName":str(user),
                "result":"あいこ！",
            }
            return render(request, "janken/janken2.html",result)
    
        elif str(c)=="チョキ":
            result={
                "win":str(win),
                "enemy":"グー",
            }
            if str(user)!="None":
                result["userName"]=str(user)
            gw = Janken(win=int(win), user_name=user)
            if user != "None":
                gw.save()
            return render(request,"janken/result.html",result)
    
        elif str(p)=="パー":
            win=int(win)
            win+=1
            result={
                "win":str(win),
                "enemy":"グー",
                "userName":str(user),
                "result":"勝ち！",
            }
            return render(request, "janken/janken2.html",result)
        
        else:
            result={
                "win":str(win),
                "userName":str(user),
            }
            return render(request, "janken/janken2.html",result)
    
    elif enemy==1:
        if str(g)=="グー":
            win=int(win)
            win+=1
            result={
                "win":str(win),
                "enemy":"チョキ",
                "userName":str(user),
                "result":"勝ち！",
            }
            return render(request, "janken/janken2.html",result)
        
        elif str(c)=="チョキ":
            result={
                "enemy":"チョキ",
                "win":str(win),
                "userName":str(user),
                "result":"あいこ！",
            }
            return render(request, "janken/janken2.html",result)

        elif str(p)=="パー":
            result={
                "win":str(win),
                "enemy":"チョキ",
            }
            if str(user)!="None":
                result["userName"]=str(user)
            cw = Janken(win=int(win), user_name=user)
            if user != "None":
                cw.save()
            return render(request,"janken/result.html",result)
        
        else:
            result={
                "win":str(win),
                "userName":str(user),
            }
            return render(request, "janken/janken2.html",result)

    elif enemy==2:
        if str(g)=="グー":
            result={
                "win":str(win),
                "enemy":"パー",
            }
            if str(user)!="None":
                result["userName"]=str(user)
            pw = Janken(win=int(win), user_name=user)
            if user != "None":
                pw.save()
            return render(request,"janken/result.html",result)

        elif str(c)=="チョキ":
            win=int(win)
            win+=1
            result={
                "win":str(win),
                "enemy":"パー",
                "userName":str(user),
                "result":"勝ち！",
            }
            return render(request, "janken/janken2.html",result)

        elif str(p)=="パー":
            result={
                "enemy":"パー",
                "win":str(win),
                "userName":str(user),
                "result":"あいこ！",
            }
            return render(request, "janken/janken2.html",result)
        
        else:
            result={
                "win":str(win),
                "userName":str(user),
            }
            return render(request, "janken/janken2.html",result)

def result2(request):
    name = request.POST["user_name"]
    win = request.POST["win"]

    return render(request,"janken/result.html")
