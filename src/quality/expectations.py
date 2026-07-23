"""
Great Expectations checks applied to the Bronze, Silver, and Gold Delta layers.
Results are combined into a single pass/fail decision that gates the Airflow pipeline.
"""

# Bronze layer: basic completeness
BRONZE_EXPECTATIONS = [
    ("book_id_not_null", "book_id", "ExpectColumnValuesToNotBeNull"),
    ("isbn_not_null", "isbn", "ExpectColumnValuesToNotBeNull"),
]

# Silver layer: deeper validation
SILVER_EXPECTATIONS = [
    ("book_id_not_null", "book_id", "ExpectColumnValuesToNotBeNull"),
    ("language_valid", "language", "ExpectColumnValuesToBeInSet", ["Arabic", "English"]),
    ("publication_year_reasonable", "publication_year", "ExpectColumnValuesToBeBetween", 1900, 2026),
]

# Gold layer: aggregate sanity
GOLD_EXPECTATIONS = [
    ("number_of_books_positive", "number_of_books", "ExpectColumnValuesToBeBetween", 1),
]

# See notebooks/SDAIA_Books_Platform.ipynb (Stage 5) for the full executable
# implementation using the Great Expectations fluent API.
