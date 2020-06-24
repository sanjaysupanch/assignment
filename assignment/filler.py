import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')

import django
django.setup()

from account.models import Member, Period
from faker import Faker

obj=Faker()

def call(N):
    num=1
    for i in range(N):
        mid=obj.bothify(text='?#??####?', letters='ABCDEWXY')
        real_name=obj.name()
        timezone=obj.timezone()
        
        member_obj=Member.objects.get_or_create(mid=mid, real_name=real_name, tz=timezone)[0]

        for j in range(2):
            member_instance=Member.objects.get(real_name=real_name)
            date_time=obj.date_time()
            date_time1=obj.date_time()
            Period_obj=Period.objects.get_or_create(start=date_time, end=date_time1, member=member_instance)
        
        num+=1

if __name__== '__main__':

    print("Filling Random data\n")
    call(150)
    print("Filling done")
