import sys
import io
import codecs

input_stream = codecs.getreader("utf-8")(sys.stdin)

for line in input_stream:
    line = line.lower()
    words = line.split()
    for word in words:
       print("%s\t%s" %(word,1))