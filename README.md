# Proyecto Django: Manejo de Request y Response

Este proyecto es una aplicación hecha en Django que demuestra el manejo de distintos tipos de `HttpRequest` y `HttpResponse`.

## URLs disponibles

- `/` → Landing Page  
- `/request/` → Muestra el método HTTP utilizado  
- `/request/app-attributes/` → Atributo personalizado definido en la vista  
- `/request/middleware/` → Atributo definido desde el middleware  
- `/request/querydict/` → Respuesta usando `QueryDict`  
- `/request/is-secure/` → Uso de `request.is_secure()`  
- `/home/` → Vista que maneja GET y POST con formulario  
- `/response/` → `HttpResponse` básico  
- `/response/subclasses/` → `HttpResponse` con encabezados personalizados  
- `/response/json/` → Respuesta JSON  
- `/response/streaming/` → Respuesta tipo *streaming*  
- `/response/file/` → Descarga de archivo desde el servidor  
- `/response/base/` → Uso de `HttpResponseBase`

## Cómo ejecutar el proyecto

1. Crear entorno virtual:

   ```bash
   python -m venv entornito
   
## Activarlo:
.\entornito\Scripts\activate

## Instalar Django:
pip install django

## Ejecutar el servidor:
python manage.py runserver
