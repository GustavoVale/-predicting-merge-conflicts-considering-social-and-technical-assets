import pandas as pd

df = pd.read_csv(r'../raw-input-data/ms-data.csv')

# Getting sample for conflicting scenarios
conflicting_ms = df.loc[df['has_conflict'] == 1];
conflicting_ms_sample =conflicting_ms.sample(n = 200)
conflicting_ms_sample.to_csv('data/01_conflicting_ms_sample.csv')

# Getting sample for safe scenarios
safe_ms = df.loc[df['has_conflict'] == 0];
safe_ms_sample = safe_ms.sample(n = 200)
safe_ms_sample.to_csv('data/01_safe_ms_sample.csv')


