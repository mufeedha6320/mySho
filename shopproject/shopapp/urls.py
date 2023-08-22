
from django.urls import path
from shopapp import views
app_name = 'shopapp'

urlpatterns = [
    path('', views.allProCat,name="allProCat"),
    path('<slug:cat_slug>/', views.allProCat, name="products_by_category"),
    path('<slug:cat_slug>/<slug:pro_slug>/', views.productDetail, name="proCatDetail")
]
