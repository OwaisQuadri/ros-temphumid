from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import SaveForm
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Temperature
from .serializers import TempSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class History(APIView):
    def get(self, request):
        temps = Temperature.objects.all()
        ser=TempSerializer(temps, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

class Home(APIView):
    def get(self,request):
        temp=Temperature.objects.last()
        ser=TempSerializer(temp)
        while Temperature.objects.count() > 60:#recorded every 1 mins, in the last hour
            #delete smallest ID object
            try:
                record=Temperature.objects.first()
                record.delete()
                print("record deleted")
            except:
                print("record DNE")
        return Response(ser.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self,request):
        ser=TempSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
