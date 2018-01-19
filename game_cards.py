#!/usr/bin/env python3

COLORS = {
    'w': 'white',
    'g': 'green',
    'b': 'blue',
    'r': 'red',
    'a': 'black',
    'j': 'joker'
}


class Card(object):
    def __init__(self, points, color, cost_dict):
        self.points = points
        self.color = color
        self.cost = cost_dict

    def __str__(self):
        return '(%s - %i - %s)' % (
            COLORS[self._color],
            self._points,
            ' '.join(['%s:%i' % (COLORS[x], self._cost[x]) for x in self._cost])
        )

    def __repr__(self):
        return self.__str__()


class Noble(object):
    def __init__(self, points, cost_dict):
        self._points = points
        self._cost = cost_dict

    def __str__(self):
        return '(%i points) %s' % (
            self._points,
            ' '.join(['%s:%i' % (x, self._cost[x]) for x in self._cost])
        )

    def __repr__(self):
        return self.__str__()


FIRST_CARDS = [
    Card(0, 'w', {'r':2, 'a':1}),
    Card(0, 'b', {'w':1, 'a':2}),
    Card(0, 'g', {'w':2, 'b':1}),
    Card(0, 'r', {'b':2, 'g':1}),
    Card(0, 'a', {'g':2, 'r':1}),

    Card(0, 'w', {'b':3}),
    Card(0, 'b', {'a':3}),
    Card(0, 'g', {'r':3}),
    Card(0, 'r', {'w':3}),
    Card(0, 'a', {'g':3}),

    Card(0, 'w', {'b':1, 'g':1, 'r':1, 'a':1}),
    Card(0, 'b', {'w':1, 'g':1, 'r':1, 'a':1}),
    Card(0, 'g', {'w':1, 'b':1, 'r':1, 'a':1}),
    Card(0, 'r', {'w':1, 'b':1, 'g':1, 'a':1}),
    Card(0, 'a', {'w':1, 'b':1, 'g':1, 'r':1}),

    Card(0, 'w', {'b':1, 'g':2, 'r':1, 'a':1}),
    Card(0, 'b', {'w':1, 'g':1, 'r':2, 'a':1}),
    Card(0, 'g', {'w':1, 'b':1, 'r':1, 'a':2}),
    Card(0, 'r', {'w':2, 'b':1, 'g':1, 'a':1}),
    Card(0, 'a', {'w':1, 'b':2, 'g':1, 'r':1}),

    Card(0, 'w', {'b':2, 'a':2}),
    Card(0, 'b', {'g':2, 'a':2}),
    Card(0, 'g', {'b':2, 'r':2}),
    Card(0, 'r', {'w':2, 'r':2}),
    Card(0, 'a', {'w':2, 'g':2}),

    Card(0, 'w', {'w':3, 'b':1, 'a':1}),
    Card(0, 'b', {'b':1, 'g':3, 'r':1}),
    Card(0, 'g', {'w':1, 'b':3, 'g':1}),
    Card(0, 'r', {'w':1, 'r':1, 'a':3}),
    Card(0, 'a', {'g':1, 'r':3, 'a':1}),

    Card(0, 'w', {'b':2, 'g':2, 'a':1}),
    Card(0, 'b', {'w':1, 'g':2, 'r':2}),
    Card(0, 'g', {'b':1, 'r':2, 'a':2}),
    Card(0, 'r', {'w':2, 'g':1, 'a':2}),
    Card(0, 'a', {'w':2, 'b':2, 'r':1}),

    Card(1, 'w', {'g':4}),
    Card(1, 'b', {'r':4}),
    Card(1, 'g', {'a':4}),
    Card(1, 'r', {'w':4}),
    Card(1, 'a', {'b':4})
]

