from django.urls import path

from balance import views
urlpatterns = [
	path("get-balance", views.get_balance, name="get_balance"),
]