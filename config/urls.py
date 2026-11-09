from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def inicio(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Mi Proyecto Django</title>
            </head>
            <body style="text-align:center; font-family:Arial; margin-top:100px;">
                <h1>Bienvenido a mi proyecto Django</h1>
                <p>Aplicación desplegada correctamente en PythonAnywhere.</p>
                <p>Proyecto desarrollado con Django.</p>
                <a href="/admin/">Ir al panel de administración</a>
            </body>
        </html>
    """)


urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
]