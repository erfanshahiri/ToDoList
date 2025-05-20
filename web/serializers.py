'''''
from rest_framework import serializers

from .models import Daily, Weekly, Monthly, Yearly, LongTerm



class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily
        fields = ('id', 'title', 'time_todo')


class WeeklySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekly
        fields = ('title', 'time_todo')


class MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monthly
        fields = ('title', 'time_todo')

class YearlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Yearly
        fields = ('title', 'time_todo')

class LongTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongTerm
        fields = ('title', 'time_todo')
'''''
