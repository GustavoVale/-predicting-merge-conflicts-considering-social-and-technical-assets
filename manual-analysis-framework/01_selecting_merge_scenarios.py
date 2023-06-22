import pandas as pd

df = pd.read_csv(r'../raw-input-data/ms-data.csv')

# Save sample of dataframe in csv with or without conflicts


def save_sample_df(df, sample_size, is_conflicting, filepath):
    new_df = df.loc[df['has_conflict'] == is_conflicting]
    new_df = new_df.sample(n=sample_size)
    new_df.to_csv(filepath)


# For conflicting scenarios
conflicting_ms_sample = save_sample_df(
    df, 200, 1, 'data/01_conflicting_ms_sample.csv')

# For safe scenarios
conflicting_ms_sample = save_sample_df(
    df, 200, 0, 'data/01_safe_ms_sample.csv')
