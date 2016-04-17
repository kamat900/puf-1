from random import randint

fp = open("test_vectors.dat", "w")

for i in range(0, 10000):
  x0 = randint(0, 2147483647)
  x1 = randint(0, 2147483647)
  x2 = randint(0, 2147483647)
  x3 = randint(0, 2147483647)
  fp.write(str(x0)+","+str(x1)+","+str(x2)+","+str(x3)+"\n")

fp.close()