from django.urls import path

from . import views

urlpatterns = [
    path('indx/',views.indexview),
    path('reg/',views.regview,name='register'),
    path('log/',views.logview,name='login'),
    path('lout/',views.loutview,name='logout'),
    path('addproduct/',views.addProductview,name='addproduct'),
    path('productlist/',views.productlistview,name='productlist'),

]