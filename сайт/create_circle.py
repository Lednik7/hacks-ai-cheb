import pickle

with open('points2.pickle', 'rb') as f:
    points = pickle.load(f)


c1_min = 56.057504
c2_min = 47.079678
c1_max = 56.161492
c2_max = 47.475529

d1 = (c1_max - c1_min)/50
d2 = (c2_max-c2_min)/40

m = []
for i in range(100):
  m.append([])
  for j in range(80):
    m[-1].append([])

for i in points:
  if c1_min < i[1] < c1_max and c2_min < i[2] < c2_max:
    i1 = int((i[1] - c1_min) // d1)
    i2 = int((i[2] - c2_min) // d2)
    m[i1][i2].append(i)

circles = []

def mean_coord(ps):
  #print(ps)
  m1_c = []
  m2_c = []
  for i in ps:
    m1_c.append(i[1])
    m2_c.append(i[2])
  return (sum(m1_c) / len(m1_c), sum(m2_c) / len(m2_c))

def most_often(ps):
    m1 = []
    m2 = []
    for i in ps:
        if i[0] not in m1:
            m2.append(1)
            m1.append(i[0])
        else:
            m2[m1.index(i[0])] += 1
    return m1[m2.index(max(m2))]

for i in range(len(m)):
  for j in range(len(m[i])):
    if len(m[i][j]) != 0:
      if True:
        a = mean_coord(m[i][j])
        #print(a)
        circles.append((a[0], a[1], len(m[i][j]), most_often(m[i][j])))

with open('circles.pickle', 'wb') as f:
    pickle.dump(circles, f)

print(circles[1])
print(circles[2])
print(circles[3])
print(circles[4])
