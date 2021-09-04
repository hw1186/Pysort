'''def numeric_compare(x, y):
    return x - y
sorted([5, 2, 4, 1, 3], cmp=numeric_compare)
'''
# 비교순서를 다음과 같이 뒤집을수 있다

'''def reverse_numeric(x, y):
    return y - x
sorted([5, 2, 4, 1, 3], cmp=reverse_numeric'''

def cmp_to_key(mycmp):
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K