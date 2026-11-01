import requests


class ApiClient:
    def __init__(self, base_url, timeout=15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get(self, path, headers=None):
        url = self.base_url + path
        return self.session.get(
            url,
            headers=headers,
            timeout=self.timeout
        )

    def post(self, path, payload=None, headers=None):
        url = self.base_url + path
        return self.session.post(
            url,
            json=payload,
            headers=headers,
            timeout=self.timeout
        )

    def patch(self, path, payload=None, headers=None):
        url = self.base_url + path
        return self.session.patch(
            url,
            json=payload,
            headers=headers,
            timeout=self.timeout
        )

    def close(self):
        self.session.close()
