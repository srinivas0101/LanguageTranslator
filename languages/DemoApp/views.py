from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import Reg,Savefile
from language import settings
import random
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request,'html/index.html')

def home(request):
    return render(request,"html/index.html")

def login(request):
    if request.method=="POST":
        n=request.POST.get('email')
        d=request.POST.get('pas1')
        try:
            users = Reg.objects.get(pk=n)
            user_emails = users.ad
            user_passwords = users.passc
            user_name=users.name
            if(n==user_emails and d==user_passwords):
                request.session['userma']=user_emails
                request.session['nme']=user_name
                return redirect("das")
            else:
                error_message = "Email or Password is incorrect."
                return render(request, "html/login.html", {'error_message': error_message})
        except:
            error_message = "User Details not found."
            return render(request, "html/login.html", {'error_message': error_message})
    return render(request,"html/login.html")

def signu(request):
    if request.method == 'POST':
        # Retrieving form data
        username = request.POST.get('ID')
        email = request.POST.get('mai')
        password = request.POST.get('pass')
        country = request.POST.get('country')
        t=settings.EMAIL_HOST_USER
        sbj='OTP for SignUp'
        otp = ''.join(random.choices('0123456789', k=6))
        m=f"Dear {username},\n\nThank you for signing up for our translation services! To ensure the security of your account, we require verification through a one-time password (OTP). Your OTP code is:\n\n {otp}\n\nPlease enter this code on the verification page to complete your registration process. If you did not request this OTP, please ignore this email.\n\n Best regards,\n\n Language Translation Team"
        b=send_mail(sbj,m,t,[email])
        request.session['otps1']=otp
        request.session['passw1']=password
        return redirect('/otp/?email={}&username={}&country={}'.format(email,username,country))
    return render(request,"html/signup.html")

def otp(request):
    otp_from_signup = request.session.get('otps1')
    email_from_signup = request.GET.get('email')
    name_from_signup = request.GET.get('username')
    pass_from_signup = request.session.get('passw1')
    country_from_signup = request.GET.get('country')
    try:
        if request.method == 'POST':
            # Retrieve form data from current OTP page
            entered_otp = request.POST.get('entotp')
            if entered_otp == otp_from_signup:
                x=Reg.objects.create(name=name_from_signup,passc=pass_from_signup,cont=country_from_signup,ad=email_from_signup)
                t=settings.EMAIL_HOST_USER
                sbj='Welcome to [Translator Website]! 🌍 Lets Get Started!'
                m=f"Dear {name_from_signup},\n\nCongratulations on successfully completing your registration with our Online Translator! We are thrilled to welcome you to our community!\n\nYou can now have access our translation services that is designed to enhance your experience.\n\n Best regards,\n\n Language Translation Team"
                b=send_mail(sbj,m,t,[email_from_signup])
                return redirect("log")
            else:
                error_message = "enter OTP Correctly."
                return render(request, "html/otps.html", {'error_message': error_message})
    except IntegrityError as e:
       return redirect("act")
    return render(request,"html/otps.html")

def dash(request):
    username = request.session.get('nme')
    usemail = request.session.get('userma')
    langs=Savefile.objects.filter(user=usemail)
    if username:
        return render(request, 'html/dashbo.html', {'username': username,'usermail':usemail,'langs':langs})
    return render(request,"html/dashbo.html")

def tet(request):
    usemail=request.session.get('userma')
    count = Savefile.objects.filter(user=usemail).count()
    count=count+1
    if request.method == 'POST':
        output_text = request.POST.get('output_text')
        inpus = request.POST.get('input_text')
        inp = request.POST.get('input_text1')
        oup = request.POST.get('output_text1')
        x=Savefile.objects.create(user=usemail,ids=count,paragraphs="Text - Text",srclang=output_text,destlang=inpus,srctext=inp,desttext=oup)
    return render(request,"html/trans.html")

def prof(request):
    username = request.session.get('nme')
    usemail = request.session.get('userma')
    users1 = Reg.objects.get(pk=usemail)
    countr=users1.cont
    if username:
        return render(request, 'html/profile.html', {'username': username,'usermail':usemail,'countr':countr})
    
    return render(request,"html/profile.html")

