from django.shortcuts import render


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
    return render(request, 'profile/profile-create.html')


def edit_profile(request):
    return render(request, 'profile/profile-edit.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')


def details_profile(request):
    return render(request, 'profile/profile-details.html')
