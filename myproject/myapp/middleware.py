class MiddlewareAttributeSetter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.middleware_attr = "Seteado por Middleware"
        return self.get_response(request)