def sets(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        usemail = request.session.get('userma')
        users = Reg.objects.get(pk=usemail)
        user_emails = users.ad
        user_passwords = users.passc
        if(user_passwords==old_password):
            if (new_password == confirm_password):
                users.passc=new_password
                users.save()
                errorm="Password changed Successfully"
                return render(request,"html/setting.html",{'errorm':"Password changed Successfully"})
            else:
                errorm="New Password and confirm Password did not match"
                return render(request,"html/setting.html",{'errorm':errorm})
        else:
            errorm="Old password not Equal"
            return render(request,"html/setting.html",{'errorm':errorm})
    return render(request,"html/setting.html")

def vmoice(request):
    if request.method == 'POST':
        outs=request.POST.get('resulttext')
    return render(request,"html/voice.html")

def logot(request):
    logout(request)
    return render(request,"html/logout.html")

def histo(request):
    usemail = request.session.get('userma')
    username = request.session.get('nme')
    user_events = Savefile.objects.filter(user=usemail)
    user_events_count = user_events.count()  # Count the number of events
    context = {
        'user_events': user_events,
        'user_events_count': user_events_count,
        'user_mail':usemail,
        'user_name':username,
    }
    return render(request,"html/hist.html",context)

def mapc(request):
    output_text = request.GET.get('outputText', '')  # Retrieve the output text from the URL query parameter
    usemail=request.session.get('userma')
    count = Savefile.objects.filter(user=usemail).count()
    count=count+1
    if request.method == 'POST':
        output_texts = request.POST.get('output_text')
        inpus = request.POST.get('input_text')
        inp = request.POST.get('input_text1')
        oup = request.POST.get('output_text1')
        x=Savefile.objects.create(user=usemail,ids=count,paragraphs="Image - Text",srclang=output_texts,destlang=inpus,srctext=inp,desttext=oup)
        return redirect("oss")
    return render(request, 'html/voicetran.html', {'output_text': output_text})
    

def ocrs(request):
    return render(request,"html/ocr.html")

def vtran(request):
    usemail=request.session.get('userma')
    result_value=request.session.get('output')
    count = Savefile.objects.filter(user=usemail).count()
    count=count+1
    if request.method == 'POST':
        output_te = request.POST.get('output_text')
        inpus1 = request.POST.get('input_text')
        inp1 = request.POST.get('input_text1')
        oup1 = request.POST.get('output_text1')
        x=Savefile.objects.create(user=usemail,ids=count,paragraphs="Speech - Text",srclang=output_te,destlang=inpus1,srctext=inp1,desttext=oup1)
        return redirect("vps")
    return render(request,"html/vtrans.html",{'result_value': result_value})

def voicet(request):
    if request.method == 'POST':
        result_text = request.POST.get('result')
        if result_text:
            request.session['output']=result_text
            return redirect('vts')
    return render(request,"html/vocetl.html")

def acct(request):
    return render(request,"html/accexist.html")

def otss(request):
        if request.method == 'POST':
            email = request.POST.get('email')
            
            # Check if email exists in the database
            if Reg.objects.filter(ad=email).exists():
                # Generate OTP
                otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
                send_mail(
                    'Forgot Password OTP',
                    f'Your OTP for resetting password is: {otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                
                # Set flag to indicate OTP sent
                request.session['otp_sent'] = True
                request.session['email'] = email
                request.session['otp'] = otp
                return redirect('vot')
            else:
                return render(request, 'html/otplogin.html', {'email_not_found': True})
        
        return render(request, 'html/otplogin.html')

def verify_otp(request):
    if request.method == 'POST':
        otps = request.POST.get('otps')
        if otps == request.session.get('otp'):
            return redirect("pas")
        else:
            return render(request, 'html/verify.html', {'otp_sent': True, 'error_message': 'Invalid OTP. Please try again.'})

    return render(request, 'html/verify.html')

def passw(request):
    usemail=request.session.get('email')
    if request.method=='POST':
        newpass=request.POST.get('newPassword')
        users = Reg.objects.get(pk=usemail)
        name=users.name
        users.passc=newpass
        users.save()
        t=settings.EMAIL_HOST_USER
        sbj='Password change Reqest'
        m=f"Dear {name},\n\nWe are writing to inform you that your password has been successfully changed.\n\nIf you did not initiate this change, please contact our support team immediately.\n\nThank you.\n\n Best regards,\n\n Language Translation Team"
        b=send_mail(sbj,m,t,[usemail])
        logout(request)
        return redirect("hm")
    return render(request,"html/password.html")

