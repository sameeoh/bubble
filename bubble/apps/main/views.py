from django.shortcuts import render, redirect
from django.contrib import messages

import bcrypt
from models import *

## BUBLE MAIN  VIEWS ##
def index(request):
    return render(request, 'main/index.html')

def login(request):
    errors_login = []
    if len(request.POST['email']) <3:
        errors_login.append("LOGIN *Email must be at least 3 characters!")
    if errors_login:
        for err in errors_login:
            messages.error(request, err)

        return redirect('/')

    else:
        user = User.objects.get(email = request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            # get name of user
            name = User.objects.get(id = user.id)
            request.session['name'] = name.name
            return redirect('/dashboard')
        else:
            return redirect('/')

def register(request):

    errors_register = []
    if len(request.POST['name']) < 3:
        errors_register.append("REGISTER *Name should be longer than 3 characters!")
    if len(request.POST['password']) < 8:
        errors_register.append("REGISTER *Password should be at least 8 characters!")
    if request.POST['password'] != request.POST['confirm_password']:
        errors_register.append("REGISTER *Password and password confirmation don't match.")

    if errors_register:
        for err in errors_register:
            messages.error(request, err)

        return redirect('/')
    else:
        try:
            User.objects.get(email=request.POST['email'])
            messages.error(request, "User with that email already exists.")
            return redirect('/')
        except User.DoesNotExist:
            password=request.POST['password']
            ## Hasing the password
            safe_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            name = request.POST['name']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            street = request.POST['street']
            city = request.POST['city']
            state = request.POST['state']
            zip = request.POST['zip']
            # Create Record
            # Level = 0 (Normal User)
            # Level = 1 (Admin)
            address = Address.objects.create(street=street, city=city, state=state, zip=zip)
            User.objects.create(name=name, email=email, phone_number = phone_number,  password=safe_password, address=address, level="1")
            return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect ('/')

def dashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    return render(request, 'main/dashboard.html')

############# ORDER ITEMS ##################
def order(request):
    if not 'user_id' in request.session:
        return redirect('/')

    return render(request, 'main/order.html')
def add_order(request):
    
    return redirect('/dashboard')

###############################
def dev(request):
    return render(request, 'main/dev.html')

def text(request):
    from twilio.rest import Client

    # Your Account SID from twilio.com/console
    account_sid = "AC3d0e91c29c5166cfa4e8b971dc705452"
    # Your Auth Token from twilio.com/console
    auth_token  = "b38bff1881d5c49c515ca5f688b62e3a"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="3235285323",
        from_="+1 213-296-1788 ",
        body="Your Order Is Finished! From Bubble Cleaning =)")

    print(message.sid)
    return redirect('/dev')