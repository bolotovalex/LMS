from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def test(request, param1='Undefined', param2='Undefined', param3='Undefined'):
    return HttpResponse(f'Param1: {param1} <p>Param2: {param2} <p>Param3: {param3}')