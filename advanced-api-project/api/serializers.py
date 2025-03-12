import datetime
from .models import Book, Author
from rest_framework import serializers

# The BookSerializer is used to serialize and deserialize Book instances.
# It converts Book model instances into JSON format and vice versa.
# The author field is a primary key related field, which means it will be represented by the author's primary key (id) in the serialized data.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # The validation_time method ensures that the publication year is not in the future.
    def validation_time(self, data):
        if data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("Year must be a positive number")
        return data
    
    
# The AuthorSerializer is used to serialize and deserialize Author instances.
# It converts Author model instances into JSON format and vice versa.
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
