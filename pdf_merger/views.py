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
    logging.info("Start")
    try:
      merger = PdfFileMerger()
      logging.info("merger test")
      firstFile = None
      for filename, file in request.FILES.iteritems():
        logging.info("file %s".filename)
        if firstFile == None:
          firstFile = request.FILES[filename]
        pdfFileReader = PdfFileReader(request.FILES[filename])
        merger.append(pdfFileReader)
      filename = str(firstFile.name)
      merger.write(filename)
      file_new = open(filename)
      file_content = b64encode(file_new.read())
      file_new.close()
      #os.remove(filename)
      #logger.debug("some message")

      logging.info("finish")
      return Response({"file": file_content})
    except:
      print "Unexpected error:", sys.exc_info()[0]
      log.exception("Error!")
      logging.info("Errro")
      return Response({"error": sys.exc_info()[0]})


    def handle_uploaded_file(f):
      with open('upload/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
          destination.write(chunk)
