from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView

# Create your views here.
class PostList(ListView):
	model =Post  ## in template [ object_list , post_list "nom de model +_list"]
	#context_object_name='all_posts'
	#template_name='post.html'
	ordering =['-created_at']
	#queryset =Post.objects.filter(active=True)

	#def get_queryset(self):
	#	return Post.objects.filter(active=True)

	def get_context_data(self,**kwargs):
		context =super().get_context_data(**kwargs)
		context['name']='abdelkader'
		return context


class PostDetail(DetailView):
	model=Post

class PostCreate():
	pass


class PostDelete():
	pass


class PostUpdate():
	pass