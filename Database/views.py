# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Database.models import Layer
from Database.serializers import *
from django.template import Template, Context
import datetime

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def layer_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        layers = Layer.objects.all()
        for layer in layers:
            layer.user = UserSerializer(layer.user).data
        serializer = LayerSerializer(layers, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def layer_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        layer = Layer.objects.get(pk=pk)
    except Layer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LayerSerializer(layer)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LayerSerializer(layer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        layer.delete()
        return HttpResponse(status=204)

@csrf_exempt
def mapas(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        #template = loader.get_template("Database/mapa.html")
        fp = open('/home/badillo/grunetafel/grunetafel/GrueneTafel/Database/mapaGoogle.html')
        t = Template(fp.read())
        fp.close()

        html = t.render(Context({'current_date': datetime.datetime.now()}))
        return HttpResponse(html)
