import os, sys
import types


for i in dir(os):
    #print(type(i))
    # if type(i) == "<class 'builtin_function_or_method'>":

     print(i.__doc__)
#print([os.__dict__.get(a) for a in dir(os) if isinstance(os.__dict__.get(a), types.FunctionType)])

for i in dir(sys):
    print(i.__doc__)