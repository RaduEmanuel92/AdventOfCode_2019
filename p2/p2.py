#!/usr/bin/python3
import sys 


def add_gate(gravity_mem, idx1, idx2, idx3):
    gravity_mem[idx3] =  gravity_mem[idx1] + gravity_mem[idx2]


def prod_gate(gravity_mem, idx1, idx2, idx3):
    gravity_mem[idx3] = gravity_mem[idx1] * gravity_mem[idx2]


def exit_gate(gravity_mem):
    print("[*] Found exit opcode, value is : {}".format(gravity_mem[0]))
    return gravity_mem[0]


def load_gravity_assist_program():
    f = open('./input', 'r').read().split(',')
    return [ int(x) for x in f]


def execute_instruction(gravity_mem):
    output = -1
    for instruction_pointer in range(0, len(gravity_mem) - 1, 4):
        if gravity_mem[instruction_pointer] == 1 :
            add_gate(gravity_mem, gravity_mem[instruction_pointer+1], gravity_mem[instruction_pointer+2], gravity_mem[instruction_pointer+3])

        elif gravity_mem[instruction_pointer] == 2: 
            prod_gate(gravity_mem, gravity_mem[instruction_pointer+1], gravity_mem[instruction_pointer+2], gravity_mem[instruction_pointer+3])       

        elif gravity_mem[instruction_pointer] == 99:    
            output = exit_gate(gravity_mem)
            break

    return output


def main():
    print("[+] Love you, {}".format("Hello World!"))
    output = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            gravity_assist_mem = load_gravity_assist_program()
            gravity_assist_mem[1] = noun
            gravity_assist_mem[2] = verb
            result =  execute_instruction(gravity_assist_mem)
            if result == output:
                print("[+] Found noun and verb, product: {}".format(str((100* noun)  + verb)))
                return

if __name__ == "__main__":
    main()