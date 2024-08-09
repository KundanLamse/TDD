import pytest 
from unittest.mock import MagicMock
from Library import LibManagement
#creating mock objects for mimicking the database interactions
@pytest.fixture
def db_connect():
    db=MagicMock()
    db.conn=MagicMock()
    db.cursor=MagicMock()
    return db
#passing the objects to the test functions to check whether the data gets added to the database correctly or not
def testing_add_book(db_connect):
    lib=LibManagement(db_connect)
    lib.add_book('123-456-789','William Shakespeare','Othello','1622')
    db_connect.cursor.execute.assert_called_once_with(
        "INSERT INTO books (ISBN, Author, Title, Year, Count) VALUES (%s, %s, %s, %s, %s)",
        ('978-3-16-148410-0', 'George Orwell', '1984', 1949, 5)
    )
    db_connect.conn.commit.assert_called_once()
