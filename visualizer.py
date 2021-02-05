from util.animation import Context

ctx = Context(1000, 700, "GROWTH")

def draw(limb):
    ctx.line(*limb.start, *limb.end, limb.size / 4, (50, 0, 0))
    ctx.circle(*limb.end, limb.size / 8, (50, 0, 0))
    for child in limb.children:
        draw(child)
    if limb.leaf:
        ctx.circle(*limb.leaf.position, 5 * limb.leaf.intensity, (0, 150, 20))

def start(root):
    def loop():
        draw(root)
    ctx.start(loop)
