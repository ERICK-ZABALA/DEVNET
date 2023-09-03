#!/usr/bin/python3
import re, datetime

startTime = datetime.datetime.now()
term1 = re.compile('ACLLOG-5-ACLLOG_FLOW_INTERNAL')
term2 = re.compile('ACLLOG-6-ACLLOG_FLOW_INTERNAL')

file_list = ['sample_syslog_nexus.log', 'sample_syslog_nexus_1.log']
            
for log in file_list:
    with open(log, 'r') as file:
        for line in file.readlines():
            if re.search(term1, line) or re.search(term2, line):
                print(line)

endTime = datetime.datetime.now()
elapsedTime = endTime - startTime
print("Spend Time looking for: " + str(elapsedTime))
