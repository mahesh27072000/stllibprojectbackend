from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
import base64
from django.core.files.base import ContentFile

# class NewUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(_('email address'), unique=True)
    
#     first_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)

#     start_date = models.DateTimeField(default=timezone.now)

# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     def __str__(self):
#         return self.name

class Book(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    print("Working...............................")
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    number_of_copies = models.PositiveSmallIntegerField()
    # cover_picture=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.title}"


class Issue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library_member = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    due_date = models.DateField()

    class Meta:
        unique_together = ['book', 'library_member']

    def __str__(self):
        return f"{self.library_member} | {self.book}"


class Return(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library_member = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_return = models.DateField()
    def __str__(self):
        return f"{self.library_member} | {self.book}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Issue.objects.filter(book=self.book, library_member=self.library_member).delete()


class Renewal(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library_member = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_renewal = models.DateField()
    due_date = models.DateField()
    def __str__(self):
        return f"{self.library_member} |{self.book}"


