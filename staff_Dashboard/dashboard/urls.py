from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard,name="dashboard"),
    path('add_staff/' , views.add_staff,name="add_staff"),
    path('edit_staff/<int:s_id>/' , views.edit_staff,name="edit_staff"),
#    path('update_staff/<int:s_id>' , views.update_staff,name="update_staff"),
    path('delete_staff/<int:s_id>/' , views.delete_staff,name="delete_staff"),
    ]
