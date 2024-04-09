"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from core.views import (
    register as RegisterView,
    login as LoginView,
    logout as LogoutView,
    me as MeView,
    # test views
    test_token as TestTokenView,
    test_protected as TestProtectedView,
    sessions as SessionsView,
)

from test_auth.views import (
    click as ClickView,
    get_clicks as GetClicksView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('sessions/', SessionsView, name='sessions'),
    path('me/', MeView, name='me'),
    # test views
    path('test-token/', TestTokenView, name='test-token'),
    path('test-protected/', TestProtectedView, name='test-protected'),
    path('click/', ClickView, name='click'),
    path('get-clicks/<int:user_id>/', GetClicksView, name='get-clicks'),
]
