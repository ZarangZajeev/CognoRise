"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("helloworld/",views.HelloWorldView.as_view()),
    path("morning/",views.GoodMorningView.as_view()),
    path("afternoon/",views.AfternoonView.as_view()),
    path("add/",views.AddView.as_view(),name="addition"),
    path("multiplication/",views.MultiplicationView.as_view(),name="multiplication"),
    path("division/",views.DivisionView.as_view(),name="division"),
    path("subtraction/",views.SubtractionView.as_view(),name="subtraction"),
    path("cube/",views.CubeView.as_view(),name="cube"),
    path("fact/",views.FactorialView.as_view(),name="factorial"),
    path("leapyear/",views.LeapYearView.as_view(),name="leapyear"),
    path("oddeven/",views.OddEvenView.as_view(),name="oddeven"),
    path("prime/",views.PrimeView.as_view(),name="primenumber"),
    path("",views.IndexView.as_view()),
    path("bmi/",views.BmiView.as_view(),name="bmi"),
    path("emi/",views.EmiView.as_view(),name="emi"),
]
