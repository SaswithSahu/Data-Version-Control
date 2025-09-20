import pandas as pd
import numpy as np
import os


def load_data():
    """Load dummy data into a DataFrame using pandas."""
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"],
        "Occupation": ["Engineer", "Doctor", "Artist"]
    }
    df = pd.DataFrame(data)
    return df

def update_data(df):
    """Update the DataFrame with new data."""
    df.loc[len(df)] = ["David", 28, "San Francisco", "Designer"]
    return df

def main():
    # Load the data
    data = load_data()
    update_data(data)
    os.makedirs("data", exist_ok=True)
    data.to_csv("data/people.csv", index=False)
    print("Initial Data:")
    print(data)


if __name__ == "__main__":
    main()