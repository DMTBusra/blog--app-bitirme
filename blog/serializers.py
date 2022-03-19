from pyexpat import model
from rest_framework import serializers
from .models import Blog,Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields=["blog","createdDate"]


class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    comment_count=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Blog
        fields=["title","content","createdDate","upDatedDate","user","comment_count","comments","image"]
    
    def get_comment_count(self,obj):
        return obj.comments.count() 
    # def get_likes_count(self,obj):
    #     return obj.likes.count() 