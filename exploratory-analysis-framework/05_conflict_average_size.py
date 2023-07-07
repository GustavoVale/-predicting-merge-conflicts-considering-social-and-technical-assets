# ['ms_id', 'pr_id', 'has_conflict', 'commit_merge_id', 'mc_hash', 'filepath',
# 'f_has_conflict', 'begin_line', 'end_line', 'c_has_conflict']

import pandas as pd

# Get matched merge scenarios from random sample:


def clean_df_chunk_names(df_conf_sample_name, df_safe_sample_name, df_chunk_names, column_sample_name='ms_id', column_files_name='ms_id'):
    df_conf_sample = pd.read_csv(df_conf_sample_name)
    df_safe_sample = pd.read_csv(df_safe_sample_name)
    # Merge sample merge scenarios
    df_sample = pd.concat([df_conf_sample, df_safe_sample])
    df_chunks = pd.read_csv(df_chunk_names)
    # It keeps the structure we got from the df_file_names
    df = df_chunks[df_chunks[column_files_name].isin(
        df_sample[column_sample_name])]
    return df


def get_unique_ms_map_with_chunk_masures(df, column_name='ms_id'):
    map = {}
    for i, row in df.iterrows():
        key = df[column_name][i]
        begin = df['begin_line'][i]
        end = df['end_line'][i]
        c_has_conflict = True if df['c_has_conflict'][i] == 1 else False
        diff_lines = 1 if end - begin < 1 else end - begin
        if key not in map:
            # columns: n_chunks, n_conf_chunks, loc_conf, loc_safe
            if c_has_conflict:
                map[key] = [1, 1, diff_lines, 0]
            else:
                map[key] = [1, 0, 0, diff_lines]
        else:
            if c_has_conflict:
                map[key] = [map[key][0] + 1, map[key][1] +
                            1, map[key][2] + diff_lines, map[key][3]]
            else:
                map[key] = [map[key][0] + 1, map[key][1],
                            map[key][2], map[key][3] + diff_lines]
    return map


def create_df_from_map(map):
    df = pd.DataFrame(columns=['ms_id', 'n_chunks', 'n_conf_chunks', 'loc_conf',
                      'loc_safe', 'avg_loc_chunks', 'avg_loc_conf_chunks', 'avg_loc_safe_chunks'])
    for key, value in map.items():
        n_chunks = value[0]
        n_conf_chunks = value[1]
        loc_conf = value[2]
        loc_safe = value[3]
        avg_loc_chunks = 0 if n_chunks <= 0 else (
            loc_conf + loc_safe) / n_chunks
        avg_loc_conf_chunks = 0 if n_conf_chunks <= 0 else (
            loc_conf) / n_conf_chunks
        avg_loc_safe_chunks = 0 if n_chunks - \
            n_conf_chunks <= 0 else loc_safe / (n_chunks - n_conf_chunks)
        df.loc[len(df.index)] = [key, n_chunks, n_conf_chunks, loc_conf, loc_safe,
                                 avg_loc_chunks, avg_loc_conf_chunks, avg_loc_safe_chunks]
    return df


def save_df_with_chunk_measures(df, path_to_save):
    map = get_unique_ms_map_with_chunk_masures(df)
    final_df = create_df_from_map(map)
    final_df.to_csv(path_to_save)

# HERE THE CALLS TO CREATED METHODS STARTS


# TODO: CHANGE THE SECOND ARGUMENT
df = clean_df_chunk_names('data/01_conflicting_ms_sample.csv',
                          'data/01_safe_ms_sample.csv',
                          'data/query_chunks.csv',
                          'ms_id',
                          'ms_id')

df_conflicting = df.loc[df['has_conflict'] == 1]
df_safe = df.loc[df['has_conflict'] == 0]

df_conflicting.describe().to_csv('data/05_conflict_statistics.csv')
df_safe.describe().to_csv('data/05_safe_statistics.csv')

save_df_with_chunk_measures(df, 'data/05_general_statistics.csv')
