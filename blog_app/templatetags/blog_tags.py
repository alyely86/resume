from django import template
# from models import Post

register = template.Library()

@register.simple_tag
def new_post(Post):
    lastes_post = Post[0]
    return lastes_post
