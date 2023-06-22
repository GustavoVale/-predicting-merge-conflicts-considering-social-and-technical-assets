# ['ms_id', 'pr_id', 'has_conflict', 'commit_merge_id', 'mc_hash', 'filepath',
# 'f_has_conflict', 'begin_line', 'end_line', 'c_has_conflict']

import pandas as pd

# Get matched merge scenarios from random sample:


def clean_df_file_names(df_sample_name, df_file_names, column_sample_name='ms_id', column_files_name='ms_id'):
    df_sample = pd.read_csv(df_sample_name)
    df_files = pd.read_csv(df_file_names)
    # It keeps the structure we got from the df_file_names
    df = df_files[df_files[column_files_name].isin(
        df_sample[column_sample_name])]
    return df


def get_unique_ms_map_with_chunk_masures(df, column_name='ms_id'):
    map = {}
    for i in range(0, len(df[column_name])):
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
        avg_loc_chunks = (value[2] + value[3]) / value[0]
        avg_loc_conf_chunks = (value[2]) / value[1]
        avg_loc_safe_chunks = value[3] / (value[0] - value[1])
        df.loc[len(df.index)] = [key, value[0], value[1], value[2], value[3],
                                 avg_loc_chunks, avg_loc_conf_chunks, avg_loc_safe_chunks]
    return df


def save_df_with_chunk_measures(df, path_to_save):
    map = get_unique_ms_map_with_chunk_masures(df)
    final_df = create_df_from_map(map)
    final_df.to_csv(path_to_save)


df = clean_df_file_names('data/01_conflicting_ms_sample.csv',
                         'data/01_conflicting_ms_sample.csv',
                         'ms_id',
                         'ms_id')

df_conflicting = df.loc[df['has_conflict'] == 1]
df_safe = df.loc[df['has_conflict'] == 0]

df_conflicting.describe().to_csv('data/05_conflict_statistics.csv')
df_safe.describe().to_csv('data/05_safe_statistics.csv')

save_df_with_chunk_measures(df, 'data/05_general_statistics.csv')
