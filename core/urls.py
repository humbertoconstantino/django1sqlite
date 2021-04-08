from django.urls import path
from .views import index,contato,produto

urlpatterns = [
    path('', index,name='index'),
    path('contato', contato,name='contato'),
                                    #name para usar no html <a>
    path('produto/<int:pk>', produto, name='produto')
]