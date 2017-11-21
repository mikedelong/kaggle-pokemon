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
heatmap = sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=axes)
plt.savefig('./pokemon_heatmap.png')
del figure

# Line Plot
# color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
figure, axes = plt.subplots(figsize=figsize)
data.Speed.plot(kind = 'line', color = 'g',label = 'Attack',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
data.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot
plt.savefig('./pokemon_speed_defense_plot.png')

logger.debug('done')
elapsed_time = time.time() - start_time
logger.debug('elapsed time %d seconds', elapsed_time)
