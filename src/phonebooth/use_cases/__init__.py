from dataclasses import dataclass

class UseCase:
    @dataclass(kw_only=True)
    class Request:
        pass

    def __call__(self, request):
        if instanceof(request, Request):
            raise TypeError('Not a request type')
        return self.execute(request)

    def execute(self, request):
        raise NotImplementedError('Not implemented')