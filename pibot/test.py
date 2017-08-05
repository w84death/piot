from blessed import Terminal

t = Terminal()

with t.fullscreen():
    x=y=4
    for x in range(4, t.width - 4):
        print(t.move(y,x)+'{t.cyan}='.format(t=t))
    for y in range(4, t.height - 4):
        print(t.move(y,x)+'{t.cyan}|'.format(t=t))
    for x in range(4, t.width - 4):
        print(t.move(y,x)+'{t.cyan}='.format(t=t))
    x=y=4
    for y in range(4, t.height - 4):
        print(t.move(y,x)+'{t.cyan}|'.format(t=t))
    t.inkey()