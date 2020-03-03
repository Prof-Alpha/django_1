from django.urls import path
from . import views
app_name = 'personal'
urlpatterns = [
		path('', views.main_page),
		path('test/', views.test, name='test'),
		path('shop_market/<int:qid>', views.details, name='details'),
]