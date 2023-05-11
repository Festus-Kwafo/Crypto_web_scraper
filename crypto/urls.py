from django.urls import path
from django.conf.urls import url
from crypto import views


urlpatterns = [
    path('api/v1/run-scraper', views.StartScraping.as_view(), name="run_scraper"),
    path('api/v1/records', views.records_list, name="list_del_data"),

]

