

def check(f):
    def inside(a,b):    # inside === f
        if(b == 0):
            print(" can't divide 0")
            return
        return f(a,b)
    return inside


# @check
def div(a,b):
    return a/b
# print(div(4,2))


# x_fn = check(div)(4,2)    # === @check
# print(x_fn)


def make_tag(tag_name):
    def decor(f):
        def wrapper(text):
            return '<%(tag)s> %(text)s <%(tag)s>' %dict(tag = tag_name,text = f(text) )
        return wrapper
    return decor

@make_tag('div')
@make_tag('div')
def fn(text):
    return text+'...'
print(fn('text to show'))

fnew = make_tag('div')(fn)('text to show')   # ===  @make_tag('div') ????
# print(fnew)     # fnew  ===  return '<%(tag)s> %(text)s <%(tag)s>' %dict(tag = tag_name,text = f(text) )
