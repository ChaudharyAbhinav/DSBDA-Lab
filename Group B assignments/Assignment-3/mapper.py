//python 2 code:    use this code if u have python 2

import sys
import io
import codecs

input_stream = codecs.getreader("utf-8")(sys.stdin)

for line in input_stream:
    line = line.lower()
    words = line.split()
    for word in words:
       print("%s\t%s" %(word,1))
    
    
    
//python 3 code:    use this code if u have python 3
import sys
import io
input_stream = io.TextIOWrapper(sys.stdin.buffer)

for line in input_stream:
	line = line.lower()
	words = line.split()
	for word in words:
		print("%s\t%s" %(word,1))
