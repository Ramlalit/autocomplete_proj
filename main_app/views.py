from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import *
from rest_framework.decorators import api_view
from django.views.generic.base import TemplateView
from .serializers import *
import pdb
@api_view(['post'])
def search_by_prefix(request):
    """
    parameters:
      - name: word
        description: type any word 
        required: true
        type: string
        paramType: form
    """
    # pdb.set_trace()
    word = request.data.get('term')
    serializer_data = []
    words = Dictionary_Data.objects.filter(word__startswith = word).order_by('word')
    if not words:
      word = word.upper() 
      words = Dictionary_Data.objects.filter(word__startswith = word).order_by('word')
    if not words:
      word = word.capitalize()
      words = Dictionary_Data.objects.filter(word__startswith = word).order_by('word')
    if words:
      serializer_data = Dictionary_DataSerializer(words, many = True).data
    response = {
      'data' : serializer_data,
      'result': 1
    }
    return Response(response, status=status.HTTP_200_OK)
class HomePageView(TemplateView):

  template_name = "home.html"

  def get_context_data(self, **kwargs):
      context = super(HomePageView, self).get_context_data(**kwargs)
      context['title'] = 'Home Page'
      return context

def autocomplete(request):
  if request.method == 'GET':
    context = {
      'title' : 'Autocomplete Example',
    }
      # context = {'title' : 'Autocomplete Example'}
    return render(request, 'main_app/autocomplete.html', {}) 
  # if request.method == 'POST':
  #   word = request.POST.get('word')
  #   if word:
  #     word = word.upper()
  #   words = Dictionary_Data.objects.filter(word__startswith = word).order_by('word')
  #   print(words)
  #   context = {
  #     'words' : words,
  #     'title' : 'Autocomplete Example',
  #   }
  #   return render(request, 'main_app/autocomplete.html', context)  