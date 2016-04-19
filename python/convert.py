fp = open("results_binary.dat", "w")

results = [line.rstrip('\n') for line in open('results.dat')]

results_bin = []

for i in range(0, len(results)):
  results_bin.append(bin(int(results[i], 16))[2:].zfill(32))

for i in range(0, len(results_bin)):
  fp.write(results_bin[i] + "\n")

fp.close()
