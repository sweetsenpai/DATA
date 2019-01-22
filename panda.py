import pandas as pd
import matplotlib.pyplot as plt

raw_data = {'names': ['Sasha', 'Panda', 'Nick', 'PPD', 'FNG'],
            'jan_ir': [100, 148, 813, 713, 645],
            'feb_ir': [373, 564, 334, 136, 859],
            'march':  [122, 464, 226, 165, 531]}

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'march'])
df['total ir'] = df['jan_ir'] + df['feb_ir'] + df['march']
print(df)

color = [(1, .4, .4), (1, .6, .1), (.5, .3, 1), (.3, .1, .5), (1, .2, .5)]
plt.pie(df['total ir'],
        labels=df['names'],
        colors=color,
        autopct='%1.1f%%')
plt.axis = 'equal'
plt.show()
