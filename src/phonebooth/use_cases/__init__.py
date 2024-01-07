from dataclasses import dataclass

class UseCase:
    @dataclass(kw_only=True)
    class Request:
        def __post_init__(self):
            self.validate()

        def validate(self):
            pass
    
    @dataclass(kw_only=True)
    class Response:
        pass

    def __call__(self, request):
        if not isinstance(request, UseCase.Request):
            raise TypeError('Not a request type')
        return self.execute(request)

    def execute(self, request):
        raise NotImplementedError('Not implemented')
