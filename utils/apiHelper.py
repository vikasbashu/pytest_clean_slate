import requests


class API_Helper:

    base_url = None
    headers = None

    def __init__(self, url, headers=None):
        self.base_url = url
        self.headers = headers

    def get(self, end_point):
        return requests.get(self.base_url + end_point, headers=self.headers)

    def post(self, end_point, payload):
        return requests.post(self.base_url + end_point, data=payload, headers=self.headers)

    def put(self, end_point, payload):
        return requests.put(self.base_url + end_point, data=payload, headers=self.headers)

    def patch(self, end_point, payload):
        return requests.patch(self.base_url + end_point, data=payload, headers=self.headers)

    def delete(self, end_point):
        return requests.delete(self.base_url + end_point, headers=self.headers)
