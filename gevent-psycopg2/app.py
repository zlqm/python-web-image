def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    path = environ['PATH_INFO'][1:] or 'web'
    return [f'hello {path}'.encode()]
