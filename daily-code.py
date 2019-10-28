# For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].

a = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
new = []
for i in a:
  for k in i:
    if k not in new:
      new.append(k)
l = len(new)
result = []
k = 0
while k < l:
  min = new[0]
  for i in new:
    if i < min:
      min = i
  k += 1
  result.append(min)
  new.remove(min)
print(result)

