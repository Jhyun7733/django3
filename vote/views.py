from django.shortcuts import render, redirect
from .models import Topic, Sel
from django.utils import timezone
# Create your views here.


def index(request):
    t = Topic.objects.all()
    context = {
        "tset": t
    }

    return render(request,'vote/index.html', context)

def detail(request,tpk):
    t = Topic.objects.get(id=tpk)
    s= t.sel_set.all()
    context = {
        "t" : t,
        "sset" : s
    }
    return render(request, 'vote/detail.html', context)

def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():

        t.voter.add(request.user)
        spk = request.POST.get("sel")
        s = Sel.objects.get(id=spk)
        s.choicer.add(request.user)
    return redirect("vote:detail", tpk)

def cancel(request,tpk):
    t = Topic.objects.get(id=tpk)
    t.voter.remove(request.user)
    u = request.user
    u.sel_set.get(topic=t).choicer.remove(u)
    return redirect("vote:detail",tpk)

def create(request):
    if request.method=="POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        sn = request.POST.getlist("sname")
        sp = request.FILES.getlist("spic")
        sc = request.POST.getlist("scon")
        t = Topic(subject = s, content=c, maker=request.user, pubdate=timezone.now())
        t.save()
        for name,pic,con in zip(sn,sp,sc):
            Sel(topic=t, sname=name, scon=con, spic=pic).save()
        return redirect("vote:index")

    return render(request, "vote/create.html")
    

def delete(request,tpk):
    t = Topic.objects.get(id=tpk)
    if t.maker == request.user:
        s = t.sel_set.all()
        for i in s:
            i.spic.delete()
        t.delete()
    else:
        pass #마지막날
    return redirect("vote:index")    


