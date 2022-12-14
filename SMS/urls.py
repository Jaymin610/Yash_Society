"""SMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name = 'authentication/login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # including applications
    path('authentication/', include('authentication.urls')),
    path('accounting/', include('accounting.urls')),
    path('member-panel/', include('member_panel.urls')),
    path('admin-panel/', include('admin_panel.urls')),

    # including apis of application
    path('api/accounting/', include('accounting.api.urls')),
    path('api/member-panel/', include('member_panel.api.urls')),
    path('api/admin-panel/', include('admin_panel.api.urls')),
]

urlpatterns += static(  settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT
)