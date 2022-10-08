import re

text='To be, or not to be, that is the question'

words=re.findall("\w+",text)
count=len(words)

print('Number of words: ',count)