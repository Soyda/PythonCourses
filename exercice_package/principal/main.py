import os
import sys
import inspect


principaldir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
exercicedir =  os.path.dirname(principaldir)
sys.path.insert(0, exercicedir)
childdir = os.path.join(principaldir, "child_folder")
sys.path.insert(0, childdir)

print(principaldir)
print(exercicedir)
print(childdir)

from parent_file import multiply
from principal.slevel import add
from child_folder.child import divide

print(round(divide(add(5, multiply(2,3)), 3), 2))

