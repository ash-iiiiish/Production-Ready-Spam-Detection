import os
import pandas as pd

def load_data(filename):
    # Project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build data path
    data_path = os.path.join(project_root, "data", filename)

    # DEBUG PRINT (INSIDE FUNCTION)
    print("Looking for file at:", data_path)

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File not found at: {data_path}")

    df = pd.read_csv(data_path)
    df.columns = ["label", "message"]
    return df
