import os

f = open("city.txt", "r")
d = ""


for x in f:
  d += x.lower();

d = d.split("\n");
d = sorted(d);
d = "\n".join(d);
print(d)

with open("city.txt", 'w') as file:
	file.write(d)