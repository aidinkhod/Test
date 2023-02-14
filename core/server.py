from socketserver import StreamRequestHandler, ThreadingMixIn, TCPServer
from urllib.parse import parse_qs

from core.controller import PostsController
from core.db import Database
from core.urls import router
from requests.request import Request
from requests.response import Response


class MyTCPHandler(StreamRequestHandler):
    def handle(self) -> None:
        data = Database.posts
        request = Request(self.rfile)

        response = Response(self.wfile)
        if request.body is not None:
            body = parse_qs(request.body)
            new_pk = 1
            for i in Database.posts:
                new_pk += 1
            Database.posts.append(
                {
                    'pk': new_pk,
                    'year': ''.join(body.get('year')),
                    'amount': ''.join(body.get('amount')),
                    'car': ''.join(body.get('car')),
                    'image': ''.join(body.get('image')),
                    'description': ''.join(body.get('description')),
                    'contacts': ''.join(body.get('contacts'))
                }
            )
        if '/posts/' in request.url:
            pk = int(request.url.split('/')[-1])
            controller = PostsController(request, response)
            controller.posts(pk=pk)
            response.send()
            return
        router.run(request, response)

        response.send()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass
