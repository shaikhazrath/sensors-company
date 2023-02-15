from django.urls import path
from app import views
urlpatterns = [
    path('about',views.About,name='about'),
    path('',views.Home,name="home"),
    path('usecase/<str:pk>',views.Usecases,name="usecase"),
    path('products/<str:pk>',views.Products,name="products"),
    path('productdetails/<int:pk>',views.Productdetails,name="productdetails"),
    path('contact',views.Contact,name='contact'),
]
