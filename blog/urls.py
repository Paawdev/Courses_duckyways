from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.blog_list, name="blog_list"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]
# {% url 'post_detail' post.slug  %}