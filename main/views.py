from gc import get_stats
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile, Category, Talent, Script,  About, Term, Professional, LikePost, subCategory, filmType, Country, Hiring, Blog
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from itertools import chain
import random

# Create your views here.
def index(request):
    category = Category.objects.all()
    talent = Talent.objects.all()
    script = Script.objects.all()
    
    return render(request, 'index.html', {'categorys':category, 'talents':talent, 'scripts':script[:4]})


def scripts(request):
    script = Script.objects.all()
    return render(request, 'allscripts.html', {'scripts':script})


def professionals(request):
    professional = Professional.objects.all()
    return render(request, 'professionals.html', {'professionals':professional})


def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'abouts':about})


def terms(request):
    term = Term.objects.all()
    return render(request, 'terms.html', {'terms':term})


def signup(request):
    
    if request.method == 'POST':
        if request.POST.get('country'):
            get_country = request.POST.get('country')
            country = get_country

            get_state = request.POST.get('state')
            state = get_state

            username = request.POST['username']
            email = request.POST['email']

            number = request.POST['number']
            bio = request.POST['bio']
            password = request.POST['password']
            password2 = request.POST['password2']

            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email taken')
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
        
                    #log user in and redirect to settings
                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)

                    #create a profile object for the new user
                    user_model = User.objects.get(username=username)
                    new_profile = Profile.objects.create(bio=bio, number=number, country=country, state=state, user=user_model, id_user=user_model.id)
                    new_profile.save()
                    return redirect('/')
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('signup')

    else:
        country = Country.objects.all()
        return render(request, 'signup.html', {'countries':country})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def sell(request):
    if request.method == 'POST':
        
        if request.POST.get('category'):
            get_category = request.POST.get('category')
            category = get_category

            get_filmtype = request.POST.get('filmtype')
            filmtype = get_filmtype

            get_subcategory = request.POST.get('subcategory')
            subcategory = get_subcategory

            get_country = request.POST.get('country')
            country = get_country

            get_state = request.POST.get('state')
            state = get_state

            
            title = request.POST['title']
            seller = request.POST['seller']
            subcategory = request.POST['subcategory']
            filmtype = request.POST['filmtype']
            synopsis = request.POST['synopsis']
            logline = request.POST['logline']
            treatment = request.POST['treatment']
            price = request.POST['price']
            firstpage = request.POST['firstpage']
            pageCount = request.POST['pagecount']

            if Script.objects.filter(title=title).exists():
                messages.info(request, 'Script Title Already taken')
                return redirect('/sell')
            else:
                script = Script.objects.create(state=state, category=category, subcategory=subcategory, filmtype=filmtype, pageCount=pageCount, firstpage=firstpage, price=price, treatment=treatment, logline=logline, synopsis=synopsis,country=country, seller=seller,title=title)
                script.save()
                messages.success(request, f"Your Script {title} is submitted successfully !")
                return redirect('/sell')
    category = Category.objects.all()
    subcategory = subCategory.objects.all()
    filmtype = filmType.objects.all()
    country = Country.objects.all()
    state = Country.objects.all()
    return render(request, 'sellscript.html', {'categorys':category, 'subcategorys':subcategory, 'filmtypes':filmtype, 'countries':country, 'states':state})


@login_required(login_url='signin')
def becomeprofessional(request):

    
    if request.method == 'POST':

        if request.POST.get('country'):
            get_country = request.POST.get('country')
            country = get_country
            name = request.POST['name']
            get_talent = request.POST.get('talent')
            talent = get_talent
            get_category = request.POST.get('category')
            category = get_category
            bio = request.POST['bio']
            rate = request.POST['rate']
            description = request.POST['description']

            image = request.FILES.get('image_upload')


            if Professional.objects.filter(name=name).exists():
                messages.info(request, 'Professional Name Already taken')
                return redirect('/becomeprofessional')
            else:
                professional = Professional.objects.create(image=image, description=description, rate=rate, talent=talent, category=category, bio=bio, name=name, country=country)
                professional.save()
                messages.success(request, f"Your application into {talent} is submitted successfully !")
                return redirect('/becomeprofessional')
    country = Country.objects.all()
    category = Category.objects.all()
    talent = Talent.objects.all()
    return render(request, 'join.html', {'categorys':category, 'countries':country, 'talents':talent})


def scriptdetail(request, pk):
    script_object = Script.objects.get(title=pk)
    return render(request, 'scriptdetail.html', {'script_object':script_object})


def professionaldetail(request, pk):
    professional_object = Professional.objects.get(name=pk)
    return render(request, 'professionaldetails.html', {'professional_object':professional_object})


@login_required(login_url='signin')
def hire_professional(request):

    
    if request.method == 'POST':

        if request.POST.get('country'):
            get_country = request.POST.get('country')
            country = get_country
            hirername = request.POST['name']
            get_talent = request.POST.get('talent')
            talent = get_talent
            get_category = request.POST.get('category')
            category = get_category
            bio = request.POST['bio']
            rate = request.POST['rate']
            description = request.POST['description']

            image = request.FILES.get('image_upload')


            if Professional.objects.filter(hirername=hirername).exists():
                messages.info(request, 'Professional Name Already Hired')
                return redirect('/hire_professional')
            else:
                professional = Hiring.objects.create(image=image, description=description, rate=rate, talent=talent, category=category, bio=bio, hirername=hirername, country=country)
                professional.save()
                messages.success(request, f"Your application to hire {talent} is submitted successfully !")
                return redirect('/hire_professional')
    country = Country.objects.all()
    category = Category.objects.all()
    talent = Talent.objects.all()
    return render(request, 'hire.html', {'categorys':category, 'countries':country, 'talents':talent})



@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    script_id = request.GET.get('script_id')

    script = Script.objects.get(id=script_id)

    like_filter = LikePost.objects.filter(script_id=script_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(script_id=script_id, username=username)
        new_like.save()
        script.no_of_likes = script.no_of_likes+1
        script.save()
        return redirect('/')
    else:
        like_filter.delete()
        script.no_of_likes = script.no_of_likes-1
        script.save()
        return redirect('/')


@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
            
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile':user_profile, 'username_profile_list':username_profile_list})


@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)


    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)



def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blogs':blog})


def blog_details(request, pk):
    blog_object = Blog.objects.get(headline=pk)
    return render(request, 'newsdetails.html', {'blog_objects':blog_object})