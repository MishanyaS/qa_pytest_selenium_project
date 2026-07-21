from __future__ import annotations

from typing import Any

import requests

from config import BASE_API_URL, REQUEST_TIMEOUT

class ApiClient:
    def __init__(self, session: requests.Session, base_url: str = BASE_API_URL, timeout: int = REQUEST_TIMEOUT) -> None:
        self.session = session
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
    
    def _url(self, endpoint: str) -> str:
        endpoint = endpoint.lstrip("/")

        return f"{self.base_url}/{endpoint}"
    
    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.session.get(self._url(endpoint), timeout=self.timeout, **kwargs)
    
    def post(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.session.post(self._url(endpoint), timeout=self.timeout, **kwargs)
    
    def put(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.session.put(self._url(endpoint), timeout=self.timeout, **kwargs)
    
    def patch(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.session.patch(self._url(endpoint), timeout=self.timeout, **kwargs)
    
    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.session.delete(self._url(endpoint), timeout=self.timeout, **kwargs)
