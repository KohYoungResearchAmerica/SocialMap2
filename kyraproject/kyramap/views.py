from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from kyramap.models import User

def index(request):
    latest_list = User.objects.order_by('-pub_date')[:5]
    context = {'latest_list': latest_list}
    return render(request, 'kyramap/index.html', context)

def result(request, user_id):
    response="You're looking at the result of user_id: %s"
    return HttpResponse(response % user_id)
