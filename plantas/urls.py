from django.urls import path
from .views import index, nosotros, galeria, plantas, crear, eliminar, modificar, contacto, registrar
#CON LAS COMILLAS SIMPLES EN path('',) EL SERVIDOR
#SE ABRE EN EL HTML DE INDEX
urlpatterns = [
    path('',index, name="index"),
    path('nosotros/',nosotros, name="nosotros"),
    path('galeria/',galeria, name="galeria"),
    path('plantas/',plantas, name="plantas"),
    path('crear/',crear, name="crear"),
    path('eliminar/<id>',eliminar, name="eliminar"),
    path('modificar/<id>',modificar, name="modificar"),
    path('contacto/',contacto, name="contacto"),
    path('registrar/', registrar, name="registrar"),
]