from asm_translator.code_writer import CodeWriter
from asm_translator.parser import Parser

class ASMTranslator:
    def __init__(self, input_file):
        self.parser = Parser(input_file)
        self.code_writer = CodeWriter(input_file.replace('.asm', '.hack'))
    
    def translate(self):
        self.parse_all_l_commands()

        self.parser.current = -1  # reset parser to start translating commands

        while self.parser.has_more_lines():

            self.parser.advance()

            if self.parser.command_type() == 'A_COMMAND':
                self.code_writer.write_a_command(self.parser.segment())
            elif self.parser.command_type() == 'C_COMMAND': 
                self.code_writer.write_c_command(self.parser.segment())
    
        self.code_writer.close()

    def parse_all_l_commands(self):
        counter = 0
        while self.parser.has_more_lines():
            self.parser.advance()
            if self.parser.command_type() == 'L_COMMAND':
                self.code_writer.add_l_command_to_table(self.parser.segment(), self.parser.current - counter)
                counter += 1 # to adjust for the fact that L_COMMANDs do not generate machine code and thus should not be counted as instructions