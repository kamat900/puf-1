import itertools
import matplotlib.pyplot as plt

def hamming2(s1, s2):
  assert len(s1) == len(s2)
  return sum(c1 != c2 for c1, c2 in zip(s1, s2))

results0 = [line.rstrip('\n') for line in open('results01_0.dat')]
results1 = [line.rstrip('\n') for line in open('results01_1.dat')]
results2 = [line.rstrip('\n') for line in open('results01_2.dat')]
results3 = [line.rstrip('\n') for line in open('results01_3.dat')]
results4 = [line.rstrip('\n') for line in open('results01_4.dat')]
results5 = [line.rstrip('\n') for line in open('results01_5.dat')]
results6 = [line.rstrip('\n') for line in open('results01_6.dat')]
results7 = [line.rstrip('\n') for line in open('results01_7.dat')]
results8 = [line.rstrip('\n') for line in open('results01_8.dat')]
results9 = [line.rstrip('\n') for line in open('results01_9.dat')]
results_bin0 = []
results_bin1 = []
results_bin2 = []
results_bin3 = []
results_bin4 = []
results_bin5 = []
results_bin6 = []
results_bin7 = []
results_bin8 = []
results_bin9 = []
temp_results = []
hamming_dist = []

for i in range(0, len(results0)):
  results_bin0.append(bin(int(results0[i], 16))[2:].zfill(32))

for i in range(0, len(results1)):
  results_bin1.append(bin(int(results1[i], 16))[2:].zfill(32))

for i in range(0, len(results2)):
  results_bin2.append(bin(int(results2[i], 16))[2:].zfill(32))

for i in range(0, len(results3)):
  results_bin3.append(bin(int(results3[i], 16))[2:].zfill(32))

for i in range(0, len(results4)):
  results_bin4.append(bin(int(results4[i], 16))[2:].zfill(32))

for i in range(0, len(results5)):
  results_bin5.append(bin(int(results5[i], 16))[2:].zfill(32))

for i in range(0, len(results6)):
  results_bin6.append(bin(int(results6[i], 16))[2:].zfill(32))

for i in range(0, len(results7)):
  results_bin7.append(bin(int(results7[i], 16))[2:].zfill(32))

for i in range(0, len(results8)):
  results_bin8.append(bin(int(results8[i], 16))[2:].zfill(32))

for i in range(0, len(results9)):
  results_bin9.append(bin(int(results9[i], 16))[2:].zfill(32))

for i in range(0, len(results0)):
  temp_results.append(results_bin0[i])
  temp_results.append(results_bin1[i])
  temp_results.append(results_bin2[i])
  temp_results.append(results_bin3[i])
  temp_results.append(results_bin4[i])
  temp_results.append(results_bin5[i])
  temp_results.append(results_bin6[i])
  temp_results.append(results_bin7[i])
  temp_results.append(results_bin8[i])
  temp_results.append(results_bin9[i])
  for j in itertools.combinations(temp_results, 2):
    hamming_dist.append(hamming2(j[0], j[1]))
  temp_results = []

print(hamming_dist.count(0))
print(hamming_dist.count(1))
print(hamming_dist.count(2))
#plt.hist(hamming_dist, bins=8, color='blue')
#plt.savefig("histXX_8bins.png")
#plt.hist(hamming_dist, bins=16, color='blue')
#plt.savefig("histXX_16bins.png")
plt.hist(hamming_dist, bins=32, color='blue')
plt.savefig("histXX_32bins.png")
plt.show()
