from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book, Author
from api.serializers import BookSerializer

class BookAPITestCase(TestCase):
    def setUp(self):
        """
        Set up test data.
        """
        self.client = APIClient()
        self.author = Author.objects.create(Name="F. Scott Fitzgerald")
        self.book1 = Book.objects.create(title="The Great Gatsby", publication_year=1925, author=self.author)
        self.book2 = Book.objects.create(title="The Catcher in the Rye", publication_year=1951, author=self.author)
        self.book3 = Book.objects.create(title="To Kill a Mockingbird", publication_year=1960, author=self.author)
        self.book4 = Book.objects.create(title="1984", publication_year=1949, author=self.author)

    # Test CRUD Operations

    def test_get_book_list(self):
        """
        Test retrieving a list of books.
        """
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_book_detail(self):
        """
        Test retrieving a single book.
        """
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        """
        Test creating a new book.
        """
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 5)

    def test_update_book(self):
        """
        Test updating a book.
        """
        url = reverse('book-update', args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 1926,
            "author": self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 3)

    # Test Filtering, Searching, and Ordering

    def test_filter_books_by_title(self):
        """
        Test filtering books by title.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'title': 'The Great Gatsby'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Great Gatsby')

    def test_search_books_by_author(self):
        """
        Test searching books by author.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Fitzgerald'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Great Gatsby')

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')
        self.assertEqual(response.data[1]['title'], 'The Great Gatsby')
        self.assertEqual(response.data[2]['title'], 'The Catcher in the Rye')
        self.assertEqual(response.data[3]['title'], 'To Kill a Mockingbird')

    # Test Permissions and Authentication

    def test_unauthenticated_user_cannot_create_book(self):
        """
        Test that unauthenticated users cannot create books.
        """
        self.client.force_authenticate(user=None)  # Ensure no user is authenticated
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        """
        Test that authenticated users can create books.
        """
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=user)
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)