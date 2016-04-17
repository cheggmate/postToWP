from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.utils import timezone
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Post, Comment


class IndexView(generic.ListView):
	template_name = 'post/index.html'
	context_object_name = 'latest_articles'

	def get_queryset(self):
		return Post.objects.filter(
			pub_date__lte = timezone.now()
			).order_by('-pub_date')[:10]
	def index(request):
		latest_articles = Post.objects.order_by('-pub_date')[:10]
		context = {
			'latest_articles':latest_articles,
		}


class DetailView(generic.DetailView):
	model = Post
	template_name = 'post/writepost.html'
	

class viewOfPost(generic.DetailView):
	model = Post
	template_name = 'post/viewOfPost.html'



# Create your views here.
