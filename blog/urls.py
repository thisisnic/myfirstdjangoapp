from django.urls import path
from . import views


# We assign a view called post_list to the root URL.
# The last part, name='post_list' is the name of the URL that will be used to identify the view
urlpatterns = [
	path('', views.post_list, name = 'post_list'),
]