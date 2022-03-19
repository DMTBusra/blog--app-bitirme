from .models import Blog
from .serializers import  BlogSerializer
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
class BlogList(mixins.ListModelMixin,mixins.CreateModelMixin ,GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@api_view(["GET", "PUT", "DELETE"])
def blog_detail(request, pk):

    if request.method == "GET":

        queryset = Blog.objects.get(id=pk)
        serializer = BlogSerializer(queryset)

        return Response(serializer.data)

    elif request.method == "PUT":

        queryset = Blog.objects.get(id=pk)
        serializer = BlogSerializer(instance=queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        queryset = Blog.objects.get(id=pk)
        queryset.delete()
        return Response("Item deleted", status=status.HTTP_204_NO_CONTENT)