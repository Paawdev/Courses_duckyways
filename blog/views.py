from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import CommentForm
from .models import Post

from django.core.paginator import Paginator

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    paginate_by = 3



from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, CategoryPost

def blog_list(request):
    query = request.GET.get("q")  # Manejo de búsqueda
    category = request.GET.get("category")  # Filtro de categorías
    blogs = Post.objects.filter(status=1).order_by("-created_on")

    if query:
        blogs = blogs.filter(title__icontains=query)  # Filtrar por título
    if category:
        blogs = blogs.filter(category_post__id=category)  # Filtrar por categoría

    paginator = Paginator(blogs, 3)  # 3 posts por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = CategoryPost.objects.all()  # Obtener categorías

    return render(request, "blog/blog.html", {"page_obj": page_obj, "categories": categories})

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = CategoryPost.objects.all()
    popular_posts = Post.objects.filter(status=1).order_by("-likes")[:5]  # Top 5 posts por likes

    return render(request, "blog/blog-detail.html", {
        "post": post,
        "categories": categories,
        "popular_posts": popular_posts,
    })
