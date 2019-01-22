import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = .2
korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width, alpha=.4, label='Корея')
c1 = plt.bar(index + 0.2, canada_scores, bar_width, alpha=.4, label='Канада')
ch1 = plt.bar(index + 0.4, china_scores, bar_width, alpha=.4, label='Китай')
f1 = plt.bar(index + 0.6, france_scores, bar_width, alpha=.4, label='Франция')


def CreateLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width()/2., height*1.05,'%d' % int(height),
                 ha='center', va='bottom')


CreateLabels(k1)
CreateLabels(c1)
CreateLabels(ch1)
CreateLabels(f1)
plt.ylabel("PISA2012 РЕЗУЛЬТАТ")
plt.xlabel("ПРЕДМЕТЫ")
plt.xticks(index+.3/2, ("МАТЕМАТИКА", "ЛИТЕРАТУРА", "НАУКА"))
plt.legend(edgecolor=None, shadow=None, loc=2, bbox_to_anchor=(1, 1))
plt.grid(True)

integer = 365


plt.show()


