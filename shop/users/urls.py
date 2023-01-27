from django.urls import path, include
from users.views import Register
# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]
