import pandas as pd

# Get matched merge scenarios from random sample:


def clean_df_file_names(df_conf_sample_name, df_safe_sample_name, df_file_names, column_sample_name='ms_id',
                        column_files_name='ms_id'):
    df_conf_sample = pd.read_csv(df_conf_sample_name)
    df_safe_sample = pd.read_csv(df_safe_sample_name)
    # Merge sample merge scenarios
    df_sample = pd.concat([df_conf_sample, df_safe_sample])
    df_files = pd.read_csv(df_file_names)
    # It keeps the structure we got from the df_file_names
    df = df_files[df_files[column_files_name].isin(
        df_sample[column_sample_name])]
    return df

# Get a map of files and the number of occurrences in the merge scenarios from the dataframe


def get_unique_files_map_with_occurrence(df, column_name='filepath'):
    map = {}
    for i, row in df.iterrows():
        key = df[column_name][i]
        has_conflict = df['f_has_conflict'][i]
        # measures: occurrences and occurences with conflict
        if key not in map:
            map[key] = [1, has_conflict]
        else:
            map[key] = [map[key][0] + 1, map[key][1] + has_conflict]
    return map

# Create a dataframe from a map


def create_df_from_map(map):
    df = pd.DataFrame(columns=['file', 'occ', 'occ_conflicts', 'avg_conflicts'])
    for key, value in map.items():
        df.loc[len(df.index)] = [key, value[0], value[1], value[1]/value[0]]
    return df

# Save a csv file with a list of unique files and the number of merge scenarios and conflicting merge scenarios


def save_df_with_unique_files_occurrence(df_conf_sample, df_safe_sample, df_file, path_to_save,
                                         col_sample='ms_id', col_files='ms_id', target_col='filepath'):
    df = clean_df_file_names(df_conf_sample, df_safe_sample,
                             df_file, col_sample, col_files)
    map_unique_files = get_unique_files_map_with_occurrence(
        df, target_col)
    final_df = create_df_from_map(map_unique_files)
    final_df.to_csv(path_to_save)


# Call created methods and save into a csv file
# TODO: Change the second filepath to the real one when we have it AND cross-check the column names
save_df_with_unique_files_occurrence('data/01_conflicting_ms_sample.csv',
                                     'data/01_safe_ms_sample.csv',
                                     'data/query_files.csv',
                                     'data/04_file_occ_and_occ_conf.csv',
                                     'ms_id',
                                     'ms_id',
                                     'filepath')
