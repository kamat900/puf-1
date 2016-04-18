import itertools
import matplotlib.pyplot as plt

def hamming2(s1, s2):
  assert len(s1) == len(s2)
  return sum(c1 != c2 for c1, c2 in zip(s1, s2))

results0 = [line.rstrip('\n') for line in open('results03_0.dat')]
results1 = [line.rstrip('\n') for line in open('results03_1.dat')]
results2 = [line.rstrip('\n') for line in open('results03_2.dat')]
results3 = [line.rstrip('\n') for line in open('results03_3.dat')]
results4 = [line.rstrip('\n') for line in open('results03_4.dat')]
results5 = [line.rstrip('\n') for line in open('results03_5.dat')]
results6 = [line.rstrip('\n') for line in open('results03_6.dat')]
results7 = [line.rstrip('\n') for line in open('results03_7.dat')]
results8 = [line.rstrip('\n') for line in open('results03_8.dat')]
results9 = [line.rstrip('\n') for line in open('results03_9.dat')]
results10 = [line.rstrip('\n') for line in open('results03_10.dat')]
results11 = [line.rstrip('\n') for line in open('results03_11.dat')]
results12 = [line.rstrip('\n') for line in open('results03_12.dat')]
results13 = [line.rstrip('\n') for line in open('results03_13.dat')]
results14 = [line.rstrip('\n') for line in open('results03_14.dat')]
results15 = [line.rstrip('\n') for line in open('results03_15.dat')]
results16 = [line.rstrip('\n') for line in open('results03_16.dat')]
results17 = [line.rstrip('\n') for line in open('results03_17.dat')]
results18 = [line.rstrip('\n') for line in open('results03_18.dat')]
results19 = [line.rstrip('\n') for line in open('results03_19.dat')]
results20 = [line.rstrip('\n') for line in open('results03_20.dat')]
results21 = [line.rstrip('\n') for line in open('results03_21.dat')]
results22 = [line.rstrip('\n') for line in open('results03_22.dat')]
results23 = [line.rstrip('\n') for line in open('results03_23.dat')]
results24 = [line.rstrip('\n') for line in open('results03_24.dat')]
results25 = [line.rstrip('\n') for line in open('results03_25.dat')]
results26 = [line.rstrip('\n') for line in open('results03_26.dat')]
results27 = [line.rstrip('\n') for line in open('results03_27.dat')]
results28 = [line.rstrip('\n') for line in open('results03_28.dat')]
results29 = [line.rstrip('\n') for line in open('results03_29.dat')]
results30 = [line.rstrip('\n') for line in open('results03_30.dat')]
results31 = [line.rstrip('\n') for line in open('results03_31.dat')]
results32 = [line.rstrip('\n') for line in open('results03_32.dat')]
results33 = [line.rstrip('\n') for line in open('results03_33.dat')]
results34 = [line.rstrip('\n') for line in open('results03_34.dat')]
results35 = [line.rstrip('\n') for line in open('results03_35.dat')]
results36 = [line.rstrip('\n') for line in open('results03_36.dat')]
results37 = [line.rstrip('\n') for line in open('results03_37.dat')]
results38 = [line.rstrip('\n') for line in open('results03_38.dat')]
results39 = [line.rstrip('\n') for line in open('results03_39.dat')]
results40 = [line.rstrip('\n') for line in open('results03_40.dat')]
results41 = [line.rstrip('\n') for line in open('results03_41.dat')]
results42 = [line.rstrip('\n') for line in open('results03_42.dat')]
results43 = [line.rstrip('\n') for line in open('results03_43.dat')]
results44 = [line.rstrip('\n') for line in open('results03_44.dat')]
results45 = [line.rstrip('\n') for line in open('results03_45.dat')]
results46 = [line.rstrip('\n') for line in open('results03_46.dat')]
results47 = [line.rstrip('\n') for line in open('results03_47.dat')]
results48 = [line.rstrip('\n') for line in open('results03_48.dat')]
results49 = [line.rstrip('\n') for line in open('results03_49.dat')]
results50 = [line.rstrip('\n') for line in open('results03_50.dat')]
results51 = [line.rstrip('\n') for line in open('results03_51.dat')]
results52 = [line.rstrip('\n') for line in open('results03_52.dat')]
results53 = [line.rstrip('\n') for line in open('results03_53.dat')]
results54 = [line.rstrip('\n') for line in open('results03_54.dat')]
results55 = [line.rstrip('\n') for line in open('results03_55.dat')]
results56 = [line.rstrip('\n') for line in open('results03_56.dat')]
results57 = [line.rstrip('\n') for line in open('results03_57.dat')]
results58 = [line.rstrip('\n') for line in open('results03_58.dat')]
results59 = [line.rstrip('\n') for line in open('results03_59.dat')]
results60 = [line.rstrip('\n') for line in open('results03_60.dat')]
results61 = [line.rstrip('\n') for line in open('results03_61.dat')]
results62 = [line.rstrip('\n') for line in open('results03_62.dat')]
results63 = [line.rstrip('\n') for line in open('results03_63.dat')]
results64 = [line.rstrip('\n') for line in open('results03_64.dat')]
results65 = [line.rstrip('\n') for line in open('results03_65.dat')]
results66 = [line.rstrip('\n') for line in open('results03_66.dat')]
results67 = [line.rstrip('\n') for line in open('results03_67.dat')]
results68 = [line.rstrip('\n') for line in open('results03_68.dat')]
results69 = [line.rstrip('\n') for line in open('results03_69.dat')]
results70 = [line.rstrip('\n') for line in open('results03_70.dat')]
results71 = [line.rstrip('\n') for line in open('results03_71.dat')]
results72 = [line.rstrip('\n') for line in open('results03_72.dat')]
results73 = [line.rstrip('\n') for line in open('results03_73.dat')]
results74 = [line.rstrip('\n') for line in open('results03_74.dat')]
results75 = [line.rstrip('\n') for line in open('results03_75.dat')]
results76 = [line.rstrip('\n') for line in open('results03_76.dat')]
results77 = [line.rstrip('\n') for line in open('results03_77.dat')]
results78 = [line.rstrip('\n') for line in open('results03_78.dat')]
results79 = [line.rstrip('\n') for line in open('results03_79.dat')]
results80 = [line.rstrip('\n') for line in open('results03_80.dat')]
results81 = [line.rstrip('\n') for line in open('results03_81.dat')]
results82 = [line.rstrip('\n') for line in open('results03_82.dat')]
results83 = [line.rstrip('\n') for line in open('results03_83.dat')]
results84 = [line.rstrip('\n') for line in open('results03_84.dat')]
results85 = [line.rstrip('\n') for line in open('results03_85.dat')]
results86 = [line.rstrip('\n') for line in open('results03_86.dat')]
results87 = [line.rstrip('\n') for line in open('results03_87.dat')]
results88 = [line.rstrip('\n') for line in open('results03_88.dat')]
results89 = [line.rstrip('\n') for line in open('results03_89.dat')]
results90 = [line.rstrip('\n') for line in open('results03_90.dat')]
results91 = [line.rstrip('\n') for line in open('results03_91.dat')]
results92 = [line.rstrip('\n') for line in open('results03_92.dat')]
results93 = [line.rstrip('\n') for line in open('results03_93.dat')]
results94 = [line.rstrip('\n') for line in open('results03_94.dat')]
results95 = [line.rstrip('\n') for line in open('results03_95.dat')]
results96 = [line.rstrip('\n') for line in open('results03_96.dat')]
results97 = [line.rstrip('\n') for line in open('results03_97.dat')]
results98 = [line.rstrip('\n') for line in open('results03_98.dat')]
results99 = [line.rstrip('\n') for line in open('results03_99.dat')]
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
results_bin10 = []
results_bin11 = []
results_bin12 = []
results_bin13 = []
results_bin14 = []
results_bin15 = []
results_bin16 = []
results_bin17 = []
results_bin18 = []
results_bin19 = []
results_bin20 = []
results_bin21 = []
results_bin22 = []
results_bin23 = []
results_bin24 = []
results_bin25 = []
results_bin26 = []
results_bin27 = []
results_bin28 = []
results_bin29 = []
results_bin30 = []
results_bin31 = []
results_bin32 = []
results_bin33 = []
results_bin34 = []
results_bin35 = []
results_bin36 = []
results_bin37 = []
results_bin38 = []
results_bin39 = []
results_bin30 = []
results_bin31 = []
results_bin32 = []
results_bin33 = []
results_bin34 = []
results_bin35 = []
results_bin36 = []
results_bin37 = []
results_bin38 = []
results_bin39 = []
results_bin40 = []
results_bin41 = []
results_bin42 = []
results_bin43 = []
results_bin44 = []
results_bin45 = []
results_bin46 = []
results_bin47 = []
results_bin48 = []
results_bin49 = []
results_bin50 = []
results_bin51 = []
results_bin52 = []
results_bin53 = []
results_bin54 = []
results_bin55 = []
results_bin56 = []
results_bin57 = []
results_bin58 = []
results_bin59 = []
results_bin60 = []
results_bin61 = []
results_bin62 = []
results_bin63 = []
results_bin64 = []
results_bin65 = []
results_bin66 = []
results_bin67 = []
results_bin68 = []
results_bin69 = []
results_bin70 = []
results_bin71 = []
results_bin72 = []
results_bin73 = []
results_bin74 = []
results_bin75 = []
results_bin76 = []
results_bin77 = []
results_bin78 = []
results_bin79 = []
results_bin80 = []
results_bin81 = []
results_bin82 = []
results_bin83 = []
results_bin84 = []
results_bin85 = []
results_bin86 = []
results_bin87 = []
results_bin88 = []
results_bin89 = []
results_bin90 = []
results_bin91 = []
results_bin92 = []
results_bin93 = []
results_bin94 = []
results_bin95 = []
results_bin96 = []
results_bin97 = []
results_bin98 = []
results_bin99 = []
temp_results = []
hamming_dist = []

