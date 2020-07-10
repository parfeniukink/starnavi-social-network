from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    # Local
    path("api/v1/auth/", include('accounts.urls')),
    path("api/v1/", include('blog.urls'))
]
