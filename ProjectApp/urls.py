from ProjectApp import views
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^product$',views.ProductApi),
    re_path(r'^product/([0-9]+)$',views.ProductApi),
    re_path(r'^RegisterCustomers$',views.RegisterCustomers),
    re_path(r'^LoginCustomer$',views.LoginUser),
    re_path(r'^ViewCustomers$',views.ViewCustomers),
    re_path(r'^Getorder$',views.Getorder),
    re_path(r'^Updateorder$',views.Updateorder),
    re_path(r'^product/savefile',views.SaveFile),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)