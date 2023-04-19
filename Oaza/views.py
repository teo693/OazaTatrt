from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.dates import MonthMixin
import calendar

class CalendarView(MonthMixin, ListView):
    template_name = 'calendar.html'
    model = calendar # zmień na swoją nazwę modelu

    def get_queryset(self):
        return self.model.objects.filter(date__month=self.get_month()).order_by('date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cal = calendar.Calendar()
        dates = cal.itermonthdates(self.get_year(), self.get_month())
        context['dates'] = dates
        return context