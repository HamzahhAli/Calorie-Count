from django.urls import path, include
from . import views as v

urlpatterns = [
    # path('', v.count),
    path('foodinfo/', v.foodinfo, name = 'foodinfo'),
    path('', v.count, name='count'),
    path('deleteitem/<int:item_id>/', v.deleteItem, name = 'deleteitem'),
    path('calorielimit/<int:pk>/', v.CalLimit, name = 'calorielimit'),
    path('numbers/', v.numbers, name = 'numbers')
    
]