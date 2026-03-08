#two types of modules in python :
# -built in modules
# -external modules
#list of all built in modules : https://docs.python.org/3/py-modindex.html

import math 
import os
import mymodule
import requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("http://www.google.com")
print(r.text)

