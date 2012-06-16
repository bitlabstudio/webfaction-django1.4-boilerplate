"""Project wide templatetags."""
from django import template

register = template.Library()


@register.simple_tag
def navactive(request, url, exact=0):
    """
    Returns ``active`` if the given URL is in the url path, otherwise ''.

    Use it in your templates like so::

        {% load project_tags %}
        <a href="#" class="{% navactive request "/" exact=1 %}">Home</a>

    :param request: A request instance.
    :param url: A string representing a part of the URL that needs to exist
      in order for this method to return ``True``.
    :param exact: If ``1`` then the parameter ``url`` must be equal to
      ``request.path``, otherwise the parameter ``url`` can just be a part of
      ``request.path``.

    """
    if exact:
        if url == request.path:
            return "active"
        return ""

    if url in request.path:
        return "active"
    return ""
