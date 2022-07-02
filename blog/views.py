from typing import Any, Dict
from django.views.generic.base import TemplateView
from .models import User


class IndexView(TemplateView):
    template_name: str = "index.html"


class PostView(TemplateView):
    template_name: str = "post.html"


class AuthorView(TemplateView):
    template_name: str = "author.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(AuthorView, self).get_context_data(**kwargs)
        context['author'] = User.objects.get(id=2)
        return context
