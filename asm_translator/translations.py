class Translations:
    constant_symbol_table = {
        'SP': 0,
        'LCL': 1,
        'ARG': 2,
        'THIS': 3,
        'THAT': 4,
        'R0': 0,
        'R1': 1,
        'R2': 2,
        'R3': 3,
        'R4': 4,
        'R5': 5,
        'R6': 6,
        'R7': 7,
        'R8': 8,
        'R9': 9,
        'R10': 10,
        'R11': 11,
        'R12': 12,
        'R13': 13,
        'R14': 14,
        'R15': 15,
        'SCREEN': 16384,
        'KBD': 24576   
    }

    dynamic_symbol_table = {}

    alu_commands_a_0 = {
        '0': '101010',
        '1': '111111',
        '-1': '111010',
        'D': '001100',
        'A': '110000',
        '!D': '001101',
        '!A': '110001',
        '-D': '001111',
        '-A': '110011',
        'D+1': '011111',
        'A+1': '110111',
        'D-1': '001110',
        'A-1': '110010',
        'D+A': '000010',
        'D-A': '010011',
        'A-D': '000111',
        'D&A': '000000',
        'D|A': '010101'
    }

    alu_commands_a_1 = {
        'M': '110000',
        '!M': '110001',
        '-M': '110011',
        'M+1': '110111',
        'M-1': '110010',
        'D+M': '000010',
        'D-M': '010011',
        'M-D': '000111',
        'D&M': '000000',
        'D|M': '010101'
    }

    jump_commands = {
        'null': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }

    dest_commands = {
        'null': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }
    
    def __init__(self):
        self.variable_address = 16

    def translate_a_command(self, command) -> str:
        if command[1:].isdigit(): # command is a number, so convert to binary and return
            return self.convert_to_binary(int(command[1:]))
        elif self.constant_symbol_table.get(command[1:]) is not None: # added symbol => either label or variable
            return self.convert_to_binary(self.constant_symbol_table[command[1:]])
        elif self.dynamic_symbol_table.get(command[1:]) is not None:
            return self.convert_to_binary(self.dynamic_symbol_table[command[1:]])
        else:
            self.dynamic_symbol_table[command[1:]] = self.variable_address # add new variable to dynamic symbol table and assign address, then return binary of address
            self.variable_address += 1
            return self.convert_to_binary(self.dynamic_symbol_table[command[1:]])

    def translate_c_command(self, command) -> str: #standard c-instruction translation
        dest, comp, jump = 'null', command, 'null'
        if '=' in command:
            dest, comp = command.split('=')
        if ';' in comp:
            comp, jump = comp.split(';')

        a_bit = '1' if 'M' in comp else '0'
        comp_bits = self.alu_commands_a_1[comp] if a_bit == '1' else self.alu_commands_a_0[comp]

        dest_bits = self.dest_commands[dest]   

        jump_bits = self.jump_commands[jump]

        return '111' + a_bit + comp_bits + dest_bits + jump_bits

    def add_l_command_to_table(self, command, label_address):
        if self.dynamic_symbol_table.get(command[1:-1]) is None: # add label to symbol table with address of next command
            self.dynamic_symbol_table[command[1:-1]] = label_address
    
    def convert_to_binary(self, value):
        return bin(value)[2:].zfill(16)