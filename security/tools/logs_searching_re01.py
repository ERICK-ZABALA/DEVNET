#!/usr/bin/python3
import re, datetime

startTime = datetime.datetime.now()
searchTerm = re.compile('ACLLOG-5-ACLLOG_FLOW_INTERNAL')
with open('sample_syslog_nexus.log', 'r') as file:
    for line in file.readlines():
        if re.search(searchTerm, line):
            print(line)
endTime = datetime.datetime.now()
elapsedTime = endTime - startTime
print("Spend Time looking for: " + str(elapsedTime))
