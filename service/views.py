import jsonify
import openai
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.html import escape

from finalProject import settings
from service.forms import RegisterForm, LoginForm
from service.models import ChatHistory

openai.api_key = settings.OPENAI_API_KEY


def home(request):
    try:
        if request.method == 'POST':
            user_input = request.POST.get('user_input')

            formatted_user = escape(user_input)
            bot_response = response(formatted_user)

            formatted_resp = bot_response.replace("\n", "<br>")

            ChatHistory.objects.create(
                user=request.user,
                message=formatted_user,
                sender='user'
            )
            ChatHistory.objects.create(
                user=request.user,
                message=formatted_resp,
                sender='bot'
            )

        chat_history = ChatHistory.objects.filter(user=request.user)

        return render(request, 'homepage.html', {'chat_history': chat_history})

    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'homepage.html', {'chat_history': []})


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
            else:
                login(request, user)
                return redirect('homepage')  # Redirect to a home page after login

    return render(request, 'login.html', {'form': form})


def gpt_response(query):
    # Constructing a prompt using SQL data and user's query
    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}  # User's query
        ]

        # Sending the request to the v1/chat/completions endpoint
        resp = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Correct model name
            messages=messages,  # List of messages to pass to the model
            max_tokens=2000,
            temperature=0.3
        )
        return resp['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error with GPT: {str(e)}"


def clear_chat(request):
    if request == 'POST':
        ChatHistory.objects.filter(user=request.user).delete()  # Remove chat history from the session
        return redirect('homepage')
    return redirect('homepage')


def response(user_input):
    try:
        question_response = gpt_response(user_input)  # Passes the question as parameter for the response method.

        formatted_response = question_response.replace("\n",
                                                       "<br>")  # Replacing the new-line character with the HTML new-line character
        return formatted_response
    except Exception as e:
        return f"Error generating response: {str(e)}"


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return redirect('register')
            else:
                user = form.save(commit=False)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                return redirect('login')  # Redirect to login page

        else:
            # If the form is invalid, display the form with errors
            messages.error(request,
                           'Password must be over 8 characters, with uppercase and special characters (e.g., !@#$%^&*).'
                           'Try a different username if issues persist.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset_password.html'  # Create this template
    email_template_name = 'password_reset_instructions.txt'  # Create this template
    subject_template_name = 'password_reset_subject.txt'  # Create this template
    success_url = '/password_reset/done/'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'change_password.html'  # Ensure this template exists
    success_url = reverse_lazy('login')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'  # Ensure this template exists

    def get(self, request, *args, **kwargs):
        # Redirect to login page after displaying the template
        return super().get(request, *args, **kwargs)
