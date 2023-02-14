from requests import HTTPResponseCode


def not_found(request, response):
    response.set_status(HTTPResponseCode.NOT_FOUND)
    response.add_header("Content-Type", "text/html")
    response.set_body("<h1>404 Not found</h1>")


def internal_server_error(request, response):
    response.set_status(HTTPResponseCode.INTERNAL_SERVER_ERROR)
    response.add_header("Content-Type", "text/html")
    response.set_body("<h1>500 Not found</h1>")