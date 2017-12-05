#!/usr/bin/env python

import sqlite3
import sys

lines = []

#read in csv data
with open(sys.argv[1], "r") as data:
    for line in data:
        lines.append(line.strip())

def prepare_data(lines):
    TARGET_FIELDS = ["id", "Date", "OFFERED", "ANSWERED", "AVG ANS DELAY SECONDS", "MAX ANS DELAY", "ABANDONED", "DelayCallsProduct"] 
    out = []
    for line in lines:
        out.append(line.split(","))
    head = out[0]
    tail = out[1:len(out)]
    
    remove_indices = []
    fields = []
    for i in range(len(head)):
        if head[i] not in TARGET_FIELDS:
            remove_indices.append(i)
        else:
            fields.append(head[i])

    rows = []
    for row in tail:
        new_row = []
        for i in range(len(row)):
            if not i in remove_indices:
                new_row.append(row[i])
        rows.append(new_row)

    return fields, rows

def make_queries(fields, data):
    pass


fields, rows = prepare_data(lines)
print(fields)
print(rows)
#conn = sqlite3.connect("311CallCentre.db")
#curse = conn.cursor()


