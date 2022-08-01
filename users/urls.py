from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import CreateUserView

urlpatterns = [
    path('cadastro', csrf_exempt(CreateUserView.as_view())),
]
