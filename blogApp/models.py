from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.deletion import CASCADE

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email field is mandatory')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser True')
        
        return self.create_user(email, password, **extra_fields)
        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email Address', unique=True)
    name = models.CharField(max_length=30, unique=True)
    user_image = models.ImageField(upload_to='userphotos/', default='avatar.png')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__ (self):
        return self.email
    
    class Meta:
        ordering = ["email"]
        verbose_name_plural = "Users"
        db_table = "Users" 

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='postimages/')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    CATEGORY = {
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Fullstack', 'Fullstack'),
    }
    category = models.CharField(max_length=20, choices=CATEGORY)
    STATUS = {
        ('Draft', 'Draft'),
        ('Published', 'Published')
    }
    status = models.CharField(max_length=20, choices=STATUS)
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    User.username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
        
    def __str__ (self):
        return self.title
    
    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Posts"
        db_table = "Posts"
        
class Likes(models.Model):
    likes_owners = models.ForeignKey(User, on_delete=CASCADE)
    likes_posts = models.ForeignKey(Post, on_delete=CASCADE)
    
    def __str__ (self):
        return self.likes_posts
        # return self.like_set.all().count()
    
    def total_likes(self):
        return self.like_set.all().count()
    
    class Meta:
        ordering = ["likes_posts"]
        verbose_name_plural = "Likes"
        db_table = "Likes"
    
class Comments(models.Model):
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True) 
    comments_owners = models.ForeignKey(User, on_delete=CASCADE)
    comments_posts = models.ForeignKey(Post, on_delete=CASCADE)
    
    def __str__ (self):
        return self.comments_posts
    
    class Meta:
        ordering = ["comments_posts"]
        verbose_name_plural = "Comments"
        db_table = "Comments"
    
class PostViews(models.Model):
    views_owners = models.ForeignKey(User, on_delete=CASCADE)
    views_posts = models.ForeignKey(Post, on_delete=CASCADE)
    
    def __str__ (self):
        return self.views_posts
    
    class Meta:
        ordering = ["views_posts"] 
        verbose_name_plural = "Postviews"
        db_table = "Postviews"
    

        
        
        
     
    