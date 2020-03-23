import pprint
class Shape:
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)    # (**kwds) is the KEY-PART

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

# cs = ColoredShape(color='red', shapename='circle')
# cs = ColoredShape(shapename='reactangle','red') # error
cs = ColoredShape('red',shapename='reactangle',) # ok 

print(cs.color,'-',cs.shapename)
