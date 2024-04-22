from django.urls import path
from . import views
urlpatterns = [
    path("index/",views.index,name='index'),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("register/",views.register_user,name="register"),
    path("tache/<id>/",views.Taches,name="tache"),
    path("ajouter/<id>/",views.ajoutTache,name='ajouter'),
    path('afficher/<id>',views.affiche,name='affiche'),
    path('supprimer/<id>',views.supprimer,name='supprimer'),
    path('modifier/<id>',views.modifier,name='modifier')
]