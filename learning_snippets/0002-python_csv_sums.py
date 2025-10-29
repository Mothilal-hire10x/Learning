#!/usr/bin/env python3
"""Mini: sum numeric columns in a CSV from stdin or file.
Usage: python3 0002-python_csv_sums.py data.csv
If no file is given, reads from stdin.
"""
import csv
import sys

def sums(reader):
    totals = []
    for row in reader:
        for i, cell in enumerate(row):
            try:
                val = float(cell)
            except Exception:
                val = 0.0
            if i >= len(totals):
                totals.append(val)
            else:
                totals[i] += val
    return totals

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    if path:
        f = open(path, newline='')
    else:
        f = sys.stdin
    reader = csv.reader(f)
    totals = sums(reader)
    for i, t in enumerate(totals, start=1):
        print(f"col{i}: {t}")
    if path:
        f.close()

if __name__ == '__main__':
    main()
