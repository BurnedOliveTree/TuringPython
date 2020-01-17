import os

# MT = (Q = skonczony zbior stanow, Σ = zbior symboli wejsciowych, δ = funkcja przejscia, Γ = alfabet, q0 = stan wejsciowy, B = symbol pusty, F = zbior stanow koncowych) # noqa


class Turing():
    def __init__(self, tape_name="tape.txt", auto_name="automaton.txt"):
        temp = Turing.open_automaton(auto_name)
        self.signs = temp[0]  # list of signs
        self.empty = temp[0][0]  # char of the empty sign
        self.entry = temp[1][0]  # char of the first state
        self.end = temp[1][1:]  # list of the end states
        self.now_state = self.entry
        self.states = [temp[i][0] for i in range(2, len(temp)) if temp[i][0] not in self.end]  # list of states
        self.moves = [[temp[i+2][1+4*j:5+4*j] for j in range(len(self.signs))] for i in range(len(self.states)) if temp[i+2][0] not in self.end]
        temp = Turing.open_tape(tape_name)
        self.tape = [temp[0][i] for i in range(len(temp[0]))]
        self.now_tape = 1

    @staticmethod
    def open_automaton(file_name):
        with open(file_name, 'r') as file:
            label = [Turing.replace(line, '', '/', ',', ';').split() for line in file]
        return label

    @staticmethod
    def open_tape(file_name):
        with open(file_name, 'r') as file:
            tape = [line for line in file]
        return tape

    @staticmethod
    def replace(string, end, *entry):
        for i in range(len(entry)):
            string = string.replace(entry[i], end)
        return string

    def main(self):
        while Turing.move(self):
            os.system('clear')
            print('\n\n      '+' '.join(sims.tape))
            print('\n'+' '*(6+2*self.now_tape)+'^')
            input()

    def move(self):
        if self.now_state in self.end:
            return False
        for i in range(len(self.moves)):
            if self.states[i] == self.now_state:
                current = i
                break
        for i in range(len(self.moves[current])):
            if self.moves[current][i][0] == str(self.tape[self.now_tape]):
                self.tape[self.now_tape] = self.moves[current][i][1]
                self.now_state = self.moves[current][i][2]
                temp = self.moves[current][i][3]
                if temp == 'L':
                    self.now_tape -= 1
                elif temp == 'P':
                    self.now_tape += 1
        return True


if __name__ == "__main__":
    sims = Turing()
    sims.main()
