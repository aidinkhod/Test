from core.db import Database
from jinja2 import Environment, FileSystemLoader


class Controller:
    def __init__(self, request, response) -> None:
        self.request = request
        self.response = response
        self.env = Environment(loader=FileSystemLoader('templates'))


class PagesController(Controller):
    def home(self):
        template = self.env.get_template('index.html')
        body = template.render(posts=Database.posts, sum=Database.sum_amount(Database.sum))
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def add(self):
        with open('templates/add.html', 'r') as file:
            body = file.read()
        self.response.add_header("Content-Type", "text/html")
        self.response.set_body(body)


class PostsController(Controller):
    def posts(self, pk=None):
        data = Database.get_post_by_pk(pk=pk)
        if data:
            template = self.env.get_template('posts.html')
            body = template.render(post=data)
            self.response.add_header("Content-Type", "text/html")
            self.response.set_body(body)
