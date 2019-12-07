#!/usr/bin/python3

def add_gate(gravity_assist, idx1, idx2, idx3):
    gravity_assist[idx3] =  gravity_assist[idx1] + gravity_assist[idx2]


def prod_gate(gravity_assist, idx1, idx2, idx3):
    gravity_assist[idx3] = gravity_assist[idx1] * gravity_assist[idx2]


def exit_gate(gravity_assist):
    print("[*] Found exit opcode, value is : {}".format(gravity_assist[0]))


def load_gravity_assist_program():
    f = open('./input', 'r').read().split(',')
    return [ int(x) for x in f]


def opcode_map(gravity_assist, idx):
    if gravity_assist[idx] == 1 :
        add_gate(gravity_assist, gravity_assist[idx+1], gravity_assist[idx+2], gravity_assist[idx+3])

    elif gravity_assist[idx] == 2: 
        prod_gate(gravity_assist, gravity_assist[idx+1], gravity_assist[idx+2], gravity_assist[idx+3])       

    elif gravity_assist[idx] == 99:    
        exit_gate(gravity_assist)



def main():
    print("[+] Love you, {}".format("Hello World!"))
    gravity_assist = load_gravity_assist_program()
    print(gravity_assist)
    for idx in range(0, len(gravity_assist) - 1, 4):
        print("[+] Parsing opcode: {}".format(gravity_assist[idx]))
        opcode_map(gravity_assist, idx)



if __name__ == "__main__":
    main()