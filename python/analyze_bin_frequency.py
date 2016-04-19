results = [line.rstrip('\n') for line in open('results02_0.dat')]
results_bin = []
results_byte = []
#fp = open("results_binned.dat", "w")

for i in range(0, len(results)):
  results_bin.append(bin(int(results[i], 16))[2:].zfill(32))

for i in range(0, len(results_bin)):
  results_byte.append(results_bin[i][0:4])
  results_byte.append(results_bin[i][4:8])
  results_byte.append(results_bin[i][8:12])
  results_byte.append(results_bin[i][12:16])
  results_byte.append(results_bin[i][16:20])
  results_byte.append(results_bin[i][20:24])
  results_byte.append(results_bin[i][24:28])
  results_byte.append(results_bin[i][28:32])

pattern0 = 0 #0000
pattern1 = 0 #0001
pattern2 = 0 #0010
pattern3 = 0 #0011
pattern4 = 0 #0100
pattern5 = 0 #0101
pattern6 = 0 #0110
pattern7 = 0 #0111
pattern8 = 0 #1000
pattern9 = 0 #1001
patternA = 0 #1010
patternB = 0 #1011
patternC = 0 #1100
patternD = 0 #1101
patternE = 0 #1110
patternF = 0 #1111

for i in range(0, len(results_byte)):
  pattern0 += results_byte[i].count('0000')
  pattern1 += results_byte[i].count('0001')
  pattern2 += results_byte[i].count('0010')
  pattern3 += results_byte[i].count('0011')
  pattern4 += results_byte[i].count('0100')
  pattern5 += results_byte[i].count('0101')
  pattern6 += results_byte[i].count('0110')
  pattern7 += results_byte[i].count('0111')
  pattern8 += results_byte[i].count('1000')
  pattern9 += results_byte[i].count('1001')
  patternA += results_byte[i].count('1010')
  patternB += results_byte[i].count('1011')
  patternC += results_byte[i].count('1100')
  patternD += results_byte[i].count('1101')
  patternE += results_byte[i].count('1110')
  patternF += results_byte[i].count('1111')

count_total = pattern0 + pattern1 + pattern2 + pattern3 + pattern4 + pattern5 + pattern6 + pattern7 + pattern8 + pattern9 + patternA + patternB + patternC + patternD + patternE + patternF

p0p = float(pattern0)/count_total
p1p = float(pattern1)/count_total
p2p = float(pattern2)/count_total
p3p = float(pattern3)/count_total
p4p = float(pattern4)/count_total
p5p = float(pattern5)/count_total
p6p = float(pattern6)/count_total
p7p = float(pattern7)/count_total
p8p = float(pattern8)/count_total
p9p = float(pattern9)/count_total
pAp = float(patternA)/count_total
pBp = float(patternB)/count_total
pCp = float(patternC)/count_total
pDp = float(patternD)/count_total
pEp = float(patternE)/count_total
pFp = float(patternF)/count_total

print("The total count is: " + str(count_total) + "\n")
print("The pattern 0 (0000) count is: " + str(pattern0) + "\n")
print("The pattern 0 percent is: " + str(p0p) + "\n")
print("The pattern 1 (0001) count is: " + str(pattern1) + "\n")
print("The pattern 1 percent is: " + str(p1p) + "\n")
print("The pattern 2 (0010) count is: " + str(pattern2) + "\n")
print("The pattern 2 percent is: " + str(p2p) + "\n")
print("The pattern 3 (0011) count is: " + str(pattern3) + "\n")
print("The pattern 3 percent is: " + str(p3p) + "\n")
print("The pattern 4 (0100) count is: " + str(pattern4) + "\n")
print("The pattern 4 percent is: " + str(p4p) + "\n")
print("The pattern 5 (0101) count is: " + str(pattern5) + "\n")
print("The pattern 5 percent is: " + str(p5p) + "\n")
print("The pattern 6 (0110) count is: " + str(pattern6) + "\n")
print("The pattern 6 percent is: " + str(p6p) + "\n")
print("The pattern 7 (0111) count is: " + str(pattern7) + "\n")
print("The pattern 7 percent is: " + str(p7p) + "\n")
print("The pattern 8 (1000) count is: " + str(pattern8) + "\n")
print("The pattern 8 percent is: " + str(p8p) + "\n")
print("The pattern 9 (1001) count is: " + str(pattern9) + "\n")
print("The pattern 9 percent is: " + str(p9p) + "\n")
print("The pattern A (1010) count is: " + str(patternA) + "\n")
print("The pattern A percent is: " + str(pAp) + "\n")
print("The pattern B (1011) count is: " + str(patternB) + "\n")
print("The pattern B percent is: " + str(pBp) + "\n")
print("The pattern C (1100) count is: " + str(patternC) + "\n")
print("The pattern C percent is: " + str(pCp) + "\n")
print("The pattern D (1101) count is: " + str(patternD) + "\n")
print("The pattern D percent is: " + str(pDp) + "\n")
print("The pattern E (1110) count is: " + str(patternE) + "\n")
print("The pattern E percent is: " + str(pEp) + "\n")
print("The pattern F (1111) count is: " + str(patternF) + "\n")
print("The pattern F percent is: " + str(pFp) + "\n")
