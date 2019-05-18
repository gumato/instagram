from django.db import models

# Create your models here.
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    bio = models.CharField(max_length=250)
    profile_photo = models.ImageField(upload_to='profile/')
    # pub_date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name


    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=40)
    image_caption = models.CharField(max_length=40)
    image_location = models.CharField(max_length=40)
    # profile = models.ForeignKey(profile,on_delete=models.CASCADE,blank=True)
    posted_time = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    # class Meta:
    #     ordering = ['_posted_time']


    def save_image(self):
        self.save()



class Comments(models.Model):
    comment = models.CharField(max_length = 400)
    # posted_on = models.DateTimeField(auto_now=True)
    # image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


