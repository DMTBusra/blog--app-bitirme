from .models import Blog
from .serializers import  BlogSerializer
from rest_framework.generics import GenericAPIView, mixins
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class BlogList(mixins.ListModelMixin,mixins.CreateModelMixin ,GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class Edit(APIView):
    
    def get_obj(self, pk):
        return get_object_or_404(Blog, pk=pk)

    def get(self, request, pk):
        permission_classes=[IsAuthenticatedOrReadOnly]
        blog = self.get_obj(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = self.get_obj(pk)
        serializer = BlogSerializer(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_obj(pk)
        todo.delete()
        data = {
            "message": "Blog succesfully deleted."
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

