from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from PyPDF2 import PdfFileMerger, PdfFileReader
from base64 import b64encode
import os
import logging
#logger = logging.getLogger(__name__)
logging.basicConfig(filename="sample.log", level=logging.INFO)

class PdfMergerView(APIView):
  parser_classes = (FileUploadParser,)

  def post(self, request, format=None):
    #logging.info("PdfFileMerger:starting")
    try:
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
      #os.remove(filename)
      #logger.debug("some message")
      return Response({"file": file_content})
    except:
      logging.error("PdfFileMerger:error:{0}".format(sys.exc_info()[0]))
      return Response({"error": sys.exc_info()[0]})


    def handle_uploaded_file(f):
      with open('upload/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
          destination.write(chunk)
