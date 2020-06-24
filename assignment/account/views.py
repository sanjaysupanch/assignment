from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, status, generics
from rest_framework.generics import * 
from .serializers import *
from .models import *

class MemberView(generics.ListCreateAPIView):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer

class MemberUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=MemberSerializer
    queryset=Member.objects.all()
    lookup_field="mid"

class PeriodView(generics.ListCreateAPIView):
    serializer_class=PeriodSerializer
    queryset=Period.objects.all()

class PeriodUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PeriodSerializer
    queryset=Period.objects.all()
    lookup_field="id"

def redirect_view(request):
    response = redirect('/member/')
    return response