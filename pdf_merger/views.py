from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from PyPDF2 import PdfFileMerger, PdfFileReader
from .models import Document
from django.core.files.base import ContentFile
import StringIO
import pprint

class PdfMergerView(APIView):
  parser_classes = (FileUploadParser,)
  def post(self, request, format=None):
    pprint.pprint(request.FILES)
    #newdoc = Document(docfile = request.FILES['file'])
    #newdoc.save()
    merger = PdfFileMerger()
    for file_upload in request.FILES:
      pprint.pprint(file_upload)
      #newdoc = Document(docfile = request.FILES[file_upload])
      #newdoc.save()
      pdfFileReader = PdfFileReader(request.FILES[file_upload])
      import ipdb; ipdb.set_trace()

      if pdfFileReader.isEncrypted:
        pdfFileReader.decrypt('sugarpdf_pdf_user_password')
      merger.append(pdfFileReader)

    merger.write("document-output.pdf")
    return Response({
      "data": request.DATA, 
      })

    def handle_uploaded_file(f):
      with open('upload/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
          destination.write(chunk)
