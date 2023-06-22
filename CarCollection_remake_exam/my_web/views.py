from django.shortcuts import render, redirect

from CarCollection_remake_exam.my_web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, CarCreateForm, \
    CarEditForm, CarDeleteForm
from CarCollection_remake_exam.my_web.models import Profile, Car


def get_profile():
    return Profile.objects.first()


def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    cars = Car.objects.all()

    context = {'cars': cars, }

    return render(request, 'common/catalogue.html', context, )


def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form, }

    return render(request, 'car/car-create.html', context, )


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {'car': car, }
    return render(request, 'car/car-details.html', context, )


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'car': car, 'form': form, }

    return render(request, 'car/car-edit.html', context, )


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form, 'car': car, }

    return render(request, 'car/car-delete.html', context, )


# Profile Views
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
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }

    return render(request, 'profile/profile-delete.html', context, )
