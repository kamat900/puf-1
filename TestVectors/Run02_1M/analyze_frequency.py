results = [line.rstrip('\n') for line in open('results02_0.dat')]
results_bin = []

for i in range(0, len(results)):
  results_bin.append(bin(int(results[i], 16))[2:].zfill(32))

count_zeros = 0
count_ones = 0

for i in range(0, len(results_bin)):
  count_zeros += results_bin[i].count('0')
  count_ones += results_bin[i].count('1')

count_total = count_zeros+count_ones
zero_percent = float(count_zeros)/count_total
one_percent = float(count_ones)/count_total

print("The total numbers counted: " + str(count_total) + "\n")
print("The total number of 0: " + str(count_zeros) + "\n")
print("The percent of 0: " + str(zero_percent) + "\n")
print("The total number of 1: " + str(count_ones) + "\n")
print("The percent of 1: " + str(one_percent) + "\n")
