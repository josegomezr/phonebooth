from phonebooth.use_cases import UseCase
from dataclasses import dataclass, MISSING

class PerformCall(UseCase):

    @dataclass
    class Request(UseCase.Request):
        to: str
        def validate(self):
            if not self.to:
                raise TypeError('Missing "to" field')

    def execute(self, request):
        print('Making call with the API')
