from interfaces.output import OutputInterface


class ConsoleOutput(OutputInterface):
    def write(self, data):
        print(data, end='')

