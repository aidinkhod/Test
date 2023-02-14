import os
from glob import glob
from os.path import isfile
from core import settings
from requests.request import Request
from requests.response import Response


class StaticResponder:
    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response
        self.static_dir = settings.STATIC_URL
        self.file = None
        self._check_file()


    @staticmethod
    def _get_file_path(path: str) -> str:
        try:
            return glob(path)[0]
        except IndexError as e:
            pass

    def _check_file(self):
        file_uri = self.request.uri
        path = './' + self.static_dir + file_uri
        file_path = self._get_file_path(path)
        if file_path and isfile(file_path):
            self.file_path = file_path

    def prepare_response(self) -> None:
        if self.file_path:
            file = open(self.file_path, 'rb')
            self.response.set_file_body(file)
