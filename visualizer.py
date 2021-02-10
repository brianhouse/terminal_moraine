from util.animation import Context

ctx = Context(1000, 700, "GROWTH")

def draw(limb):
    size = limb.load
    ctx.line(*limb.start, *limb.end, size, (50, 0, 0))
    ctx.circle(*limb.end, size / 2, (50, 0, 0))
    for child in limb.children:
        draw(child)
    if limb.leaf:
        ctx.circle(*limb.leaf.position, 5 * limb.leaf.intensity, (0, 150, 20))

def start(tree):
    def loop():
        draw(tree.root)
    ctx.start(loop)
