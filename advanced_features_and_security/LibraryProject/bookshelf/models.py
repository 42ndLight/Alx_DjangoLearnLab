from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password, date_of_birth, profile_photo):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, password=password, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)  
        user.date_of_birth = date_of_birth
        user.profile_photo = profile_photo      
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, date_of_birth, )

        
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['password', 'date_of_birth']



    def __str__(self):
        return self.email  

    