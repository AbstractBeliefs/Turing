#!/usr/bin/env python
import TM

rule = {
    0:{
        'a':{
            'w': 1,
            'm': 1,
            'n': 'b'
            },
        'b':{
            'w': 1,
            'm': -1,
            'n': 'a'
            },
        'c':{
            'w': 1,
            'm': -1,
            'n': 'b'
            },
        },
    1:{
        'a':{
            'w': 1,
            'm': -1,
            'n': 'c'
            },
        'b':{
            'w': 1,
            'm': 1,
            'n': 'b'
            },
        'c':{
            'w': 1,
            'm': 1,
            'n': 'halt'
            },
        },
}

class BB(TM.machine):
    startstate = 'a'
    startpos = 0
    states = ['a','b','c','halt']
    blank = 0

tape = {0:0}
mymach = BB(rule)
i = TM.interpreter(mymach, tape)
i.mainloop()
