class Parser:
    def __init__(self, filename):
        self.commands = []
        self.current = -1
        
        with open(filename, 'r') as f:
            for line in f.readlines():
                # remove comments and whitespace
                line = line.split('//')[0].strip()
                # skip empty lines
                if line:
                    self.commands.append(line)
    
    def has_more_lines(self):
        return self.current < len(self.commands) - 1
    
    def advance(self):
        self.current += 1
        return self.commands[self.current]
    
    def command_type(self):
        cmd = self.commands[self.current]
        if cmd[0] == '@':
            return 'A_COMMAND'
        elif cmd.startswith('(') and cmd.endswith(')'):
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'
    
    def segment(self):
        return self.commands[self.current]