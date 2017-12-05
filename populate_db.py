#!/usr/bin/env python

import sqlite3
import sys

lines = []
TARGET_FIELDS = ["id", "Date", "APPLICATION", "OFFERED", "ANSWERED", "AVG ANS DELAY SECONDS", "MAX ANS DELAY", "ABANDONED", "DelayCallsProduct"] 
csvTodb = {
            "id" : "id",
            "Date" : "date",
            "OFFERED" : "offered",
            "ANSWERED": "answered",
            "AVG ANS DELAY SECONDS" : "avg_ans_delay_seconds",
            "MAX ANS DELAY" : "max_ans_delay",
            "ABANDONED" : "abandonned",
            "DelayCallsProduct": "delay_calls_product",
            "APPLICATION": "tableName"
        }

csvToIndex = {}
for i in range(len(TARGET_FIELDS)):
    csvToIndex[TARGET_FIELDS[i]] = i

#read in csv data
with open(sys.argv[1], "r") as data:
    for line in data:
        lines.append(line.strip())

def prepare_data(lines):
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

    for row in rows:
        row[1] = row[1].replace("/", "-")
        for i in range(len(row)):
            if row[i] == "":
                row[i] = "NULL"

    return fields, rows

def make_queries(fields, data):
   query_template = "INSERT INTO {tableName} VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
   queries = []
   for row in data:
       queries.append((
           query_template.format(tableName = row[csvToIndex["APPLICATION"]].replace("ccc_311_", "").replace("ccc_", "")),
            (
                row[csvToIndex["id"]],
                row[csvToIndex["Date"]],
                row[csvToIndex["OFFERED"]],
                row[csvToIndex["ANSWERED"]],
                row[csvToIndex["AVG ANS DELAY SECONDS"]],
                row[csvToIndex["MAX ANS DELAY"]],
                row[csvToIndex["ABANDONED"]],
                row[csvToIndex["DelayCallsProduct"]]
            ),
            row[csvToIndex["APPLICATION"]].replace("ccc_311_", "").replace("ccc_", "")))
   return queries

fields, rows = prepare_data(lines)
assert(fields == TARGET_FIELDS)
print(fields)
queries = make_queries(fields, rows)
conn = sqlite3.connect("311CallCentre.db")
curse = conn.cursor()

for query in queries:
    print(query)
    q, params, tableName = query
    try:
        curse.execute(q, params)
    except sqlite3.OperationalError as e:
        curse.execute("CREATE TABLE '{}' ('id' TEXT NOT NULL, 'date' DATETIME NOT NULL, 'offered' INTEGER NOT NULL, 'answered' INTEGER NOT NULL, 'avg_ans_delay_seconds' INTEGER NOT NULL, 'max_ans_delay' INTEGER, 'abandonned' INTEGER NOT NULL, 'delay_calls_product' INTEGER NOT NULL)".format(tableName))
        curse.execute(q, params)

conn.commit()


