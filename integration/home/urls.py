# from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("",views.home, name="home"), # most common mistake is forget ","
    path("task/",views.task, name="task"),
    # path("addTask/",views.addTask, name="addTask"),
]
