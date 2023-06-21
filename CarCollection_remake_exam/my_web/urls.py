from django.urls import path, include

from CarCollection_remake_exam.my_web.views import index, catalogue, create_car, details_car, edit_car, delete_car, \
    create_profile, edit_profile, delete_profile, details_profile

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),

    path('car/', include([
        path('create/', create_car, name='create-car'),
        path('<int:pk>/details/', details_car, name='details-car'),
        path('<int:pk>/edit/', edit_car, name='edit-car'),
        path('<int:pk>/delete/', delete_car, name='delete-car'),
    ])),

    path('profile/', include([
        path('create/', create_profile, name='create-profile'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile'),
        path('details/', details_profile, name='details-profile'),
    ]))
)

"""

http://localhost:8000/ - index page
http://localhost:8000/catalogue/ - catalogue page

http://localhost:8000/car/create/ - car create page
http://localhost:8000/car/1/details/ - car details page
http://localhost:8000/car/1/edit/ - car edit page
http://localhost:8000/car/1/delete/ - car delete page

http://localhost:8000/profile/create - profile create page
http://localhost:8000/profile/details/ - profile details page
http://localhost:8000/profile/edit/ - profile edit page
http://localhost:8000/profile/delete/ - profile delete page

"""
