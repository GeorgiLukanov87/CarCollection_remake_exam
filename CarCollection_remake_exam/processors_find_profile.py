from CarCollection_remake_exam.my_web.models import Profile


def get_profile(request):
    profile = Profile.objects.first()
    return {'profile': profile}
