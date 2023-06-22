from turtle import color, position, width
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

conflicting_ms_sample = pd.read_csv(r'data/01_conflicting_ms_sample.csv')
safe_ms_sample = pd.read_csv(r'data/01_safe_ms_sample.csv')

df = pd.concat([conflicting_ms_sample, safe_ms_sample])

ms_columns = ['top_proj', 'top_proj_target', 'top_proj_source', 'occ_proj', 'occ_proj_target', 'occ_proj_source', 'top_ms', 'top_ms_target', 'top_ms_source', 'occ_ms', 'occ_ms_target', 'occ_ms_source', 'devs', 'devs_target',
              'devs_source', 'devs_both', 'files', 'files_target', 'files_source', 'files_both', 'chunks', 'chunks_target', 'chunks_source', 'loc', 'loc_target', 'loc_source', 'commits', 'commits_target', 'commits_source', 'commits_source']


def generate_graph(num_rows, num_cols, ms_columns):
    fig, axs = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 15))
    counter = 0
    for i in range(num_rows):
        for j in range(num_cols):
            parts = axs[i, j].violinplot(
                dataset=[conflicting_ms_sample[ms_columns[counter]], safe_ms_sample[ms_columns[counter]]], showextrema=False)
            is_dark_color = True
            if i != num_rows - 1:
                axs[i, j].set_xticks(np.arange(1, 3), labels=[
                                     '', ''])
            else:
                axs[i, j].set_xticks(np.arange(1, 3), labels=[
                                     'conflicting', 'safe'])
            axs[i, j].set_title(ms_columns[counter])
            counter += 1
            # defining the style of a graph
            define_graph_style(parts, is_dark_color)

    fig.suptitle("Violin Plotting")
    fig.subplots_adjust(hspace=0.4)
    plt.savefig('figures/03-plots.png')
    plt.show()


def define_graph_style(parts, is_dark_color):
    for pc in parts['bodies']:
        pc.set_facecolor('white')

        # Strings are color names
        current_color = 'DarkSlateBlue' if is_dark_color else 'MediumSpringGreen'
        pc.set_edgecolors(current_color)
        is_dark_color = False
        pc.set_linewidths(2)
        pc.set_alpha(1)
        pc.convert_yunits(1)


generate_graph(6, 5, ms_columns)
