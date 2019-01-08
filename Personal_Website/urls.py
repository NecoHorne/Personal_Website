from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Neco.urls')),
    path('', include('Blog.urls')),
    path('admin/', admin.site.urls),
]

# playing around with admin customization
admin.site.site_header = "Neco Horne Admin"
admin.site.site_title = "Neco Horne Admin Portal"
admin.site.index_title = "Welcome to the Admin Portal"

