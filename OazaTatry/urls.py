"""
URL configuration for OazaTatry project.

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
from schedule.views import CalendarView
import calendar
from django.shortcuts import render
urlpatterns = [
   # path("admin/", admin.site.urls),
    path('calendar/', CalendarView.as_view(), name='calendar'),
]

def calendar_view(request):
    # Generowanie listy dat dla miesiąca kwietnia 2023 roku
    cal = calendar.Calendar()
    dates = cal.itermonthdates(2023, 4)

    # Przekazywanie listy dat do szablonu HTML
    context = {
        'dates': dates,
    }
    return render(request, 'templates/calendar.html', context)