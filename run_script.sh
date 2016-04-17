#!/bin/bash
for((i=0;i<100;i++));
do
  ./hello
  cp results.dat results03_$i.dat
  echo "Finished run " $i
done
