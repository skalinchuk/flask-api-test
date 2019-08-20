import requests
from .settings import API_URL


def get_data() -> dict:
    """
    Sends the request to the API and returns the result as dictionary
    :return: dict
    """
    r = requests.get(url=API_URL)
    return r.json()


def get_books(order_by: str = '', order_dir: str = 'asc') -> list:
    """
    Returns list of books retrieved from the API, and sorted according to the parameters
    :param order_by: Sorting field
    :param order_dir: Sorting direction (asc|desc)
    :return: list
    """
    data = get_data()['books']
    if order_by and order_dir == 'desc':
        data.sort(key=lambda item: item[order_by].lower(), reverse=True)
    elif order_by and order_dir == 'asc':
        data.sort(key=lambda item: item[order_by].lower(), reverse=False)
    return data


def get_authors() -> list:
    """
    Returns list of authors for the retrieved set of books
    :return: list
    """
    books = get_data()['books']
    data = {}
    for book in books:
        if book['author'] not in data:
            data[book['author']] = {"name": book['author'], "books": []}
        data[book['author']]['books'].append(book)
    return [v for v in data.values()]