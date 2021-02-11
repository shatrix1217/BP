import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load seaborn built-in dataset
crash_df = sns.load_dataset('car_crashes')
tips_df = sns.load_dataset('tips')

#Distribution plot
sns.displot(crash_df['not_distracted'])

#Joint plot
sns.jointplot(x = 'speeding', y = 'alcohol', data = crash_df, kind = 'kde')

#Pair plot
sns.pairplot(tips_df, hue = 'sex', palette = 'Blues')

#Pair grid
iris = sns.load_dataset('iris')
iris_g = sns.PairGrid(iris, hue = 'species')
iris_g.map(plt.scatter)

#Rug plot
sns.rugplot(tips_df['tip'])

#Styling
sns.set_style('ticks')
sns.set_context('paper', font_scale = 1.5)
plt.figure(figsize = (8, 4))
sns.jointplot(x = 'speeding', y = 'alcohol', data = crash_df, kind = 'reg')
sns.despine(left = True)

#Bar plot
sns.barplot(x = 'sex', y = 'total_bill', data = tips_df)

#Box plot
sns.boxplot(x = 'day', y = 'total_bill', data = tips_df, hue = 'sex')
plt.legend(loc = 0)

#violin plot
sns.violinplot(x = 'day', y = 'total_bill', data = tips_df, hue = 'sex')

#Swarm plot
sns.swarmplot(x = 'day', y = 'total_bill', data = tips_df, hue = 'sex')

#heatmaps, need to turn columns to index.
plt.figure(figsize = (8, 6))
sns.set_context('paper', font_scale = 1.4)

crash_mx = crash_df.corr()
sns.heatmap(crash_mx, annot=True, cmap='Blues')

#heatmaps, using another dataset
flights = sns.load_dataset('flights')
flights = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(flights, cmap='Blues')

#facet grid
tips_fg = sns.FacetGrid(tip_df, col = 'time', row = 'smoker')
tips_fg.map(plt.hist, 'total_bill', bins = 8)