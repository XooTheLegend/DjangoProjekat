from django.shortcuts import render, redirect, get_object_or_404
from .models import Practice
from .forms import PracticeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
# Create your views here.


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Naslov Stranice'})
    else:
        return redirect('demo_app:practices')


@login_required
def practices(req):
    tmp = Practice.objects.all()
    return render(req, 'practices.html', {'practices': tmp})


@login_required
def practice(req, id):
    tmp = get_object_or_404(Practice, id=id)
    return render(req, 'practice.html', {'practice': tmp, 'page_title': tmp.type})


@permission_required('demo_app.change_practice')
def edit(req, id):
    if req.method == 'POST':
        form = PracticeForm(req.POST)

        if form.is_valid():
            p = Practice.objects.get(id=id)
            p.type = form.cleaned_data['type']
            p.location = form.cleaned_data['location']
            p.content = form.cleaned_data['content']
            p.rate = form.cleaned_data['rate']
            p.hours = form.cleaned_data['hours']
            p.minutes = form.cleaned_data['minutes']
            p.save()
            return redirect('demo_app:practices')
        else:
            return render(req, 'edit.html', {'form':form, 'id':id})
    else:
        p = Practice.objects.get(id=id)
        form = PracticeForm(instance=p)
        return render(req,'edit.html',{'form':form, 'id':id})


@permission_required('treninzi.add_practice')
def new(req):
    if req.method == 'POST':
        forma = PracticeForm(req.POST)
        if forma.is_valid():
            p = Practice(type = forma.cleaned_data['type'], location = forma.cleaned_data['location'], content = forma.cleaned_data['content'], rate = forma.cleaned_data['rate'], hours = forma.cleaned_data['hours'], minutes = forma.cleaned_data['minutes'], owner= req.user)
            p.save()
            return redirect('demo_app:practices')
        else:
            return render(req, 'new.html', {'form': forma})
    else:
        forma = PracticeForm()
        return render(req, 'new.html', {'form': forma})