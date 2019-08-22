from django.urls import path
from .views import SignUpView, ProfileUpdate

urlpatterns = [

	path('profile/', ProfileUpdate.as_view(), name="profile"),
	path('signup/', SignUpView.as_view(), name="signup"),
]