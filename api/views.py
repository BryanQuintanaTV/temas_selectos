from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
import json
from chat import get_response
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
import time
from .models import Report
from django.utils.dateparse import parse_datetime

# Create your views here.
# Class with the actions that endpoints are going to do
# {url}/api/v1/chat/
class ItemList(APIView):

    # POST {url}/api/v1/chat/
    @csrf_exempt
    def post(self, request):
        # message = request.data.get('message', '')

        # return Response({'response': response})
        # Procesar el body JSON recibido

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user_message = body.get('message', '')

        if not user_message:
            return Response({'error': 'No message provided'}, status=400)
        #
        response = get_response(user_message)

        # Aquí iría tu lógica real de chatbot (por ahora simulemos una respuesta)
        full_response = response

        # Función que envía fragmentos poco a poco
        def event_stream():
            for char in full_response:
                yield f"data: {char}\n\n"
                time.sleep(0.025)  # simula streaming lento (opcional)

            # Al final envías una marca de fin
            yield "data:    [DONE]\n\n"

        # Streaming HTTP Response para SSE
        response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        return response

class ItemReport(APIView):

    # POST {url}/api/v1/report/
    @csrf_exempt
    def post(self, request):

        try:
            data = json.loads(request.body)

            Report.objects.create(
                message_send=data['message_send'],
                message_receive=data['message_receive'],
                date=parse_datetime(data['date']),
                dataset_version=data['dataset_version'],
                message_report=data['message_report'],
            )

            return JsonResponse({"message": "Reporte guardado en la base de datos"}, status=201)

        except Exception as e:
            print("Error al guardar:", e)
            return JsonResponse({"error": "Error al guardar el reporte"}, status=500)