def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be trees!'
    return [label]+branches
def root_label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
'''
对象
--------------------------------------
对象操作
'''
def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        return is_tree(branch)
    return True
def is_leaf(tree):
    return not branches(tree)
#判断操作
#----------------
#<量化操作
def count_leaf(tree):
    if is_leaf(tree):return 1
    else:
        sum_list=[count_leaf(b) for b in branches(tree)]
        return sum(sum_list)
def sum_label(tree):
    if is_leaf(tree):return root_label(tree)
    sum_list=[sum_label(b) for b in branches(tree)]
    return sum(sum_list,root_label(tree))
#量化操作>
#----------------
#打印操作
def print_tree(tree,space=0):
    print(" "*space+str(root_label(tree)))
    for branch in branches(tree):
        print_tree(branch,space+1)


#以下是实例:
t=tree(1,[tree(2,[[4],[5]]),[3]])#运行成功无报错
#实例1
def fib_tree(n):
    '''递归创建斐波那契tree'''
    if n<2:
        return tree(n)
    return tree(n,[fib_tree(n-1),fib_tree(n-2)])
#实例2
def partition_tree(n,m):
    '''
    用不大于m的整数分割n
    label=m
    第一个分支表示用至少一个m
    第二个分支表示不用m(用1~m-1)
    '''
    if n==0:return tree(True)
    if n<0 or m==0: return tree(False)
    left=partition_tree(n-m,m)
    right=partition_tree(n,m-1)
    return tree(m,[left,right])
def print_parts(tree,partition=[]):#打印所有可能的情形
    if is_leaf(tree) :
        if root_label(tree):
            print (' + '.join(partition))
        else: return
    else:
        left,right=branches(tree)
        m=str(root_label(tree))
        print_parts(left,partition+[m])
        print_parts(right,partition)
