#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect("../311CallCentre.db")
curse = conn.cursor()

curse.execute("SELECT name FROM sqlite_master WHERE type='table';")
names = [i[0] for i in curse.fetchall()]
print(names)

with open("gen.template", "r") as template:
    template_script = template.read()
    for i in range(len(names)):
        with open("gen%s.R" % i, "w") as out:
            outStr = template_script.format(num = i, tableName = names[i])
            out.write(outStr)
