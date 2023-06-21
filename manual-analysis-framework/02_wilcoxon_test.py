import pandas as pd
import scipy.stats as stats

conflicting_ms_sample = pd.read_csv(r'data/01_conflicting_ms_sample.csv')

safe_ms_sample = pd.read_csv(r'data/01_safe_ms_sample.csv')

ms_columns = ['top_proj', 'top_proj_target', 'top_proj_source', 'occ_proj', 'occ_proj_target', 'occ_proj_source', 'top_ms', 'top_ms_target', 'top_ms_source', 'occ_ms', 'occ_ms_target', 'occ_ms_source', 'devs', 'devs_target',
              'devs_source', 'devs_both', 'files', 'files_target', 'files_source', 'files_both', 'chunks', 'chunks_target', 'chunks_source', 'loc', 'loc_target', 'loc_source', 'commits', 'commits_target',	'commits_source']

df = pd.DataFrame(columns=['measure', 'statistic', 'pvalue'])

for col in ms_columns:
    result = stats.wilcoxon(conflicting_ms_sample[col], safe_ms_sample[col])
    df.loc[len(df.index)] = [col, result[0], result[1]]

df.to_csv('02_wilcoxon_test.csv')
