import itertools
import matplotlib.pyplot as plt

def hamming2(s1, s2):
  assert len(s1) == len(s2)
  return sum(c1 != c2 for c1, c2 in zip(s1, s2))

results = [line.rstrip('\n') for line in open('results.dat')]
results_bin = []
hamming_dist = []

for i in range(0, len(results)):
  results_bin.append(bin(int(results[i], 16))[2:].zfill(32))

for i in itertools.combinations(results_bin, 2):
  hamming_dist.append(hamming2(i[0], i[1]))

plt.hist(hamming_dist, bins=8, color='blue')
plt.savefig("hist.png")
plt.show()