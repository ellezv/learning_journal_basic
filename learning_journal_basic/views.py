"""Views for pyramid."""

from pyramid.view import view_config

ENTRIES = [
    {
        "title": "Monday 12/19: Day 12",
        "id": 1,
        "published_on": "Dec 20, 2016",
        "body": """Today I learned to make this.
          This is pretty awesome.
          I also learned to implement a Deque with Python. It was interesting to change partners this week as I get to know people I have never worked with. I think it went pretty well and even though I'm leaving later than expected I did learn a ton and the work was equally divided.
          I'm also getting feedback on our server assignment and so far I'm pretty happy with that.
          Looking forward to use Jinja2 and templating a bit more so writing this learning journal won't be as tedious anymore.
          I'm also excited to pitch my idea to the class tomorrow and really hope I will be able to convey how important for people with apraxia and other disabilities it could be.
          """
    },
    {
        "title": "Tuesday 12/20: Day 13",
        "id": 2,
        "published_on": "Dec 21, 2016",
        "body": """Today I learned that I don't know how to implement a Deque.
          So there's that.
          Jinja2 templating is really similar to Django templates which have a (very minimal) experience with so it wasn't too overwhelming.
          I'm excited to implement a database so I don't have to harcode this.
        """
    },
]


@view_config(route_name="home", renderer="templates/index.jinja2")
def home_list(request):
    """View for the home page."""
    return {"posts": ENTRIES}


@view_config(route_name="detail", renderer="templates/post_details.jinja2")
def detail(request):
    """View for the detail page."""
    return {"post": ENTRIES[int(request.matchdict['id']) - 1]}


@view_config(route_name="create", renderer="templates/new_post_form.jinja2")
def create(request):
    """View for create page."""
    return {"post": ENTRIES}


@view_config(route_name="update", renderer="templates/edit_post_form.jinja2")
def update(request):
    """View for update page."""
    return {"post": ENTRIES[int(request.matchdict['id']) - 1]}
