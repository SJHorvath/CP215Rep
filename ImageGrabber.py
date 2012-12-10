import re
import os
import urllib2
import sys
import string


page_file = urllib2.urlopen(raw_input(),'r')
url_text = page_file.read()
regex = re.compile('<img[^>]*\ssrc="(.*?)"',re.IGNORECASE)
matches= re.findall(regex,url_text)


i = 0

for match in matches:
		output_file_name = 'output_%d.jpg'%(i,)
		i +=1
		req = urllib2.Request(match)
		response = urllib2.urlopen(req)
		output = open(output_file_name,'wb')
		output.write(response.read())
		output.close()
# output = open('out.jpg','wb')
# output.write(response.read())
# output.close()
