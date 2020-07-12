from django.shortcuts import render, redirect
from .forms import UserOurRegistraion, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserOurRegistraion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth')
    else:
        form = UserOurRegistraion()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Ругистрация пользователя'})

@login_required
def profile(request):
    if request.method == "POST":
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid():
            update_user.save()

            return redirect('profile')

    else:
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'update_user': update_user,
    }
    return render(request, 'users/profile.html', data)