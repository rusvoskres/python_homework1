import os
from os import mkdir
from os import rmdir as remover
from os import *

# remover('test')
# mkdir('test')
print(getcwd())

print(list(walk(getcwd())))