from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('inicio/', views.inicio, name = "Inicio"),

    path('posibleJugador/', views.posibleJugador, name="posibleJugador"),
    
    path('login/', views.login_request, name="Login"),
    
    path('register/', views.register, name="register"),
    
    path('leerPosiblesJugadores', views.leerPosiblesJugadores, name="leerPosiblesJugadores"),
    
    path('leerPosiblesJugadoresDetalles', views.leerPosiblesJugadoresDetalles, name="leerPosiblesJugadoresDetalles"),
    
    path('inicio/about/', views.about, name = "About"),

    path('logout/', LogoutView.as_view(template_name = 'AppCoder/logout.html'), name="Logout"),

    path('editarUsuario/', views.editarUsuario, name="EditarUsuario")

]