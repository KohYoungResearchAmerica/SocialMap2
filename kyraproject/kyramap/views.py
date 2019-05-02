from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
# Create your views here.
from kyramap.models import User

from django.views.generic.base import TemplateView

def index(request):
    user_list = User.objects.order_by('-pub_date')[:5]
    context = {'user_list': user_list}
    return render(request, 'kyramap/index.html', context)

def result(request, user_id):
    response="You're looking at the result of user_id: %s"
    return HttpResponse(response % user_id)

def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'kyramap/detail.html',{'user':user})
    # try:
    #     user = User.objects.get(pk=user_id)
    # except User.DoesNotExist:
    #     raise Http404("User does not exist")
    # return render(request, 'kyramap/detail.html', {'user':user})


class AboutView(TemplateView):
    template_name = 'kyramap/about.html'
