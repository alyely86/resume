from django import template
from blog_app.models import Post

register = template.Library()

# @register.simple_tag
# def new_post(Post):
#     lastes_post = Post[0]
#     return lastes_post


@register.inclusion_tag('blog/Include/most_view.html')
def most_view():
    posts = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('views')[:3]
    return {'posts':posts}