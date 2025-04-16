#!/usr/bin/env python3
"""
Parse Nessus CSV exports to filter high/critical findings and summarize key details.
"""

import csv

def parse_nessus_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            severity = row['Severity']
            if severity in ['High', 'Critical']:
                print(f"[{severity}] {row['Plugin Name']}: {row['Host']} - {row['Port']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python parse_nessus.py <nessus_export.csv>")
    else:
        parse_nessus_csv(sys.argv[1])
