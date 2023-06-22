from django import forms

from CarCollection_remake_exam.my_web.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }

        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(ProfileBaseForm):
    pass
