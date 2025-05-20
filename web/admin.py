from django.contrib import admin

from .models import Daily, Weekly, Monthly, Yearly, LongTerm, Token


@admin.register(Token)
class DailyAdmin(admin.ModelAdmin):
    list_display = ['user']



@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_todo', 'is_done']
    list_filter = ['is_done']
    search_fields = ['title']

@admin.register(Weekly)
class WeeklyAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_todo', 'is_done']
    list_filter = ['is_done']
    search_fields = ['title']

@admin.register(Monthly)
class MonthlyAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_todo', 'is_done']
    list_filter = ['is_done']
    search_fields = ['title']

@admin.register(Yearly)
class YearlyAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_todo', 'is_done']
    list_filter = ['is_done']
    search_fields = ['title']

@admin.register(LongTerm)
class LongTermAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_todo', 'is_done']
    list_filter = ['is_done']
    search_fields = ['title']
