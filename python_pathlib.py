import pathlib

p = pathlib.Path('readme.md')
print(p)
print(p.exists())
print(p.resolve())
