from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', views.index, name='index'),
    path('', views.index2, name='index'),
    # name='index' is name of the path a/
    path('b/', views.index1, name='index1')
]

handler404 = "myProject.views.page_not_found_view"