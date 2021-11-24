import re

txt = '# sadgepepesleep'
x = re.search('#.*', txt) 

if (x):
  print("Yes, there is at least one match!", x.group(x))
else:
  print("No match")