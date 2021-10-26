import requests

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers=headers)
print(r.text[:100])

# The code generates an error that suggests the requests module does not have a get  method.
# The requests library does actually have a get  method.
# Import statements first look for a local file in the current directory (e.g. requests.py).
# If there is such file it imports that file, and not the actual module.


#
# In the code Python is actually referring to the script name which is requests  and it doesn't find a get attribute for that name.
# Script names load in the current namespace. They are actually stored in the __name__  variable.
# You could try to print that variable out and you would see that it prints your script name.
# Therefore you should not name your scripts under library names.