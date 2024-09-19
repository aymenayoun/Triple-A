from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
import mailersend
from mailersend import emails
from decouple import config
import requests
import json
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import account_activation_token
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Create your views here.

api_key=config('api_key')
mailer = emails.NewEmail(api_key)

#mailer = emails.NewEmail(api_key)

class UsernameValidView(View):
    def post(self,request):
        data=json.loads(request.body)  #everything the user has entered as py dic
        username=data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username is to be alphanumeric ＼(°ロ＼)'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'soz already taken (=_=)'},status=409)
        else:
            return JsonResponse({'username_valid':True})
    

class EmailValidView(View):
    def post(self,request):
        data=json.loads(request.body)  #everything the user has entered as py dic
        email=data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'E-mail form is incorrect (ーー;)'},status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'soz already taken (ー_ー)!!'},status=409)
        else:
            return JsonResponse({'email_valid':True})
    
class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')

    def post(self,request):
        
        
        
        #messages.success(request,'Welcome aboard (＾◇＾)')
        #messages.warning(request,'Welcome aboard (＾◇＾)')
        #messages.error(request,'Welcome aboard (＾◇＾)')
        #messages.info(request,'Welcome aboard (＾◇＾)')
        
        #Getting user Info
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        context={
            'fieldValues': request.POST        }
        #check for dublicate
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                #create user
                user=User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.is_active=False
                user.save()
                #email_subject='Account Activation'
                #email_body='activation test'
                #email = EmailMessage(
                        #email_subject,
                        #email_body,
                        #"noreply@esemycolon.com",
                        #[email],
                        #headers={"Message-ID": "foo"},
                    #)
                #email.send(fail_silently=False)
                
                uidb64=urlsafe_base64_encode(force_bytes(user.pk))
                domain =get_current_site(request).domain
                link=reverse('activate',kwargs={'uidb64':uidb64,'token':account_activation_token.make_token(user)})
                activate_url='http://'+domain+link
                
                
                payload = {
                        "from": {
                            "email": "aymenayouni11@trial-7dnvo4dweo3l5r86.mlsender.net",
                            "name": "Triple -A- Expenses"
                        ,},
                        "to": [
                            {    
                             "email": email,
                             "name": username
                            }
                        ],
                         "subject": "Axtivate your Account",
                         "html": """
                            <h1>Welcome to Our Service!</h1>
                            <p>Dear {username},</p>
                            <p>Use this link to verify your account: <a href="{alink}">Verify Now</a></p>
                            <p>Thank you for signing up. We're excited to have you on board!</p>
                            <p>Best regards,<br>Ayouni</p>
                         """.format(username=username,alink=activate_url),  # HTML body content with dynamic insertion of username
                         "text": "Dear {username},\n\nUse this link to verify your account: {alink}\n\nThank you for signing up. We're excited to have you on board!\n\nBest regards,\nAyouni".format(username=username, alink=activate_url)  # Plain text body content
                        #"subject": "Hello from Mailersend!",
                        #"html": "<p>This is the HTML content of the email.</p>",
                        #"text": "This is the plain text content of the email."
                   }

                 # The headers including the API key
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }



                # Sending the POST request
                response = requests.post("https://api.mailersend.com/v1/email", headers=headers, data=json.dumps(payload))

                # Check the response
                if response.status_code == 202:
                    print("Email sent successfully!")
                
                else:
                        print(f"Failed to send email: {response.status_code}")
                        print(response.text)
    


                
                messages.success(request,'Verification Email Sent ＼(^o^)／')
                return redirect('register')  
            else:
                messages.warning(request,'Email already used (・へ・)')
        else:
            messages.warning(request,'Username already used (・ω・)')
                
        
        return render(request, 'authentication/register.html', context)
    
    
class VerificationView(View):
    def get(self,request,uidb64,token):
        try:
            id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=id)
            if not account_activation_token.check_token(user,token):#check if user already active
                return redirect('login'+'message='+'user exists already')
            if user.is_active:
                return redirect('login')
            else:
                user.is_active=True
                user.save()
            messages.success(request,'Welcome aboard (＾◇＾)')
            return redirect('login')
        except Exception as e:
            pass
            
        return redirect('login')
    
    
