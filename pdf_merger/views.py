from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from PyPDF2 import PdfFileMerger, PdfFileReader
from base64 import b64encode
import os

class PdfMergerView(APIView):
  parser_classes = (FileUploadParser,)
  def post(self, request, format=None):
    merger = PdfFileMerger()
    filedata = request.FILES.itervalues().next()
    for file_upload in request.FILES:
      pdfFileReader = PdfFileReader(request.FILES[file_upload])
      merger.append(pdfFileReader)
    filename = str(filedata.name)
    merger.write(filename)
    file_new = open(filename)
    file_content = b64encode(file_new.read())
    file_new.close()
    os.remove(filename)
    return Response({"file": file_content})


    def handle_uploaded_file(f):
      with open('upload/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
          destination.write(chunk)
