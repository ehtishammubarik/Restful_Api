from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .Model import Book
from .initialzePdf import *
from .serializers import BookSerializer


@api_view(['GET'])  # display all the books in database
def bookList(request):
    book = Book.objects.all().order_by('-id')
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)


@api_view(['GET'])  # Query book based upon their id
def getBook(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['POST'])  # add a book directly in database
def addBook(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return Response('Your Book has sucessfully been removed!')


class ApiOverview(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'The Api is Live!'}
        return Response(content)


class PdfFiles(APIView):

    def get(self, request):
        files = main()
        return Response(files)
