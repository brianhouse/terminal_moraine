from util.turtle import Turtle

t = Turtle(1000, 700, "GROWTH")

def draw(limb, angle=0):
    t.right(limb.angle)
    t.width = limb.age / 4
    t.color = 50, 0, 0
    t.forward(limb.age)
    t.circle(t.width / 2)
    if limb.has_leaf:
        t.color = 0, 150, 20
        t.circle(5)
    else:
        x, y = t.x, t.y
        angle = t.a
        for c, child in enumerate(limb.children):
            draw(child)
            t.jump(x, y)
            t.face(angle)

def start(root):
    def loop(root):
        def f():
            t.reset()
            t.jump(500, 700)
            draw(root)
        return f
    t.start(loop(root))
