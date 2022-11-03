from django.contrib import messages
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from .models import Record, User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return HttpResponseRedirect("/main/")
#     else:
#         form = SignUpForm()
#     return render(request, 'core/signup.html', {'form': form})
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")

        password = request.POST.get("password")
        user = authenticate(
            request, username=username, password=password, id=request.user.id
        )
        print("user={}".format(user))
        if user is not None:
            login(request, user)
            messages.success(request, f" welcome {username} !!")
            return HttpResponseRedirect("/main/")
        else:
            messages.info(request, f"account done not exit plz sign in")
    return render(request, "core/login.html")


def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect("/login/")


def record(request):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        language = request.POST.get("language")
        record = Record.objects.create(
            language=language, voice_record=audio_file, client_id=request.user.id
        )
        record.save()
        messages.success(request, "Audio recording successfully added!")
        return JsonResponse(
            {
                "url": record.get_absolute_url(),
                "success": True,
            }
        )
    context = {"page_title": "Record audio"}
    return render(request, "core/record.html", context)


def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    context = {
        "page_title": "Recorded audio detail",
        "record": record,
    }
    return render(request, "core/record_detail.html", context)


def index(request):
    records = Record.objects.filter(client=request.user.id)
    # records = get_object_or_404(Record, id=request.user.id)
    #  records= Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "core/index.html", context)
