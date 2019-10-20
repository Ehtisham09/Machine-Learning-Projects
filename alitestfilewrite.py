import codecs

import os




path=os.path.abspath('datafiles/CurrentAffairs1.txt')
ff=codecs.open(path,'r',encoding='utf-8',errors='ignore')
text=ff.read()

print(type(text))

path=os.path.abspath('datafiles/write.txt')
ff=codecs.open(path,'w',encoding='utf-8',errors='ignore')
ff.write(text)
