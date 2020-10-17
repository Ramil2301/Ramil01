from collections import Counter

a = [[1, 2, 3, 5, 4],
     [1, 2, 2, 5, 4],
     [1, 5, 5, 5, 4],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 0, 0]]
maxs = [Counter(x).most_common(1)[0][1] for x in a]
print(maxs.index(max(maxs)) + 1)