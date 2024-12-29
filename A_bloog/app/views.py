from django.template import loader
from django.http import HttpResponse
from .models import Post


# Create your views here.
def get_page(request):
    results = Post.objects.all().values()
    template = loader.get_template("index.html")

    context = {
        "results": results,
    }
    return HttpResponse(template.render(context, request))
