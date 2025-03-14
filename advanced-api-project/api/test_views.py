from django.test import TestCase
from api.models import Book
from rest_framework.test import APIRequestFactory


# Create your tests here.
class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title='The Great Gatsby', author='F. Scott Fitzgerald', publication_year='1925')
        Book.objects.create(title='The Catcher in the Rye', author='J.D. Salinger', publication_year='1951')
        Book.objects.create(title='To Kill a Mockingbird', author='Harper Lee', publication_year='1960')
        Book.objects.create(title='1984', author='George Orwell', publication_year='1949')
        

    def test_book_title(self):
        """Books are correctly identified by title"""
        the_great_gatsby = Book.objects.get(title='The Great Gatsby')
        the_catcher_in_the_rye = Book.objects.get(title='The Catcher in the Rye')
        to_kill_a_mockingbird = Book.objects.get(title='To Kill a Mockingbird')
        nineteen_eighty_four = Book.objects.get(title='1984')
        self.assertEqual(the_great_gatsby.title, 'The Great Gatsby')
        self.assertEqual(the_catcher_in_the_rye.title, 'The Catcher in the Rye')
        self.assertEqual(to_kill_a_mockingbird.title, 'To Kill a Mockingbird')
        self.assertEqual(nineteen_eighty_four.title, '1984')

factory = APIRequestFactory()
request = factory.get('/api/books/')
request = factory.post('/api/books/', {'title': '1984', 'author': 'George Orwell', 'publication_year': '1949'})
request = factory.put('/api/books/', {'title': '1984', 'author': 'George Orwell', 'publication_year': '1949'})
request = factory.delete('/api/books/', {'title': '1984', 'author': 'George Orwell', 'publication_year': '1949'})
