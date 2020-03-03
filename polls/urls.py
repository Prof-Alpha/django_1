from django.urls import path
from . import views

app_name:'polls'
urlpatterns = [
        path('', views.index, name='index'),
        path('<int:qu_num>/results/', views.results, name='results'),
        path('<int:qu_number>/vote/', views.vote, name='vote')
]
