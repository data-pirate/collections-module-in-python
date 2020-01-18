from collections import namedtuple

convo = namedtuple('robo_convo', "hi bye how_are_you")

robot = convo(hi = 'hello', bye = 'see you soon', how_are_you = 'fine')

hi,bye,how_are_you = robot

print('hi:',hi)
print('how are you:',how_are_you)
print('Bye:',bye)
