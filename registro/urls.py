

from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('', views.index, name="index"),
    
    path('registro/crear',views.crear,name="crear"),
    path('registro/eliminar/<int:id>',views.eliminar,name="eliminar"),
    path('registro/editar',views.editar,name="editar"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('administrar/',views.administrar, name="administrar"),
    path('administrar/registPerro',views.registPerro, name='registPerro'),
    path('administrar/editPerro',views.editPerro, name='editPerro'),
    path('galeria', views.galeria, name='galeria')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
