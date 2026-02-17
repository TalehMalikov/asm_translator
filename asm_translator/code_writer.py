from asm_translator.translations import Translations

class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.translations = Translations()
    
    def add_l_command_to_table(self, cmd, label_address):
        self.translations.add_l_command_to_table(cmd, label_address)

    def write_a_command(self, cmd):
        hack = self.translations.translate_a_command(cmd)
        self.file.write(hack + '\n')

    def write_c_command(self, segment):
        hack = self.translations.translate_c_command(segment)
        self.file.write(hack + '\n')

    def write_back(self, hack):
        self.file.write(hack + '\n')

    def close(self):
        self.file.close()