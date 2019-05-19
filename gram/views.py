from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .forms import ImageForm,SignupForm,CommentForm,EditForm
from django.contrib.auth.decorators import login_required.

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Instagram account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    date = dt.date.today()
    
    return render(request, 'registration/homepage.html', {"date": date,})

@login_required(login_url='/home')
def index(request):
    date = dt.date.today()
    photos = Image.objects.all()
    # print(photos)
    profiles = Profile.objects.all()
    # print(profiles)
    form = CommentForm()

    return render(request, 'all-posts/index.html', {"date": date, "photos":photos, "profiles":profiles, "form":form})

def new_image(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
        return redirect('index')

    else:
        form = ImageForm()
    return render(request, 'new_image.html', {"form": form})