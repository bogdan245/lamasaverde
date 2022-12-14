from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .form import PostForm
from django.urls import reverse_lazy
import datetime

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    # ordering = ['-id']
    cats = Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context





def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace("-", ' ')) #category e definit in model
    context = {}
    context['cats'] = cats.title().replace('-', ' ')
    context['category_post'] = category_post
    cat_menu = Category.objects.all()
    context['cat_menu'] = cat_menu
    return render(request, 'categories.html', context)


# def CategoryListView(request, cats):
#     cat_menu_list = Category.objects.all()
#     return render(request, 'categories.html', {'cat_menu_list': cat_menu_list})



class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategory(CreateView):
    model = Category
    form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategory, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(EditPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
