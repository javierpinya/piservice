from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from vehiculos.models import Cliente

# Create your views here.

class ProfileListView(ListView):
	model = Cliente
	template_name = "profiles/profile_list.html"
	#paginated_by = 6

class ProfileDetailView(DetailView):
	model = Cliente
	template_name = "profiles/profile_detail.html"

	def get_object(self):
		return get_object_or_404(Cliente, dni=self.kwargs['dni'])
	 	#context = super().get_context_data(**kwargs)
		#context['filter'] = ClienteVehiculoFilter(self.request.GET, queryset=self.get_queryset())
		#return context
        