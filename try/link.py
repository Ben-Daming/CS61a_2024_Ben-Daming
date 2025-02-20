'return a list with the first element and the rest'
def link(first,rest):
    assert is_link(rest), 'rest must be a linked list'
    return [first,rest]

'return first element of the list_link'
def first(linklist):
    assert is_link(linklist), 'first must apply on linked list'
    assert  linklist!='empty', 'empty list has no first element'
    return linklist[0]

'return the rest linklist of the linklist'
def rest(linklist):
    assert is_link(linklist), 'rest must apply on a linked list'
    assert linklist!='empty', 'empty list has no rest element'
    return linklist[1]

'check if the object is linked list'
def is_link(linklist):
    return linklist=='empty' or (type(linklist)==list and len(linklist)==2 and is_link(linklist[1]))
'''
data abstraction done
-------------------------------------
object method
'''
#get the len of linked list
def len_link(s):
    if s=='empty':return 0
    return len_link(rest(s))+1

#get a list with linked list s followed by t
def extend_link(s,t):
    assert is_link(s) and is_link(t), 'arguments not all linked list'
    if s=='empty':
        return t
    return link(first(s),extend_link(rest(s),t))

#return a string of all elements separated by separator
def string_link(s,separator=" "):
    assert is_link(s), 'first argument is not linked list'
    if s=='empty':
        return ""
    return str(first(s))+separator+string_link(rest(s),separator)
"""
basic method done
----------------
build-up method
"""
#return a functional implementation of mutable linked list
def mutable_link():
    contents='empty'
    def dispatch(message,value=None):
        nonlocal contents
        if message=='len':
            return len(contents)
        if message=='push':
            contents=link(value,contents)
        if message=='pop':
            assert contents!='empty', 'pop from empty linked list'
            contents=rest(contents)
        if message=='getitem':
            return getitem_link(contents,value)
        if message=='append':
            contents=extend_link(contents,link(value,'empty'))
        if message=='delete':
            contents=delete_item_link(contents,value)
        if message=='string':
            return string_link(contents)
    return dispatch

#return a linked list with elements same as list source
def list_to_link(source):
    assert type(source)==list, 'argument must be a list'
    s=mutable_link()
    for i in range(len(source)-1,-1,-1):
        s('push',source[i])
    return s

'''
bulid-up method done
---------------------
helper method
'''

#get the element at index i of linked list
def getitem_link(s,i):
    assert s!='empty', 'index out of length'
    if not i:
        return first(s)
    return getitem_link(rest(s),i-1)

#apply function to all elements in linked list
def apply_all_link(f,s):
    assert is_link(s), 'second argument is not linked list'
    if s=='empty':
        return s
    return link(f(first(s)),apply_all_link(f,rest(s)))

#return a list with element of s which f(e)==true
def keep_if_link(f,s):
    assert is_link(s), 'second argument is not linked list'
    if s=='empty':return s
    check=first(s)
    if f(check):
        return link(check,keep_if_link(f,rest(s)))
    return keep_if_link(f,rest(s))

#delete element at index in linked list s
def delete_item_link(s,i):
    assert is_link(s), 'first argument not linked list'
    assert s!='empty', 'index over length'
    assert i>=0, 'index invalid'
    if not i:
        return rest(s)
    return link(first(s),delete_item_link(rest(s),i-1))

