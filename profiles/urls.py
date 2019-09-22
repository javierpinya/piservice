from django.urls import path
from .views import ProfileListView, ProfileDetailView

profiles_patterns = ([
    #path('', ProfileListView.as_view(), name='list'),
    #path('<username>/', ProfileDetailView.as_view(), name='detail'),
    path('perfiles/', ProfileListView.as_view(), name='list'),
    path('perfil/<dni>/', ProfileDetailView.as_view(), name='detail'),
], 'profiles')