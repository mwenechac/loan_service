from django.urls import path

from loan import views
urlpatterns = [
	path("initiate", views.initiate_loan, name="initiate"),

]
