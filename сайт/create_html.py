# -*- coding: utf-8 -*-

import pickle

with open('soc_places.pickle', 'rb') as f:
    parks = pickle.load(f)

with open('circles.pickle', 'rb') as f:
    circles = pickle.load(f)

s = ''
circles = circles + [(56.104557, 47.319695, 1, 'освещение')]

for i in circles:
    #print(i)
    s = s + """L.circle([""" + str(i[0]) + ", " + str(i[1]) +"""], """ +str(min(i[2] + 30, 200))+""" , {color: 'red', fillColor: '#f03', fillOpacity: 0.5}).addTo(mymap).bindPopup('""" + i[3] + """')\n"""

sp = ''
for i in parks:
    #print(i)
    sp = sp + """L.circle([""" + str(i[1]) + ", " + str(i[2]) +"""], 45 , {color: 'green', fillColor: 'green', fillOpacity: 0.5}).addTo(mymap).bindPopup('""" + str(i[0]) + """')\n"""

#s.encode('utf-8')


f = open('service.html', 'r', encoding="utf-8")
r = f.read()
f.close()

r = r.replace('//<<points>>', s)
r = r.replace('//<<parks>>', sp)

r = r.replace('qqobrgqq', '8553')

r = r.replace('qqobrbqq', str(len(circles)))

r = r.replace('qqparksqq', str(len(parks)))

f = open('service3.html', 'w', encoding="utf-8")
f.write(r)
f.close()
