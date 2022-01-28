from django.urls import path

from payment import views
urlpatterns = [
	path("pay", views.add_payment, name="pay"),
]