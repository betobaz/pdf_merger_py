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
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=request.GET['box_size'],
                border=request.GET['border'],
            )
            qr.add_data(request.GET['text'])
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            response = HttpResponse(content_type="image/png")
            img.save(response, "PNG")
            response['Content-Disposition'] = 'attachment; filename="qr.png"'
            return response
        except MultiValueDictKeyError as e:
            return HttpResponseBadRequest(
                content='Falta parametro <text>'
            )
