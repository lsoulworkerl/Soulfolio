from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from portfolio.views import ObjectLimitPaginationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ObjectLimitPaginationView.as_view(), name='Information'),
]
