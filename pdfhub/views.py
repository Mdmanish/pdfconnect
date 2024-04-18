from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegistrationForm, FileUploadForm
from .models import UploadedFile, UserProfile
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from .utils import fetch_answer_from_pdf

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = RegistrationForm(request.POST)

        validated_files = []
        # Retrieve uploaded files
        for key, uploaded_file in request.FILES.items():
            # Validate file extension
            validator = FileExtensionValidator(allowed_extensions=['pdf'])
            try:
                validator(uploaded_file)
            except ValidationError:
                messages.error(request, 'File must be in PDF format.')
                return redirect('/register')

            # Validate file size
            if uploaded_file.size > 10 * 1024 * 1024:  # 10MB
                messages.error(request, 'File size must be less than 10MB.')
                return redirect('/register')
                
            validated_files.append(uploaded_file)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # Save each validated file
            file_instances = [UploadedFile(user_profile=profile, file=validated_file) for validated_file in validated_files]
            UploadedFile.objects.bulk_create(file_instances)
            
            messages.success(request, 'Files uploaded successfully.')
            return redirect('/login/')
        else:
            messages.error(request, 'Form data is not valid.')
    else:
        user_form = UserCreationForm()
        profile_form = RegistrationForm()
        file_form = FileUploadForm()
        file_labels = [
            "10th Grade Marksheet",
            "12th Grade Marksheet",
            "Migration Certificate",
            "Transcript",
            "Letter of Recommendation",
            "Statement of Purpose",
            "Resume"
        ]

    return render(request, 'pdfhub/register.html', {'user_form': user_form, 'profile_form': profile_form, 'file_form': file_form, 'file_labels': file_labels})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'pdfhub/login.html', {'form': form})


def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    user_profile = UserProfile.objects.get(user=request.user)
    user_files = UploadedFile.objects.filter(user_profile__user=request.user)
    return render(request, 'pdfhub/home.html', {'user_profile': user_profile, 'user_files': user_files})

def fetch_answer(request):
    if request.method == 'POST':
        pdf_file = request.POST.get('file')
        question = request.POST.get('question')
        if not question:
            question = request.POST.get('custom_question')
        if pdf_file:
            print(pdf_file)
            # Call the function to fetch the answer based on the selected question
            answer = fetch_answer_from_pdf(pdf_file, question)
            if answer:
                return HttpResponse({answer})
            else:
                return HttpResponse('Failed to fetch answer from PDF')
        else:
            return HttpResponse('No PDF file found')
    else:
        return HttpResponse('Invalid request method')
    
