import sys
sys.path.append('../')  # Add the parent directory to the module search path

import pandas as pd
from src.loader import load_data
from src.utils import parse_url

# Import the functions you want to test

# Function 1: load_data
def test_load_data():
    # Define the file paths for test data
    data_file_path = 'path/to/data.csv'
    rating_file_path = 'path/to/rating.csv'
    # Load the data using the load_data function
    data = load_data(data_file_path)
    rating = load_data(rating_file_path)
    
    # Assert that the loaded data is of the correct type (DataFrame)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(rating, pd.DataFrame)
    
    # Assertion: Check if the loaded data has the expected number of rows
    # assert len(data) == 1000
    # assert len(rating) == 500
    
    # Check if the loaded data has the expected columns
    data_columns = ['article_id', 'source_id', 'source_name', 'author', 'title',
       'description', 'url', 'url_to_image', 'published_at', 'content',
       'category', 'full_content']
    
    rating_columns =['article_id', 'source_id', 'source_name', 'author', 'title',
       'description', 'url', 'url_to_image', 'published_at', 'content',
       'category', 'article', 'title_sentiment']
    
    assert data.columns.tolist() == data_columns
    assert rating.columns.tolist() == rating_columns

# Function 2: parse_url
def test_parse_url():
    # Define a test URL
    url = 'https://www.example.com'
    
    # Call the parse_url function
    parsed_url = parse_url(url)
    
    # Assert that the parsed URL has the expected components
    assert parsed_url.scheme == 'https'
    assert parsed_url.netloc == 'www.example.com'
    assert parsed_url.path == ''
    assert parsed_url.params == ''
    assert parsed_url.query == ''
    assert parsed_url.fragment == ''
    
    # Add additional assertions as needed for the specific requirements of the URL parsing

# Run the tests
def run_tests():
    test_load_data()
    test_parse_url()

# Execute the tests
run_tests()