from typing import BinaryIO


class Request:
    def __init__(self, file: BinaryIO):
        self.file = file
        self.method = ''
        self.url = ''
        self.protocol = ''
        self.headers = {}
        self.body = None
        self.parse_request_data()
        self.parse_headers()
        self.parse_body()

    def parse_body(self):
        content_length = self.headers.get('Content-Length')
        if content_length:
            self.body = self.file.read(int(content_length)).decode()

    def parse_request_data(self) -> None:
        request_data = self.read_line()
        split_request_line = request_data.split()
        self.method, self.url, self.protocol = split_request_line
        if self.protocol != 'HTTP/1.1':
            raise ValueError("Incorrect protocol version")

    def parse_headers(self) -> None:
        while True:
            header = self.read_line()
            if header == '':
                break
            name, value = header.split(': ')
            self.headers[name] = value

    def read_line(self) -> str:
        return self.file.readline().decode().strip()
