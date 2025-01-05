import pandas as pd
from ucimlrepo import fetch_ucirepo

from recommender_systems.config import DATA_RAW


def fetch_dataset(write: bool = True, verbose: bool = False) -> pd.DataFrame:
    """
    Fetch data from the UCI repository and save it to the data/raw folder.

    Parameters
    ----------
    write : bool, optional
        Whether to write the raw data, by default True
    verbose : bool, optional
        Whether to print info about the data (shape and first 5 rows), by default False

    Returns
    -------
    pd.DataFrame
        The fetched raw data
    """
    online_retail = fetch_ucirepo(id=352)
    data = online_retail.data.features

    if verbose:
        print(data.shape)
        print(data.head())

    if write:
        data.to_csv(DATA_RAW / "data.csv", index=False)

    return data


if __name__ == "__main__":
    fetch_dataset(write=True, verbose=True)
