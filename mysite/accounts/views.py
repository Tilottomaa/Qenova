from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm,LoginForm
from django.utils import timezone
from .models import OrganizationUser
from .forms import OrganizationForm,OrganizationLoginForm




def user_list(request):
    users = User.objects.all()
    return render(request,'user_list.html',{'users':users})

def user_upload(request):

    if request.method == 'POST':

        form = UserForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            user = form.save()

            request.session['user_id'] = user.id

            return redirect('profile')

    else:

        form = UserForm()

    return render(
        request,
        'user_upload.html',
        {'form': form}
    )

def update_user(request, pk):

    user = User.objects.get(pk=pk)

    if request.method == 'POST':

        form = UserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():

            form.save()

            return redirect('user_list')

    else:

        form = UserForm(instance=user)

    return render(request, 'update_user.html', {'form': form})



def delete_user(request, pk):

    user = User.objects.get(pk=pk)

    if request.method == 'POST':

        user.delete()

        return redirect('user_list')

    return render(request, 'delete_user.html', {'user': user})


def login_user(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            password = form.cleaned_data['password']

            user = User.objects.filter(
                email=email,
                password=password
            ).first()

            if user:
                user.last_login = timezone.now()

                user.save()

                request.session['user_id'] = user.id

                return redirect('dashboard')

    else:

        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def logout_user(request):

    request.session.flush()

    return redirect('login')

def profile(request):

    user_id = request.session.get('user_id')

    if not user_id:

        return redirect('login')

    user = User.objects.get(id=user_id)

    return render(request, 'profile.html', {'user': user})

def dashboard(request):

    return render(request, 'dashboard.html')



def organization_register(request):
    if request.method == 'POST':

        form = OrganizationForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('organization_login')

    else:
        form = OrganizationForm()


    return render(request,'organization_register.html',
        {'form': form})



def organization_login(request):

    if request.method == 'POST':

        form = OrganizationLoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            password = form.cleaned_data['password']

            organization = OrganizationUser.objects.filter(
                email=email,
                password=password
            ).first()

            if organization:

                request.session['organization_id'] = organization.id

                return redirect('organization_dashboard')

    else:

        form = OrganizationLoginForm()

    return render(
        request,
        'organization_login.html',
        {'form': form}
    )



def organization_dashboard(request):

    organization_id = request.session.get('organization_id')

    if not organization_id:

        return redirect('organization_login')

    organization = OrganizationUser.objects.get(
        id=organization_id
    )

    return render(
        request,
        'organization_dashboard.html',
        {'organization': organization}
    )

def organization_logout(request):

    request.session.flush()

    return redirect('organization_login')