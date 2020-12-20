import pandas as pd 

def json_to_df(data):
    """
    Convert a JSON to a pandas DataFrame for use with the prediction model.
    Parameters:
     - data: a JSON object
    Returns:
     - a pandas DataFrame with missing values filled in
    """
    x = pd.DataFrame(data, index=[0])
    return x
