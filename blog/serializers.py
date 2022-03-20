from pyexpat import model
from rest_framework import serializers
from .models import Blog,Comment,likes

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model=likes
        fields="__all__"
     

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields=["blog","createdDate"]


class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    comment_count=serializers.SerializerMethodField(read_only=True)
    likes=LikesSerializer(many=True,write_only=True)
    likes_count=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Blog
        fields=["title","content","id","likes","createdDate","upDatedDate","user","comment_count","comments","image","likes_count"]
    
    def get_comment_count(self,obj):
        return obj.comments.count() 
    def get_likes_count(self,obj):
         return obj.likes.count() 
    
