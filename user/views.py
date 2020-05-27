from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from home.models import UserProfile
from gezi.models import Category, Gezi, Comment
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import GeziForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile}
    return render(request, 'userprofile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile': profile,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz başarıyla değişti')
            return redirect('change_password')
        else:
            messages.error(request, 'Hatalı işlem', '<br>' + str(form.errors))
            return HttpResponseRedirect('/user/changepassword')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        return render(request, 'change_password.html', {
            'form': form,
            'category': category,
            'profile': profile,
        })


@login_required(login_url='/login')
def yorum_listele(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    comments = Comment.objects.filter(user_id = current_user.id)
    context = {
        'category': category,
        'comments': comments,
        'profile': profile
    }
    return render(request, "yorum_listele.html", context)

@login_required(login_url='/login')
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Yorum başarıyla silindi...')

    return HttpResponseRedirect('/user/comments/')


@login_required(login_url='/login')
def user_gezi(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    gezis = Gezi.objects.filter(user_id = current_user.id)
    form = GeziForm()
    context = {
        'category':category,
        'gezis': gezis,
        'profile': profile,
        'form': form
    }
    return render(request, 'user_gezis.html',context)

@login_required(login_url='/login')
def add_gezi(request):
    if request.method == 'POST':
        form = GeziForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Gezi()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.category = form.cleaned_data['category']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.city = form.cleaned_data['city']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, "Başarıyla eklendi")
            return HttpResponseRedirect('/usergezis')
        else:
            messages.success(request, " Hata")
            return HttpResponseRedirect('/')
    else:
        category = Category.objects.all()
        form = GeziForm()
        context = {
            'category': category,
            'form': form
        }
        return render(request,'user_addgezi.html',context)


