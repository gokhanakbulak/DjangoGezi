from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponseBadRequest
# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.utils.safestring import mark_safe

from gezi.models import Category, Gezi, Images, Comment
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormMessage, ContactFormu, UserProfile


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    songezi = Gezi.objects.filter(status='True').order_by('-id')[:4]
    context = {'setting': setting,
               'page': 'home',
               'songezi': songezi,
               'category': category}
    if not request.user.is_authenticated:
        return render(request, 'index.html', context)
    else:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'setting': setting,
                   'page': 'home',
                   'profile': profile,
                   'songezi': songezi,
                   'category': category}
        return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'setting': setting,
               'page': 'aboutus',
               'profile': profile,
               'category': category}
    return render(request, 'aboutus.html', context)


def user_profile(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'aboutus',
               'category': category}
    return render(request, 'userprofile.html', context)


def reference(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()

    context = {'setting': setting,
               'page': 'reference',
               'category': category}
    return render(request, 'references.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarıyla iletilmiştir")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'contact',
               'form': form,
               'category': category}
    return render(request, 'contacts.html', context)


def category_gezi(request, id, slug):
    category = Category.objects.all()

    categorydata = Category.objects.get(pk=id)
    gezi = Gezi.objects.filter(category_id=id)
    context = {'gezi': gezi,
               'category': category,
               'categorydata': categorydata}
    return render(request, 'geziler.html', context)

    image_tag.short_description = 'Image'


def gezi_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            gezi = Gezi.objects.filter(title__icontains=query)

            context = {'gezi': gezi,
                       'category': category}
            return render(request, 'gezi_search.html', context)
    return HttpResponseRedirect('/')


def gezi_detay(request, id, slug):
    category = Category.objects.all()
    obj = Category.objects.filter(children__isnull=True)
    images = Images.objects.filter(gezi_id=id)
    message = Comment.objects.filter(gezi_id=id, status='True')

    songezi = Gezi.objects.all().order_by('-id')[:4]
    gezidata = Gezi.objects.get(pk=id)

    context = {'gezidata': gezidata,
               'images': images,
               'message': message,
               'category': category,
               'obj': obj,
               'songezi': songezi}
    return render(request, 'gezidetay.html', context)





def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
    # Redirect to a success page.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseBadRequest("Hatalı kullanıcı adı veya şifre")


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    obj = Category.objects.filter(children__isnull=True)
    songezi = Gezi.objects.all().order_by('-id')[:4]
    context = {'category': category,
               'form': form,
               'obj': obj,
               'songezi': songezi}

    return render(request, 'signup.html', context)
