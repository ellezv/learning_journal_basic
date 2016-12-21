"""Views for pyramid."""

from pyramid.view import view_config
import os


HERE = os.path.dirname(__file__)

ENTRIES = [
        {
        "title": "Entry 1",
        "id": 1,
        "creation_date": "Dec 20, 2016",
        "body": "I learned some stuff about some other stuff."},
        {"title": "Entry 2",
        "id": 2,
        "creation_date": "Dec 21, 2016",
        "body": "I learned some stuff about some other stuff."},
        {"title": "Entry 3",
        "id": 3,
        "creation_date": "Dec 23, 2016",
        "body": "I learned some stuff about some other stuff."}

]

@view_config(route_name="home", renderer="templates/list.jinja2")
def home_list(request):
    """View for the home page."""
    # imported_text = open(os.path.join(HERE, 'templates/index.html')).read()
    # # return Response(imported_text)
    all_my_stuff = [
        "pens",
        "book",
        "laptop",
        "more stuff",
        "even more stuff"
    ]
    return {"bag_list": all_my_stuff}


@view_config(route_name="detail", renderer="string")
def detail(request):
    """View for the detail page."""
    imported_text = open(os.path.join(HERE, 'data/day11.html')).read()
    # return Response(imported_text)
    return imported_text


@view_config(route_name="create", renderer="string")
def create(request):
    """View for create page."""
    imported_text = open(os.path.join(HERE, 'templates/new_post_form.html')).read()
    # return Response(imported_text)
    return imported_text


@view_config(route_name="update", renderer="string")
def update(request):
    """View for update page."""
    imported_text = open(os.path.join(HERE, 'templates/edit_post_form.html')).read()
    # return Response(imported_text)
    return imported_text


# def includeme(config):
#     """Include me function."""
#     config.add_view(home_list, route_name='home')
#     config.add_view(detail, route_name='detail')
#     config.add_view(create, route_name='create')
#     config.add_view(update, route_name='update')
