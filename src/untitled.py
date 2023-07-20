import os
import pandas as pd

class PimpMyData:
    def __init__(self):
        self.dtypes = {
            "immocode": "int32", 
            "price": "int32",
            "price_per_sqmeter": "float",
            "habitable_surface": "float",
            "plot_area": "float",
            "land_surface": "float",
            "bedroom_count": "int32",
            "room_count": "int32"
        }
        self.option_continuous = ["plot_area", "habitable_surface", "bedroom_count", "land_surface", "room_count"]
        self.targets = ["price", "price_per_sqmeter"]
        self.option_categorical = ["type", "subtype", "epc_score", "immo_status", "postalcode", "municipality", "district", "province", "region"]
        self.main_df = self.load_dataframe("data", "data_forsale_new.csv")

    @staticmethod
    def _get_file_path(folder, name):
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        file_dir = os.path.abspath(os.path.join(parent_dir, folder, name))
        return file_dir

    def load_dataframe(self, folder, name):
        file_path = self._get_file_path(folder, name)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{name}' not found in folder '{folder}'. Please check the file path.")
        return pd.read_csv(file_path)

    def present_data(self, column=None, choice=None, details=None, df=None):
        if column is not None and choice is not None and df is not None:
            if column in self.option_continuous and choice == "summarize":
                summary = df[column].describe()
                return summary
            elif column in self.option_categorical and choice == "summarize":
                summary = df[column].describe()
                return summary

    def give_continuous(self, df, target):
        if target in self.targets:
            df_price_continuous = df[[target, "plot_area", "habitable_surface", "bedroom_count", "land_surface", "room_count"]]
            return df_price_continuous
        else:
            raise ValueError(f"Invalid target '{target}'. The target must be one of: {', '.join(self.targets)}")

    def give_categorical(self, df=None, option=None, target=None):
        if df is not None and option is not None and target is not None:
            if target in self.targets and len(df[option]) <= 5: 
                dummies = pd.get_dummies(df[option])
                output = pd.concat([df[target], dummies], axis=1)
                return output
            else:
                return "Please check your parameters. Maybe your variable is too complex."

    def clean_dtypes_numerics(self, df=None):
        if df is not None:
            return df.astype(dtype=self.dtypes)

    def give_subset(self, df, subset):
        new_subset = df[subset]
        return new_subset

    def give_nan_columns(self, df):
        nan_columns = df.columns[df.isna().any()].tolist()
        return [f"Column '{col}' has missing values." for col in nan_columns]

    def describe_data(self, df, subject=None):
        if subject is None:
            return df.describe()
        else:
            return df[subject].describe()