class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')
    
    def post(self,request):
        username_or_email = request.POST.get('username')
        password=request.POST['password']
        if username_or_email and password:
             if '@' in username_or_email:
                # If user with the provided email exists
                try:
                    user = User.objects.get(email=username_or_email)
                    username = user.username  # Get the username of user with this email
                except User.DoesNotExist:
                    messages.warning(request, 'Invalid credentials ((+_+))')
                    return render(request, 'authentication/login.html')
             else:
                username=username_or_email
             user = auth.authenticate(request, username=username, password=password)
             if user:
                if user.is_active:
                    auth.login(request,user)
                    messages.success(request,'Welcome '+user.username)
                    return redirect('expenses')
                else:
                    messages.warning(request,'Account is not activated yet (?_?) pls check your E-mail')
             else:
                messages.warning(request,'Invalid credentials ((+_+))')
                return render(request,'authentication/login.html')
        else:
            messages.warning(request,'Please fill in all fields (－‸ლ)')
            return render(request,'authentication/login.html')
        
        
class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,'Logged out (^_^)/~')
        return redirect('login')
    
    
    
class RequestPasswordResetEmail(View):
    def get(self, request):
        return render(request, 'authentication/reset-password.html')

    def post(self, request):
        email = request.POST.get('email')
        context = {'values': request.POST}

        if not validate_email(email):
            messages.error(request, 'Invalid Email')
            return render(request, 'authentication/reset-password.html', context)

        user = User.objects.filter(email=email).first()

        if user:  # If the user exists
            username = user.username
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)  # Create reset token
            link = reverse('reset-user-password', kwargs={'uidb64': uidb64, 'token': token})
            reset_url = f'http://{domain}{link}'

            payload = {
                "from": {
                    "email": "aymenayouni11@trial-7dnvo4dweo3l5r86.mlsender.net",
                    "name": "Triple -A- Expenses"
                },
                "to": [
                    {"email": email}
                ],
                "subject": "Password Reset",
                "html": f"""
                    <p>Hello {username},</p>
                    <p>Use this link to reset your password: <a href="{reset_url}">Reset Password</a></p>
                    <p>Best regards,<br>Triple -A- Expenses</p>
                """,
                "text": f"Hello {username},\n\nUse this link to reset your password: {reset_url}\n\nBest regards,\nAyouni"
            }

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            # Send email
            response = requests.post("https://api.mailersend.com/v1/email", headers=headers, data=json.dumps(payload))

            if response.status_code == 202:
                messages.success(request, 'Password reset link sent successfully.')
            else:
                print(f"Failed to send email: {response.status_code}")
                messages.error(request, 'Error sending the email. Please try again later.')
        else:
            # Not revealing whether an email exists
            messages.info(request, 'If an account with that email exists, a reset link has been sent.')

        return render(request, 'authentication/reset-password.html', context)


        
    
    

class CompletePasswordReset(View):
    def get(self, request, uidb64, token):
        context={
            'uidb64': uidb64,
            'token': token
        }
        try:
                user_id=force_str(urlsafe_base64_decode(uidb64))
                user=User.objects.get(pk=user_id)
                if not PasswordResetTokenGenerator().check_token(user,token):
                    messages.success(request,'Password Reset Link Already Used')
                    return render(request, 'authentication/reset-password.html', context)
        except Exception as identifier:
            pass
        return render(request,'authentication/set-new-password.html',context)
    
    def post(self, request, uidb64, token):
        context={
            'uidb64': uidb64,
            'token': token
        }
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            messages.error(request,'please confirm your new password')
            return render(request,'authentication/set-new-password.html',context)
        elif len(password1)<8:
            messages.error(request,'password must be at least 8 characters long')
            return render(request,'authentication/set-new-password.html',context)
        else:
            try:
                user_id=force_str(urlsafe_base64_decode(uidb64))
                user=User.objects.get(pk=user_id)
                user.set_password(password1)
                user.save()
                messages.success(request,'Password changes successfully')
                return redirect('login')
            except Exception as identifier:
                messages.error(request,'Password changes was not successful')
                return render(request,'authentication/set-new-password.html',context)
        
    