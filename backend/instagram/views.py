from asyncio.log import logger
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def dispatch(self, request, *args, **kwargs):
        print("request.body: ", request.body)
        print("request.POST: ", request.POST)
        return super().dispatch(request, *args, **kwargs)
# def post_list(request):
#     pass

# def post_detail(request, pk):
#     pass