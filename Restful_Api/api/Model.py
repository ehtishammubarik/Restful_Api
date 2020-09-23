from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publish_year = models.CharField(max_length=200)
    file_url = models.CharField(max_length=200)
    file_size = models.CharField(max_length=10)

    def __str__(self):
        return self.title


# class PdfFile(models.Model):
#     name = models.CharField(max_length=200)
#     downloadable = models.BooleanField(default=False, blank=True, null=True)
#
#     def __str__(self):
#         return self.title

