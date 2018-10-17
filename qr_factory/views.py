from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.datastructures import MultiValueDictKeyError

import qrcode
import base64

class QrGenView(APIView):
    def get(self, request, format=None):
        try:
            img = qrcode.make(request.GET['text'])
            response = HttpResponse(content_type="image/png")
            img.save(response, "PNG")
            response['Content-Disposition'] = 'attachment; filename="qr.png"'
            return response
        except MultiValueDictKeyError as e:
            return HttpResponseBadRequest(
                content='Falta parametro <text>'
            )
