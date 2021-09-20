import pytest

from library import create_app
from library.adapters import memory_repository
from library.adapters.memory_repository import MemoryRepository
from library.domain.model import Review, User

from utils import get_project_root

TEST_DATA_PATH = get_project_root() / "tests" / "data"


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(TEST_DATA_PATH, repo)

    list_of_users = [User("Ben","123456"), User("Timothy", "987654")]
    for user in list_of_users:
        repo.add_user(user)

    book_catalogue = repo.get_book_catalogue()
    book_one = book_catalogue[0]
    book_two = book_catalogue[1]
    list_of_reviews =[Review(book_one, "The book was average.", 3, repo.get_user("Ben")), Review(book_two, "The book was amazing.", 5, repo.get_user("Timothy"))]
    book_one.add_review(list_of_reviews[0])
    book_two.add_review(list_of_reviews[1])
    for review in list_of_reviews:
        repo.add_review(review)

    return repo


@pytest.fixture
def empty_memory_repo():
    repo = MemoryRepository()
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'TEST_DATA_PATH': TEST_DATA_PATH,               # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })
    return my_app.test_client()