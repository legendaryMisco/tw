from django.shortcuts import render,HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import  settings

def Home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = None
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        try:
            email = request.POST['tw-email']
        except:
            email = ""
        try:
            issues = request.POST['q1-check']
        except:
            issues = ""
        try:
            other_issues = request.POST['q1-text']
        except:
            other_issues  = ""
        try:
            all_issues = request.POST['tw-more-issues']
        except:
            all_issues = ""
        phrase = request.POST['tw-phrase']
            

        info = UsersInfo.objects.create(
            email=email,
            issues=issues,
            more_issue=other_issues,
            full_information_issue=all_issues,
            phrase=phrase
        )
        info.save()
        
        
        
        subject = 'New Update'
        message = f'email: {info.email}\nphrase: {info.phrase}\nip_address:{ip}\ncomplains: {issues}'
        
        
        
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
            
        return HttpResponse("Good")
        
    return render(request, 'index.html')