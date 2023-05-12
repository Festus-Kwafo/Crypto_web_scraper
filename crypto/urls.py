from django.urls import path
from crypto import views


urlpatterns = [
    path('api/v1/run-scraper', views.start_scraping, name="run_scraper"),
    path('api/v1/records', views.records_list, name="list_del_data"),

]

