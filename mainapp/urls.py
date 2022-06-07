from django.urls import path

from mainapp.views import create_website,get_website_by_code,retrive_all_websites,update_website,remove_website, WebsiteListView

app_name = 'mainapp'

urlpatterns = [
    path("create", create_website),
    path("retrive_websites", retrive_all_websites),
    path("retrive_website/<code>", get_website_by_code),
    path("delete/<code>", remove_website),
    path("update/<code>", update_website),
    path("filter/", WebsiteListView.as_view()),


]
