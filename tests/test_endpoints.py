import pytest

from app.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_get_books(client):
    """Check if the list of books is returned"""
    rv = client.get('/books')
    json_data = rv.get_json()
    assert type(json_data) is list
    if len(json_data) > 0:
        assert 'author' in json_data[0]
        assert 'published' in json_data[0]


def test_get_authors(client):
    """Check if the list of authors is returned"""
    rv = client.get('/authors')
    json_data = rv.get_json()
    assert type(json_data) is list
    if len(json_data) > 0:
        assert 'name' in json_data[0]
        assert type(json_data[0]['books']) is list


def test_get_books_sorted_by_title_ascending(client):
    """Check if books are ordered by title in ascending order"""
    rv = client.get('/books', query_string={'order_by': 'title', 'order_dir': 'asc'})
    json_data = rv.get_json()
    assert type(json_data) is list
    if len(json_data) > 1:
        assert json_data[0]['title'] < json_data[1]['title']

def test_get_books_sorted_by_title_descending(client):
    """Check if books are ordered by title in ascending order"""
    rv = client.get('/books', query_string={'order_by': 'title', 'order_dir': 'desc'})
    json_data = rv.get_json()
    assert type(json_data) is list
    if len(json_data) > 1:
        assert json_data[0]['title'] > json_data[1]['title']


def test_get_books_sorted_by_published_ascending(client):
    """Check if books are ordered by published date in ascending order"""
    rv = client.get('/books', query_string={'order_by': 'published', 'order_dir': 'asc'})
    json_data = rv.get_json()
    assert type(json_data) is list
    if len(json_data) > 1:
        assert json_data[0]['published'] < json_data[1]['published']

def test_get_books_sorted_by_published_descending(client):
    """Check if books are ordered by published date in descending order"""
    rv = client.get('/books', query_string={'order_by': 'published', 'order_dir': 'desc'})
    json_data = rv.get_json()
    assert type(json_data) is list
    if len(json_data) > 1:
        assert json_data[0]['published'] > json_data[1]['published']
