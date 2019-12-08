#!/usr/bin/python3

# Global front panel hash
front_panel = {}
signal1 = 0 
signal2 = 0
wire1 = {}
wire2 = {}

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    

def read_wires():
    return [ wire.strip('\n') for wire in open('./input', 'r').readlines() ]


def taint_panel(coordinate, id_w):
    global front_panel

    # for each wire, check whether the wire didn't cross himself
    if id_w == 'w1': 
        if (coordinate not in front_panel.keys()): 
            front_panel[coordinate] = 'w1'
        elif (coordinate in front_panel.keys())  and (front_panel[coordinate] == 'w2'):
            front_panel[coordinate] = 'w1w2'
    else: 
        if (coordinate not in front_panel.keys()) :
            front_panel[coordinate] = 'w2'
        elif (coordinate in front_panel.keys()) and (front_panel[coordinate] == 'w1'):
            front_panel[coordinate] = 'w1w2'


def report_signal(coordinate, id_w):
    global wire1, wire2
    global signal1, signal2

    if id_w == 'w1':
        wire1[coordinate] = signal1
    else:         
        wire2[coordinate] = signal2


def increase_signal(idw):
    global signal1, signal2
    if idw == "w1":
        signal1 += 1
    else:
        signal2 += 1


def mark_segment(curent_pos, segment, id_w):
    # draw current segment starting from the last found point
    direction = segment[0]
    length = int(''.join(segment[1:]))

    if direction == 'L':
        for unit in range(length):
            increase_signal(id_w)
            current_position = Coordinate(curent_pos.getX() - unit, curent_pos.getY())
            # Taint current position as part of the wire
            taint_panel(str(current_position), id_w)
            report_signal(str(current_position), id_w)
        # Correct last_pos    
        curent_pos.x -= length    

    elif direction == 'R':
        for unit in range(length):
            increase_signal(id_w)
            current_position = Coordinate(curent_pos.getX() + unit, curent_pos.getY())
            # Taint current position as part of the wire
            taint_panel(str(current_position), id_w)
            report_signal(str(current_position), id_w)
        # Correct last_pos    
        curent_pos.x += length 

    elif direction == 'U':
        for unit in range(length):
            increase_signal(id_w)
            current_position = Coordinate(curent_pos.getX(), curent_pos.getY() + unit)
            # Taint current position as part of the wire
            taint_panel(str(current_position), id_w)
            report_signal(str(current_position), id_w)
        # Correct last_pos    
        curent_pos.y += length 

    elif direction == 'D':
        for unit in range(length):
            increase_signal(id_w)
            current_position = Coordinate(curent_pos.getX(), curent_pos.getY() - unit)
            # Taint current position as part of the wire
            taint_panel(str(current_position), id_w)
            report_signal(str(current_position), id_w)
        # Correct last_pos    
        curent_pos.y -= length 


def draw(wire, id_w):
    # Reset current_pos when drawing new wire
    curent_pos = Coordinate(0, 0)
    for segment in wire.split(','):
        mark_segment(curent_pos,segment, id_w)


def intersect(panel):
    distances = []
    min_signals = []

    # Delete origin point which does not represent an intersection
    del panel[str(Coordinate(0, 0))]
    for key, val in panel.items():
        if val == 'w1w2':
            # Decrease two steps who are counted twice (original position and intersection point)
            min_signals.append( wire1[key] + wire2[key] - 2 )
            # Extract keys and compute Hamming distance
            coord_intesect = key.strip('\<\>').split(',')
            distances.append(abs(int(coord_intesect[0])) + abs(int(coord_intesect[1])))

    print("[+] Manhattan distance from the central port to the closest intersection is: {}".format(min(distances)))
    print("[+] Number of the fewest combined steps the wires must take to reach an intersection is: {}".format(min(min_signals)))        


def main():
    wires = read_wires()
    draw(wires[1], "w1")
    draw(wires[0], "w2")
    intersect(front_panel)


if __name__ == "__main__":
    main()
