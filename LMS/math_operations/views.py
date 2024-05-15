from django.shortcuts import render
from django.http import HttpResponse


def index(request, int1=0, int2=0):
    return HttpResponse(f'Int1: {int1}<p>Int2: {int2}')

def sum(request, int1=0, int2=0):
    return HttpResponse(f'Sum: {int(int1)+int(int2)}')

def sub(request, int1=0, int2=0):
    return HttpResponse(f'Sub: {int(int1)-int(int2)}')


