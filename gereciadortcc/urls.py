"""gereciadortcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(),name='index'),
    path('student_registration/', StudentRegistrationView.as_view(),name='student_registration'),
    path('student/', StudentListView.as_view(),name='student'),
    path('student/<int:pk>/detail/', StudentDetailView.as_view(),name='student_detail'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(),name='student_update'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(),name='student_delete'),
    path('teacher_registration/', TeacherRegistrationView.as_view(),name='teacher_registration'),
    path('project_registration/', ProjectRegistrationView.as_view(),name='project_registration'),
    path('examination_board_registration/', ExaminationBoardRegistrationView.as_view(),name='examination_board_registration'),

]