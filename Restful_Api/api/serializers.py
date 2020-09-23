from rest_framework import serializers
from .Model import Book
# from .Model import PdfFile


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields ='__all__'


# class PdfFileSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = PdfFile
# 		fields ='__all__'