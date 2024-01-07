from phonebooth.use_cases import UseCase
from dataclasses import dataclass

class PerformCall(UseCase):

    @dataclass
    class Request(UseCase.Request):
        to: str

    def execute(self, request):
        print('Making call with the API')
