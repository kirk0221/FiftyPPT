from django.contrib.auth.models import User
from .forms import RegisterForm
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, SigninSerializer

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework.authtoken.models import Token
from .forms import LoginForm


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class SigninView(generics.GenericAPIView):
    serializer_class = SigninSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)


# ---------------------------------------------------------------------------ㅍ


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 후 자동 로그인
            messages.success(request, '회원가입이 완료되었습니다!')
            return redirect('https://fiftyppt.pythonanywhere.com/')
    else:
        form = RegisterForm()
    return render(request, 'Mentor/register.html', {'form': form})


class Signin(generics.GenericAPIView):
    def get(self, request):
        form = LoginForm()
        return render(request, 'Mentor/signin.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                messages.success(request, f'로그인 성공! 토큰: {token.key}')
                return redirect('https://fiftyppt.pythonanywhere.com/')
            else:
                return render(request, 'https://fiftyppt.pythonanywhere.com/',
                              {'form': form, 'error': '로그인 정보가 올바르지 않습니다.'})
        else:
            return render(request, 'https://fiftyppt.pythonanywhere.com/', {'form': form})


from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)  # Django의 logout 함수로 로그아웃 처리
    return redirect('https://fiftyppt.pythonanywhere.com/')
