from django.shortcuts import render
import time

# Create your views here.
from django.http import (
    HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse, HttpResponseBase
)
from django.views.decorators.csrf import csrf_exempt

# Landing Page
def landing_page(request):
    return HttpResponse("Bienvenido a la Landing Page")

# Responder por HttpRequest
def request_view(request):
    return HttpResponse(f"Método HTTP utilizado: {request.method}")

# Responder con un atributo que fue seteado en la vista
def request_app_attributes(request):
    request.custom_attr = "Este es un atributo definido en la vista"
    return HttpResponse(f"Atributo personalizado: {request.custom_attr}")

# Responder con un atributo seteado en el Middleware
def request_middleware(request):
    valor = getattr(request, 'middleware_attr', 'No seteado')
    return HttpResponse(f"Atributo desde el middleware: {valor}")

# Responder con un objeto QueryDict
def request_querydict(request):
    query_params = request.GET.dict()
    return JsonResponse({"QueryDict": query_params})

# Utilizar HttpRequest.is_secure()
def request_is_secure(request):
    return HttpResponse(f"¿Es segura la conexión?: {request.is_secure()}")

# Demostrar manejo de GET y POST con plantilla HTML
@csrf_exempt
def home(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre", "Sin nombre")
        return HttpResponse(f"POST recibido. Nombre enviado: {nombre}")
    elif request.method == 'GET' and 'nombre' in request.GET:
        nombre = request.GET.get("nombre", "Sin nombre")
        return HttpResponse(f"GET recibido. Nombre enviado: {nombre}")
    return render(request, 'home.html')

# HttpResponse básico
def basic_response(request):
    return HttpResponse("Esta es una respuesta básica de HttpResponse")

# HttpResponse con encabezados
def response_with_headers(request):
    response = HttpResponse("Respuesta con encabezados")
    response['X-Custom-Header'] = 'Este es un encabezado personalizado'
    return response

# Responder con JSON
def json_response(request):
    data = {"mensaje": "Hola desde JSON"}
    return JsonResponse(data)


# Streaming response
def streaming_response(request):
    def generate():
        yield "Streaming parte 1\n"
        time.sleep(1)
        yield "Streaming parte 2\n"
        time.sleep(1)
        yield "Streaming parte 3\n"
    return StreamingHttpResponse(generate(), content_type="text/plain")


# Responder con un archivo
def file_response(request):
    archivo = open(__file__, 'rb')  # archivo actual como ejemplo
    return FileResponse(archivo, as_attachment=True, filename="views.py")

# Usar HttpResponseBase
def response_base(request):
    return HttpResponseBase(content="Respuesta usando HttpResponseBase", content_type="text/plain")
