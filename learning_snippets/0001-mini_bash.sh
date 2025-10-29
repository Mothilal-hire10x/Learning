#!/usr/bin/env bash
# Mini: print the first N Fibonacci numbers (default 10)
# Usage: ./0001-mini_bash.sh 15
N=${1:-10}
a=0
b=1
for i in $(seq 1 "$N"); do
  printf "%d" "$a"
  if [ "$i" -lt "$N" ]; then
    printf " "
  else
    printf "\n"
  fi
  fn=$((a + b))
  a=$b
  b=$fn
done
