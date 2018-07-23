# from django.shortcuts import render
# from django.core import serializers

from django.template import loader
from .models import Map

from django.http import HttpResponse

# def index(request):
# #     return render(request, 'life/index.html')
#     return render(request, 'life/retrieve.html')

#Display latest 3 Map locations separated by CommonPasswordValidator
def index(request):
    latest_location_list = Map.objects.order_by('-pub_date')[:10]
    template = loader.get_template('life/index.html')
    context = {
        'latest_location_list': latest_location_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))
  