SECOND_CARDS = [
    Card(1, 'w', {'w':2, 'b':3, 'r':3}),
    Card(1, 'b', {'b':2, 'g':3, 'a':3}),
    Card(1, 'g', {'w':3, 'g':2, 'r':3}),
    Card(1, 'r', {'b':3, 'r':2, 'a':3}),
    Card(1, 'a', {'w':3, 'g':3, 'a':2}),
    
    Card(1, 'w', {'g':3, 'r':2, 'a':2}),
    Card(1, 'b', {'b':2, 'g':2, 'r':3}),
    Card(1, 'g', {'w':2, 'b':3, 'a':2}),
    Card(1, 'r', {'w':2, 'r':2, 'a':3}),
    Card(1, 'a', {'w':3, 'b':2, 'g':2}),
    
    Card(2, 'w', {'g':1, 'r':4, 'a':2}),
    Card(2, 'b', {'w':2, 'r':1, 'a':4}),
    Card(2, 'g', {'w':4, 'b':2, 'a':1}),
    Card(2, 'r', {'w':1, 'b':4, 'g':2}),
    Card(2, 'a', {'b':1, 'g':4, 'r':2}),
    
    Card(2, 'w', {'r':5, 'a':3}),
    Card(2, 'b', {'w':5, 'b':3}),
    Card(2, 'g', {'b':5, 'g':3}),
    Card(2, 'r', {'w':3, 'a':5}),
    Card(2, 'a', {'g':5, 'r':3}),
    
    Card(2, 'w', {'r':5}),
    Card(2, 'b', {'b':5}),
    Card(2, 'g', {'g':5}),
    Card(2, 'r', {'a':5}),
    Card(2, 'a', {'w':5}),
    
    Card(3, 'w', {'w':6}),
    Card(3, 'b', {'b':6}),
    Card(3, 'g', {'g':6}),
    Card(3, 'r', {'r':6}),
    Card(3, 'a', {'a':6})
]

THIRD_CARDS = [
    Card(3, 'w', {'b':3, 'g':3, 'r':5, 'a':3}),
    Card(3, 'b', {'w':3, 'g':3, 'r':3, 'a':5}),
    Card(3, 'g', {'w':5, 'b':3, 'r':3, 'a':3}),
    Card(3, 'r', {'w':3, 'b':5, 'g':3, 'a':3}),
    Card(3, 'a', {'w':3, 'b':3, 'g':5, 'r':3}),
    
    Card(4, 'w', {'w':3, 'r':3, 'a':6}),
    Card(4, 'b', {'w':6, 'b':3, 'a':3}),
    Card(4, 'g', {'w':3, 'b':6, 'g':3}),
    Card(4, 'r', {'b':3, 'g':6, 'r':3}),
    Card(4, 'a', {'g':3, 'r':6, 'a':3}),
    
    Card(5, 'w', {'w':3, 'a':7}),
    Card(5, 'b', {'w':7, 'b':3}),
    Card(5, 'g', {'b':7, 'g':3}),
    Card(5, 'r', {'g':7, 'r':3}),
    Card(5, 'a', {'r':7, 'a':3}),
    
    Card(4, 'w', {'a':7}),
    Card(4, 'b', {'w':7}),
    Card(4, 'g', {'b':7}),
    Card(4, 'r', {'g':7}),
    Card(4, 'a', {'r':7})
]

NOBLES = [
    Noble(3, {'g':3, 'b':3, 'w':3}),
    Noble(3, {'g':3, 'b':3, 'r':3}),
    Noble(3, {'a':3, 'r':3, 'w':3}),
    Noble(3, {'a':3, 'r':3, 'g':3}),
    Noble(3, {'a':3, 'b':3, 'w':3}),
    
    Noble(3, {'a':4, 'w':4}),
    Noble(3, {'b':4, 'w':4}),
    Noble(3, {'r':4, 'g':4}),
    Noble(3, {'a':4, 'r':4}),
    Noble(3, {'b':4, 'g':4}),
]

if __name__ == '__main__':
    for card in FIRST_CARDS:
        print(card)
