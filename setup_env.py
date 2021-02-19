import os 

with open(os.environ['GITHUB_ENV'], 'a+') as f:
    f.write("foo=bar")

