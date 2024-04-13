import sys
sys.path.append('../')
import unittest
import pandas as pd
from src.loader import load_data

class TestDataCSV(unittest.TestCase):
    def test_load_data(self):
        # Define the file path for data.csv
        data_file_path = '../data/data.csv'
        
        # Define the expected column names
        expected_columns = ['article_id', 'source_id', 'source_name', 'author', 'title',
                            'description', 'url', 'url_to_image', 'published_at', 'content',
                            'category', 'full_content']
        
        # Load the data.csv file using the function to be tested
        loaded_data = load_data(data_file_path)
        
        # Get the actual column names
        actual_columns = loaded_data.columns.tolist()
        
        # Assertions to check if the loaded data has the expected column names
        self.assertEqual(actual_columns, expected_columns)

if __name__ == '__main__':
    unittest.main()