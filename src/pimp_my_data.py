# import os

# current_directory = os.getcwd()
# print("Current working directory:", current_directory)

# parent_dir = os.path.dirname(current_directory)
# print(parent_dir)

# file_dir = os.path.abspath(os.path.join(parent_dir, 'project_immo_regression', 'data', 'data_for_sale.json'))

# print(file_dir)

# parent_directory = os.pardir()
# print(os.pardir)

import os
import sys
import pandas as pd

class PimpMyData:
    """
    PimpMyData has 3 methods and 1 static method
    """
    @staticmethod
    def _get_file_path():
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        file_dir = os.path.abspath(os.path.join(parent_dir, 'data', 'data_for_sale.json'))
        return file_dir

    def __init__(self):
        
        data_file_path = PimpMyData._get_file_path
        
        if not os.path.isfile(data_file_path):
            raise FileNotFoundError(f"File '{data_file_path}' not found. Please check the file path.")
        
        self.dataframe_main = pd.read_json(data_file_path)
            
        self.dtypes = {
            "ïmmocode": "int32", 
            "price" : "int32",
            "price_per_sqmeter" : "float",
            "habitable_surface" : "float",
            "plot_area" : "float",
            "land_surface" : "float",
            "bedroom_count" : "int32",
            "room_count" : "int32"
        }


    def present_data(self, columns=None, choices=None, details=None, df=None):
        if df is None:
            result = self.dataframe_main.head()
        else:
            if columns is not None and choices is not None and details is not None:
                for choice in choices:
                    for detail in details:
                        for col in columns:
                            if choice == "display":    
                                if detail == "head":
                                    result = df.head()
                                elif detail == "tail":
                                    result = df.head()
                                elif detail == "info":
                                    result = df[col].info()
                                elif detail == "describe":
                                    result = df[col].describe()
                                else:
                                    result = self.dataframe_main.head()
                            elif choice == "value_counts":
                                result = df[col].value_counts()
        
        return result
                         

    def give_continuous(self, df=None, option=None, target=None):
        option_list = ["plot_area", "habitable_surface", "bedroom_count", "land_surface", "room_count"]
        target_list = ["price", "price_per_sqmeter"]
        if df is not None and option is not None and target is not None:
            if option in option_list and target in target_list:
                output = df[[target, option]]
            else:
                print("Try Again")
        else:
            print("Try Again")


    def give_categorical(self, df=None, option=None, target=None):
        if df is not None and option is not None and target is not None:
            if target == "price" and len(df[option]) <= 5: 
                dummies = pd.get_dummies(df[option])
                output = pd.concat(pd.DataFrame(df["price"]).reset_index(), dummies)
        return output
    
    def clean_dtypes_numerics(self, df=None):
        if df is not None:
            df = df.astype(dtype=self.dtypes)
        return df
    
