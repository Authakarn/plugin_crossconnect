from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import plugin_crossconnect

class plugin_crossconnectView(View):
    """Display Crossconnect details"""

    queryset = plugin_crossconnect.objects.all()

    def get(self, request, pk):
        """ Get request."""
        plugin_crossconnect_obj = get_object_or_404(self.queryset, pk=pk)

        return render(
            request,
            "plugin_crossconnect/plugin_crossconnect.html",
            {
                "plugin_crossconnect": plugin_crossconnect_obj,
            },
        )