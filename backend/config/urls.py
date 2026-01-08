
from django.contrib import admin
from django.urls import path, include
from allauth.account.decorators import secure_admin_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path("_allauth/", include("allauth.headless.urls")),
]

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)
