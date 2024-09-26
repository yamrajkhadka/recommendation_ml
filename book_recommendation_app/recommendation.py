import pandas as pd
import numpy as np

# Sample recommendation function (replace with actual logic)
def get_recommendations(book_name):
    # Dummy book list for demonstration
    books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick", "Pride and Prejudice"]
    
    # Generate recommendations by excluding the selected book
    recommended_books = [book for book in books if book.lower() != book_name.lower()]
    
    return recommended_books  # Return the recommended books
