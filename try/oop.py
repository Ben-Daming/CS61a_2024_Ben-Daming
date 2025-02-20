#class,entity,inheritance
class Account:
    interest=0.01
    def __init__(self,name):
        self.name=name
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        assert self.balance>=amount,'not enough money'
        self.balance-=amount
        return self.balance   
class Pro_Account(Account):
    interest=0.02
    withdraw_fee=1
    def withdraw(self, amount):
        return super().withdraw(amount+self.withdraw_fee)
'oop设计:1.多用method 2.instance preferred'
#composition:一个对象将另一个对象作为属性
'''
inheritance适用于"is a"问题
如,pro_account is a type of account

composition适用于'has a'问题
eg,a bank has bank accounts
'''
#design a bank
class Bank:
    '''
    A bank has accounts
    >>> bank = Bank()
    >>> John = bank.open_account('john',10)
    >>> Jack = bank.open_account('Jack',5,Pro_Account)
    >>> John.interest
    0.01
    >>> Jack.interest
    0.02
    >>> bank.pay_interest()
    >>> John.balance
    10.1
    '''
    def __init__(self):
        self.accounts=[]
    def open_account(self,holder,amount,kind=Account):
        account=kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    def pay_interest(self):
        for each in self.accounts:
            each.deposit(each.balance*each.interest)
#多重继承
class saving_Account(Account):
    deposit_fee=2
    def deposit(self,amount):
        return super().deposit(amount-self.deposit_fee)
class good_account(saving_Account,Pro_Account):
    def __init__(self, name):
        super().__init__(name)
        self.balance=10
'---------------------------------------------------------------'
#链表
class Link:
    empty=()
    def __init__(self,label,rest=empty):
        assert isinstance(rest,Link) or rest is Link.empty, "the rest not Link"
        self.label,self.rest=label,rest
    def __str__(self):
        def charlist(link):
            if link.rest:
                return [str(link.label)]+charlist(link.rest)
            else:
                return [str(link.label)]
        return '->'.join(charlist(self))
    def __repr__(self):
        if self.rest:
            str_rest=', '+repr(self.rest)
        else:
            str_rest=''
        return f'Link({repr(self.label)}{str_rest})'
#map,filter,range的链表实现
def range_link(start,end):
    if start>=end:
        return Link.empty
    else:
        return Link(start,range_link(start+1,end))
def map_link(f,linklist):
    assert isinstance(linklist,Link) or linklist is Link.empty
    if linklist is Link.empty:
        return linklist
    else:
        return Link(f(linklist.label),map_link(f,linklist.rest))
def filter_link(f,linklist):
    assert isinstance(linklist,Link) or linklist is Link.empty
    if linklist is Link.empty:
        return linklist
    elif f(linklist.label):
        return Link(linklist.label,filter_link(f,linklist.rest))
    else:
        return filter_link(f,linklist.rest)

def add_link(s,v):
    'add v into a sorted link s,return the modified s'
    'if repeated,still return s'
    assert s is not Link.empty and isinstance(s,Link)
    if s.label>v:
        s.label,s.rest=v,Link(s.label,s.rest)#s.label,s.rest都是变动前的s属性
    elif s.label<v and s.rest is Link.empty:
        s.rest=Link(v)
    else:
        add_link(s.rest,v)
    return s

#树class实现
class Tree:
    def __init__(self,label,branches=None):
        assert branches is None or all(isinstance(branch,Tree) for branch in branches),'all branches must be tree'
        self.label=label
        if branches is None:
            self.branches=[]#防止默认值可变类型陷阱
        else:
            self.branches=branches
    def __repr__(self):
        if self.branches:
            str_branch=', '+repr(self.branches)
        else:
            str_branch=''
        return f'Tree({self.label}{str_branch})'
    def __str__(self):
        def charlist(tree):#return the list of tree
            mylist=[str(tree.label)]
            for b in tree.branches:
                mylist+=[' '+i for i in charlist(b)]
            return mylist
        return '\n'.join(charlist(self))
    'higher method'
    def is_leaf(self):return not self.branches
    def leaves(self):#return list of all the leaves of tree
        if not self.is_leaf():
            mylist=[]
            for b in self.branches:
                mylist+=b.leaves()
            return mylist
        else: return [self.label]
    def height(self):#return height of tree
        if self.is_leaf():return 0
        else:
            return 1+max([b.height() for b in self.branches])
#construct fib_tree
def fib_tree(n):
    if n ==1 or n ==0:
        return Tree(n)
    else:
        left=fib_tree(n-1)
        right=fib_tree(n-2)
        value=left.label+right.label
        return Tree(value,[left,right])