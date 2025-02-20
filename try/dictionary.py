def dictionary():
    'functional implemention of dictionary'
    records=[]
    def additem(key,value):
        nonlocal records
        records.append((key,value))
    def getitem(key,r):
        assert r!=[],'key not found'
        if r[0][0]==key:
            return r[0][1]
        else:
            return getitem(key,r[1:])
    def delitem(key):
        nonlocal records
        def delete(r):
            assert r!=[],'key not found'
            if r[0][0]==key:
                if len(r)==1:
                    return []
                return r[1:]
            else:
                return [r[0]]+delete(r[1:]) 
        records=delete(records)
    def printall():
        print(records)
    def dispatch(message,key=None,value=None):
        if message=='additem':
            return additem(key,value)
        elif message=='getitem':
            return getitem(key,records)
        elif message=='delitem':
            return delitem(key)
        elif message=='printall':
            return printall()
    return dispatch