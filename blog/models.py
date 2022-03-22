from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=200)
    createdDate = models.DateTimeField(auto_now_add=True)
    upDatedDate=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to=None,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
   
    
    def __str__(self):
        return  f'{self.title} '
class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    comment=models.CharField(max_length=150)
    createdDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return  f'{self.blog} '
class likes(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="likes")
    likes= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
         return  f'{self.blog} '