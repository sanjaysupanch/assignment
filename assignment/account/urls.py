from django.urls import include, path
from .import views
from .views import *

urlpatterns=[
    path('member/', MemberView.as_view(), name="member"),
    path('member/<mid>/', MemberUpdateView.as_view(), name='member-update'),
    path('period/', PeriodView.as_view(), name='period'),
    path('period/<id>/', PeriodUpdateView.as_view(), name='period-update'),

]

