from configparser import ConfigParser

import pandas as pd


def ini_to_df(ini_path):
    cp = ConfigParser()
    cp.read(ini_path)
    rows = []
    for section in cp.sections():
        row = {k: v for k, v in cp.items(section)}
        rows.append(row)
    df = pd.DataFrame(rows)
    return df
