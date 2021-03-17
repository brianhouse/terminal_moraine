from util.animation import Context

ctx = Context(600, 600, "GROWTH")

def draw_side(limb):
    size = limb.load
    ctx.line(*limb.start[:2], *limb.end[:2], size, (50, 0, 0))
    ctx.circle(*limb.end[:2], size / 2, (50, 0, 0))
    for child in limb.children:
        draw_side(child)
    if limb.leaf:
        ctx.circle(*limb.leaf.position[:2], 5 * limb.leaf.maturity, (0, 150, 20))

def draw_top(limb):
    size = limb.load
    ctx.line(*limb.start[::2], *limb.end[::2], size, (50, 0, 0))
    ctx.circle(*limb.end[::2], size / 2, (50, 0, 0))
    for child in limb.children:
        draw_top(child)
    if limb.leaf:
        ctx.circle(*limb.leaf.position[::2], 5 * limb.leaf.maturity, (0, 150, 20))

def start(tree):
    def loop():
        # draw_side(tree.root)
        draw_top(tree.root)
    ctx.start(loop)
