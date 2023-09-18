from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.core import serializers

def post_list_and_create(request):
    qs = Post.objects.all()

    context = {'qs': qs}
    return render(request,'posts/main.html', context)

def load_post_data_view(request):
    qs = Post.objects.all()
    data = serializers.serialize('json', qs)
    return JsonResponse({'data': data})


def hello_world_view(request):
    return JsonResponse({'text': 'hello wrld'})