for i in range(0, len(results0)):
  results_bin0.append(bin(int(results0[i], 16))[2:].zfill(32))
  results_bin1.append(bin(int(results1[i], 16))[2:].zfill(32))
  results_bin2.append(bin(int(results2[i], 16))[2:].zfill(32))
  results_bin3.append(bin(int(results3[i], 16))[2:].zfill(32))
  results_bin4.append(bin(int(results4[i], 16))[2:].zfill(32))
  results_bin5.append(bin(int(results5[i], 16))[2:].zfill(32))
  results_bin6.append(bin(int(results6[i], 16))[2:].zfill(32))
  results_bin7.append(bin(int(results7[i], 16))[2:].zfill(32))
  results_bin8.append(bin(int(results8[i], 16))[2:].zfill(32))
  results_bin9.append(bin(int(results9[i], 16))[2:].zfill(32))
  results_bin10.append(bin(int(results10[i], 16))[2:].zfill(32))
  results_bin11.append(bin(int(results11[i], 16))[2:].zfill(32))
  results_bin12.append(bin(int(results12[i], 16))[2:].zfill(32))
  results_bin13.append(bin(int(results13[i], 16))[2:].zfill(32))
  results_bin14.append(bin(int(results14[i], 16))[2:].zfill(32))
  results_bin15.append(bin(int(results15[i], 16))[2:].zfill(32))
  results_bin16.append(bin(int(results16[i], 16))[2:].zfill(32))
  results_bin17.append(bin(int(results17[i], 16))[2:].zfill(32))
  results_bin18.append(bin(int(results18[i], 16))[2:].zfill(32))
  results_bin19.append(bin(int(results19[i], 16))[2:].zfill(32))
  results_bin20.append(bin(int(results20[i], 16))[2:].zfill(32))
  results_bin21.append(bin(int(results21[i], 16))[2:].zfill(32))
  results_bin22.append(bin(int(results22[i], 16))[2:].zfill(32))
  results_bin23.append(bin(int(results23[i], 16))[2:].zfill(32))
  results_bin24.append(bin(int(results24[i], 16))[2:].zfill(32))
  results_bin25.append(bin(int(results25[i], 16))[2:].zfill(32))
  results_bin26.append(bin(int(results26[i], 16))[2:].zfill(32))
  results_bin27.append(bin(int(results27[i], 16))[2:].zfill(32))
  results_bin28.append(bin(int(results28[i], 16))[2:].zfill(32))
  results_bin29.append(bin(int(results29[i], 16))[2:].zfill(32))
  results_bin30.append(bin(int(results30[i], 16))[2:].zfill(32))
  results_bin31.append(bin(int(results31[i], 16))[2:].zfill(32))
  results_bin32.append(bin(int(results32[i], 16))[2:].zfill(32))
  results_bin33.append(bin(int(results33[i], 16))[2:].zfill(32))
  results_bin34.append(bin(int(results34[i], 16))[2:].zfill(32))
  results_bin35.append(bin(int(results35[i], 16))[2:].zfill(32))
  results_bin36.append(bin(int(results36[i], 16))[2:].zfill(32))
  results_bin37.append(bin(int(results37[i], 16))[2:].zfill(32))
  results_bin38.append(bin(int(results38[i], 16))[2:].zfill(32))
  results_bin39.append(bin(int(results39[i], 16))[2:].zfill(32))
  results_bin40.append(bin(int(results40[i], 16))[2:].zfill(32))
  results_bin41.append(bin(int(results41[i], 16))[2:].zfill(32))
  results_bin42.append(bin(int(results42[i], 16))[2:].zfill(32))
  results_bin43.append(bin(int(results43[i], 16))[2:].zfill(32))
  results_bin44.append(bin(int(results44[i], 16))[2:].zfill(32))
  results_bin45.append(bin(int(results45[i], 16))[2:].zfill(32))
  results_bin46.append(bin(int(results46[i], 16))[2:].zfill(32))
  results_bin47.append(bin(int(results47[i], 16))[2:].zfill(32))
  results_bin48.append(bin(int(results48[i], 16))[2:].zfill(32))
  results_bin49.append(bin(int(results49[i], 16))[2:].zfill(32))
  results_bin50.append(bin(int(results50[i], 16))[2:].zfill(32))
  results_bin51.append(bin(int(results51[i], 16))[2:].zfill(32))
  results_bin52.append(bin(int(results52[i], 16))[2:].zfill(32))
  results_bin53.append(bin(int(results53[i], 16))[2:].zfill(32))
  results_bin54.append(bin(int(results54[i], 16))[2:].zfill(32))
  results_bin55.append(bin(int(results55[i], 16))[2:].zfill(32))
  results_bin56.append(bin(int(results56[i], 16))[2:].zfill(32))
  results_bin57.append(bin(int(results57[i], 16))[2:].zfill(32))
  results_bin58.append(bin(int(results58[i], 16))[2:].zfill(32))
  results_bin59.append(bin(int(results59[i], 16))[2:].zfill(32))
  results_bin60.append(bin(int(results60[i], 16))[2:].zfill(32))
  results_bin61.append(bin(int(results61[i], 16))[2:].zfill(32))
  results_bin62.append(bin(int(results62[i], 16))[2:].zfill(32))
  results_bin63.append(bin(int(results63[i], 16))[2:].zfill(32))
  results_bin64.append(bin(int(results64[i], 16))[2:].zfill(32))
  results_bin65.append(bin(int(results65[i], 16))[2:].zfill(32))
  results_bin66.append(bin(int(results66[i], 16))[2:].zfill(32))
  results_bin67.append(bin(int(results67[i], 16))[2:].zfill(32))
  results_bin68.append(bin(int(results68[i], 16))[2:].zfill(32))
  results_bin69.append(bin(int(results69[i], 16))[2:].zfill(32))
  results_bin70.append(bin(int(results70[i], 16))[2:].zfill(32))
  results_bin71.append(bin(int(results71[i], 16))[2:].zfill(32))
  results_bin72.append(bin(int(results72[i], 16))[2:].zfill(32))
  results_bin73.append(bin(int(results73[i], 16))[2:].zfill(32))
  results_bin74.append(bin(int(results74[i], 16))[2:].zfill(32))
  results_bin75.append(bin(int(results75[i], 16))[2:].zfill(32))
  results_bin76.append(bin(int(results76[i], 16))[2:].zfill(32))
  results_bin77.append(bin(int(results77[i], 16))[2:].zfill(32))
  results_bin78.append(bin(int(results78[i], 16))[2:].zfill(32))
  results_bin79.append(bin(int(results79[i], 16))[2:].zfill(32))
  results_bin80.append(bin(int(results80[i], 16))[2:].zfill(32))
  results_bin81.append(bin(int(results81[i], 16))[2:].zfill(32))
  results_bin82.append(bin(int(results82[i], 16))[2:].zfill(32))
  results_bin83.append(bin(int(results83[i], 16))[2:].zfill(32))
  results_bin84.append(bin(int(results84[i], 16))[2:].zfill(32))
  results_bin85.append(bin(int(results85[i], 16))[2:].zfill(32))
  results_bin86.append(bin(int(results86[i], 16))[2:].zfill(32))
  results_bin87.append(bin(int(results87[i], 16))[2:].zfill(32))
  results_bin88.append(bin(int(results88[i], 16))[2:].zfill(32))
  results_bin89.append(bin(int(results89[i], 16))[2:].zfill(32))
  results_bin90.append(bin(int(results90[i], 16))[2:].zfill(32))
  results_bin91.append(bin(int(results91[i], 16))[2:].zfill(32))
  results_bin92.append(bin(int(results92[i], 16))[2:].zfill(32))
  results_bin93.append(bin(int(results93[i], 16))[2:].zfill(32))
  results_bin94.append(bin(int(results94[i], 16))[2:].zfill(32))
  results_bin95.append(bin(int(results95[i], 16))[2:].zfill(32))
  results_bin96.append(bin(int(results96[i], 16))[2:].zfill(32))
  results_bin97.append(bin(int(results97[i], 16))[2:].zfill(32))
  results_bin98.append(bin(int(results98[i], 16))[2:].zfill(32))
  results_bin99.append(bin(int(results99[i], 16))[2:].zfill(32))

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
  temp_results.append(results_bin10[i])
  temp_results.append(results_bin11[i])
  temp_results.append(results_bin12[i])
  temp_results.append(results_bin13[i])
  temp_results.append(results_bin14[i])
  temp_results.append(results_bin15[i])
  temp_results.append(results_bin16[i])
  temp_results.append(results_bin17[i])
  temp_results.append(results_bin18[i])
  temp_results.append(results_bin19[i])
  temp_results.append(results_bin20[i])
  temp_results.append(results_bin21[i])
  temp_results.append(results_bin22[i])
  temp_results.append(results_bin23[i])
  temp_results.append(results_bin24[i])
  temp_results.append(results_bin25[i])
  temp_results.append(results_bin26[i])
  temp_results.append(results_bin27[i])
  temp_results.append(results_bin28[i])
  temp_results.append(results_bin29[i])
  temp_results.append(results_bin30[i])
  temp_results.append(results_bin31[i])
  temp_results.append(results_bin32[i])
  temp_results.append(results_bin33[i])
  temp_results.append(results_bin34[i])
  temp_results.append(results_bin35[i])
  temp_results.append(results_bin36[i])
  temp_results.append(results_bin37[i])
  temp_results.append(results_bin38[i])
  temp_results.append(results_bin39[i])
  temp_results.append(results_bin40[i])
  temp_results.append(results_bin41[i])
  temp_results.append(results_bin42[i])
  temp_results.append(results_bin43[i])
  temp_results.append(results_bin44[i])
  temp_results.append(results_bin45[i])
  temp_results.append(results_bin46[i])
  temp_results.append(results_bin47[i])
  temp_results.append(results_bin48[i])
  temp_results.append(results_bin49[i])
  temp_results.append(results_bin50[i])
  temp_results.append(results_bin51[i])
  temp_results.append(results_bin52[i])
  temp_results.append(results_bin53[i])
  temp_results.append(results_bin54[i])
  temp_results.append(results_bin55[i])
  temp_results.append(results_bin56[i])
  temp_results.append(results_bin57[i])
  temp_results.append(results_bin58[i])
  temp_results.append(results_bin59[i])
  temp_results.append(results_bin60[i])
  temp_results.append(results_bin61[i])
  temp_results.append(results_bin62[i])
  temp_results.append(results_bin63[i])
  temp_results.append(results_bin64[i])
  temp_results.append(results_bin65[i])
  temp_results.append(results_bin66[i])
  temp_results.append(results_bin67[i])
  temp_results.append(results_bin68[i])
  temp_results.append(results_bin69[i])
  temp_results.append(results_bin70[i])
  temp_results.append(results_bin71[i])
  temp_results.append(results_bin72[i])
  temp_results.append(results_bin73[i])
  temp_results.append(results_bin74[i])
  temp_results.append(results_bin75[i])
  temp_results.append(results_bin76[i])
  temp_results.append(results_bin77[i])
  temp_results.append(results_bin78[i])
  temp_results.append(results_bin79[i])
  temp_results.append(results_bin80[i])
  temp_results.append(results_bin81[i])
  temp_results.append(results_bin82[i])
  temp_results.append(results_bin83[i])
  temp_results.append(results_bin84[i])
  temp_results.append(results_bin85[i])
  temp_results.append(results_bin86[i])
  temp_results.append(results_bin87[i])
  temp_results.append(results_bin88[i])
  temp_results.append(results_bin89[i])
  temp_results.append(results_bin90[i])
  temp_results.append(results_bin91[i])
  temp_results.append(results_bin92[i])
  temp_results.append(results_bin93[i])
  temp_results.append(results_bin94[i])
  temp_results.append(results_bin95[i])
  temp_results.append(results_bin96[i])
  temp_results.append(results_bin97[i])
  temp_results.append(results_bin98[i])
  temp_results.append(results_bin99[i])

  for j in itertools.combinations(temp_results, 2):
    hamming_dist.append(hamming2(j[0], j[1]))
  temp_results = []

fp = open("hamming_results.dat", "w")
for i in range(0, len(hamming_dist)):
  fp.write(hamming_dist[i]+"\n")

print(hamming_dist.count(0))
print(hamming_dist.count(1))
print(hamming_dist.count(2))
print(hamming_dist.count(3))
print(hamming_dist.count(4))
print(hamming_dist.count(5))
print(hamming_dist.count(6))
plt.hist(hamming_dist, bins=4, color='blue')
plt.savefig("histXX_4bins.png")
#plt.hist(hamming_dist, bins=16, color='blue')
#plt.savefig("histXX_16bins.png")
#plt.hist(hamming_dist, bins=32, color='blue')
#plt.savefig("histXX_32bins.png")
plt.show()