from django.urls import path
from app import views
urlpatterns = [
    path('about',views.About,name='about'),
    path('',views.Home,name="home"),
    path('usecase',views.Usecases,name="usecase"),
    path('products',views.Products,name="products"),
    path('productdetails/<int:pk>',views.Productdetails,name="productdetails"),



]
