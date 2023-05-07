#!/usr/bin/python
# import sys
# for line in sys.stdin.buffer:
#     line = line.strip()
#     words = line.split()
#     for word in words:
#         print("%s\t%s" % (word, 1))

import sys
import io
import codecs

input_stream = codecs.getreader("utf-8")(sys.stdin)

for line in input_stream:
    line = line.lower()
    words = line.split()
    for word in words:
       print("%s\t%s" %(word,1))
  
#   cat input.rtf |python mapper.py
# cat input.rtf |python mapper.py |sort| python reducer.py
# hdfs dfs -mkdir /hadpy
# hdfs dfs -copyFromLocal /home/abhi/input.txt /hadpy
#   hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar -input /hadpy/wordc.txt -output /hadout/output -file mapper.py -file reducer.py -mapper 'python3 mapper.py' -reducer 'python3 reducer.py'
  