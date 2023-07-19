import json
import os

class Data_Processor:
    @staticmethod
    def data_loader(file_path):
        # Get the absolute path of the JSON file relative to data_processor.py
        json_file_path = os.path.join(os.path.dirname(__file__), 'data')
        
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        return data