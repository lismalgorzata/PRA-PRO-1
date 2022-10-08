import re

text='To be, or not to be, that is the question'

vowels=re.findall("[aeiou]",text)
count=len(vowels)

print('Number of vowels: ',count)