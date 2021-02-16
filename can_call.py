'''
If there exists a path in the call graph for some_file.c from caller
to callee, the tool should print out 'True' to standard output.  Otherwise the
tool should print "None" to the console.
'''

__author__= "Vasileios Klimis"
__email__ = "vklimis@icloud.com"

""" Usage: call with <filename> <caller> <callee>
"""

import sys
from clang.cindex import CursorKind
from clang.cindex import Index
from clang.cindex import TypeKind


visited = set() # Set to keep track of visited nodes.

def dfs(caller):
    if str(caller) not in visited and caller.get_children():
        visited.add(str(caller))
        # find all function declarations within
        # a translation unit for a source file.
        for child in caller.get_children():
            if child.spelling == sys.argv[3]:
                sys.exit("True")
            # this will traverse the sub-tree from
            # the 'child' node at the root, covering
            # the case of having prototype function
            off(child.spelling)
            dfs(child)


def all_functions(node):
    """ Retrieve list of function declarations in a translation unit
    """
    funcs = []
    for c in node.get_children():
        if c.kind == CursorKind.FUNCTION_DECL:
            funcs.append(c)
    return funcs


def off(caller):
    for i in all_functions(root):
        if i.spelling == caller:
            dfs(i)


# Entry point: load the C source code
index = Index.create()
translation_unit = index.parse(sys.argv[1])

# The translation unit cursor exists primarily to act
# as the root cursor for traversing the contents of a
# translation unit (cursor is a generic object for
# representing a node in the AST)
root = translation_unit.cursor

'''for i in find_callers(root):
    print(i.spelling)'''

print(off(sys.argv[2]))