import requests


def fetch(url: str, session: requests.Session):
    return session.get(url)


def page_exists(url: str, session: requests.Session):
    return fetch(url, session).status_code in range(200, 300)
