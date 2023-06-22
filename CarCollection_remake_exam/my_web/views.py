from django.shortcuts import render, redirect

from CarCollection_remake_exam.my_web.forms import ProfileCreateForm, ProfileEditForm
from CarCollection_remake_exam.my_web.models import Profile, Car


def get_profile():
    return Profile.objects.first()


def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    return render(request, 'common/catalogue.html')


def create_car(request):
    return render(request, 'car/car-create.html')


def details_car(request, pk):
    return render(request, 'car/car-details.html')


def edit_car(request, pk):
    return render(request, 'car/car-edit.html')


def delete_car(request, pk):
    return render(request, 'car/car-delete.html')


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }

    return render(request, 'profile/profile-create.html', context, )


def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price = 0
    if cars.count():
        total_price = sum([c.price for c in cars])

    context = {'profile': profile, 'total_price': total_price, }

    return render(request, 'profile/profile-details.html', context, )


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {'form': form, }

    return render(request, 'profile/profile-edit.html', context, )


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')
