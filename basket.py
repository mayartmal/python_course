
objects = [1, 2, 1, 2, 7, 7, 3]
i = 0
ids = []
for obj in objects:
    ids.append(id(obj))
print(ids)
s = set(ids)
ans = s.__len__()
print(ans)

