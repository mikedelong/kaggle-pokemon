import logging
import time

import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

start_time = time.time()
# set up logging
formatter = logging.Formatter('%(asctime)s : %(name)s :: %(levelname)s : %(message)s')
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
console_handler.setLevel(logging.DEBUG)
logger.debug('started')

data_path = './input/'
data = pd.read_csv(data_path + 'pokemon.csv')

logger.debug(data.info())

figsize = (16, 9)
figure, axes = plt.subplots(figsize=figsize)
heatmap = sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt='.1f', ax=axes)
plt.savefig('./pokemon_heatmap.png')
del figure
del axes

# Line Plot
# color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
figure, axes = plt.subplots(figsize=figsize)
data.Speed.plot(kind='line', color='g', label='Attack', linewidth=1, alpha=0.5, grid=True, linestyle=':')
data.Defense.plot(color='r', label='Defense', linewidth=1, alpha=0.5, grid=True, linestyle='-.')
plt.legend(loc='upper right')  # legend = puts label into plot
plt.xlabel('x axis')  # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')  # title = title of plot
plt.savefig('./pokemon_speed_defense_plot.png')
del figure
del axes

# Scatter Plot
# x = attack, y = defense
figure, axes = plt.subplots(figsize=figsize)
data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='red')
plt.xlabel('Attack')  # label = name of label
plt.ylabel('Defence')
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.title('Attack Defense Scatter Plot')  # title = title of plot
plt.savefig('./pokemon_attack_defense_scatter_plot.png')
del figure
del axes

# Histogram
# bins = number of bar in figure
figure, axes = plt.subplots(figsize=figsize)
data.Speed.plot(kind='hist', bins=100, figsize=figsize)
plt.savefig('./pokemon_speed_histogram.png')
del figure
del axes

# For example lets look frequency of pokemom types
logger.debug(data['Type 1'].value_counts(dropna=False))  # if there are nan values that also be counted

figure, axes = plt.subplots(figsize=figsize)
data.boxplot(column='Attack', by='Legendary')
plt.savefig('./pokemon_attack_boxplot.png')
del figure
del axes

figure, axes = plt.subplots(figsize=figsize)
data.loc[:, ["Attack", "Defense", "Speed"]].plot(subplots=True)
plt.savefig('./pokemon_subplots.png')
del figure
del axes

# histogram subplot with non cumulative and cumulative
figure, axes = plt.subplots(nrows=2, ncols=1)
data.loc[:, ["Attack", "Defense", "Speed"]].plot(kind="hist", y="Defense", bins=50, range=(0, 250), normed=True,
                                                 ax=axes[0])
data.loc[:, ["Attack", "Defense", "Speed"]].plot(kind="hist", y="Defense", bins=50, range=(0, 250), normed=True,
                                                 ax=axes[1], cumulative=True)
plt.savefig('./pokemon_histogram_subplots.png')
del figure
del axes

elapsed_time = time.time() - start_time
logger.debug('elapsed time %d seconds', elapsed_time)
