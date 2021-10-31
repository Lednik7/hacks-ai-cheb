import pickle

with open('points.pickle', 'rb') as f:
    points = pickle.load(f)

s = ''

print(points[0][0])

for i in points[:100]:
    s = s + f"""L.marker([{i[1]}, {i[2]}]).addTo(mymap).bindPopup("something").openPopup();\n"""

#s.encode('utf-8')


f = open('service.html', 'r')
r = f.read()
f.close()

r = r.replace('<<points>>', s)

f = open('service2.html', 'w')
f.write(r)
f.close()