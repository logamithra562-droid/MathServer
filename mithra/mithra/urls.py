from django.urls import path
from mathapp import views
urlpatterns = [path('', views.calculate_Total, name='Total')]