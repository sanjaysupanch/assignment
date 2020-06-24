from rest_framework import serializers
from .models import *
from rest_framework.serializers import HyperlinkedModelSerializer


class PeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Period
        fields=('start', 'end')


class MemberSerializer(serializers.ModelSerializer):
    activity_periods=serializers.SerializerMethodField()
    
    class Meta:
        model = Member
        fields =('mid', 'real_name', 'tz', 'activity_periods')

    def get_activity_periods(self, obj):
       data = PeriodsSerializer(obj.activity_periods.all(), many=True).data
       return data


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Period
        fields=[ 'start', 'end', 'id', 'member']



