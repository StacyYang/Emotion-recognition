import pandas as pd
import re
import os
import glob
from pathlib import Path


# Concatenate csv files of the five sessions
csv_files_path = os.path.join("./", "*.csv")
csv_files = glob.glob(csv_files_path)
iemocap_features = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)
iemocap_features.to_csv('iemocap_features.csv')

print(iemocap_features['label'].value_counts())