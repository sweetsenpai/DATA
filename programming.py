import matplotlib.pyplot as plt

labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
size = [33, 55, 20, 17, 62, 49]
separated = (.1, 0.3, 0, 0.2, 0.35, 0.45)
plt.pie(size, labels=labels,autopct='%1.1f%%',explode=separated)
plt.axis('equal')
plt.show()
