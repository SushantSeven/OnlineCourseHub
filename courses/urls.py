"""
URL configuration for onlinecourse project.

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
from django.urls import path, include
from courses.views import HomePageView, coursePage , SignupView , LoginView , signout , checkout, verifyPayment, MyCoursesList, newpage, searchedPage, filteratoz,filterztoa,lowtohigh,hightolow, forgotpasswordPage, changepasswordPage, run_python_script
from django.conf.urls.static import static
from onlinecourse.settings import MEDIA_URL, MEDIA_ROOT
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('logout', signout, name="logout"),
    path('my-courses', MyCoursesList.as_view(), name="my-courses"),
    path('signup',SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('course/<str:slug>', coursePage, name="coursepage"),
    path('check-out/<str:slug>', checkout, name="checkoutpage"),
    path('verify_payment', verifyPayment, name="verify_payment"),
    path("new",newpage,name='newpage'),
    path("searched",searchedPage,name='searched'),
    path("filteratoz",filteratoz,name='filteratoz'),
    path("filterztoa",filterztoa,name='filteraztoa'),
    path("lowtohigh",lowtohigh,name='lowtohigh'),
    path("hightolow",hightolow,name='hightolow'),
    path("forgot_password",forgotpasswordPage,name='forgot_password'),
    path("change_password/<str:token>/",changepasswordPage,name='change_password'),
    path('run_script/', run_python_script, name='run_python_script'),

    # path("reset_password/",auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
]
# ]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
# setiing for staic files

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 