from django.db import models

class ImageCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class ViewImages(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='image description.')
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    image_cat = models.ForeignKey(ImageCategory,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UploadModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploadedimg')
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name