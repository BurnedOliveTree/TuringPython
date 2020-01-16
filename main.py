# MT = (Q = skonczony zbior stanow, Σ = zbior symboli wejsciowych, δ = funkcja przejscia, Γ = alfabet, q0 = stan wejsciowy, B = symbol pusty, F = zbior stanow koncowych) # noqa


class State():
    def __init__(self, temp, i, Γ):
        self.name = temp[i+2][0]
        # self.type  # entry, standard, end
        self.transitions = [temp[i+2][1+4*j:5+4*j] for j in range(len(Γ))]


class Turing():
    def __init__(self, tape_name="tape.txt", auto_name="automaton.txt"):
        temp = Turing.open_automaton(auto_name)
        self.signs = temp[0]  # list of signs
        self.empty = temp[0][0]  # char of the empty sign
        self.states = [temp[i][0] for i in range(2, len(temp))]  # list of states
        self.entry = temp[1][0]  # char of the first state
        self.end = temp[1][1:]  # list of the end states
        self.now_state = self.entry
        self.moves = [State(temp, i, self.signs) for i in range(len(self.states)) if temp[i+2][0] not in self.end]
        temp = Turing.open_tape(tape_name)
        self.tape = [temp[0][i] for i in range(len(temp[0]))]
        self.now_tape = 0

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
            pass

    def move(self):
        for i in range(len(self.moves)):
            if self.moves[i].name == self.now_state:
                current = i
                break
        if self.now_state in self.end:
            return False
        for i in range(len(self.moves[current].transitions)):
            if self.moves[current].transitions[i][0] == str(self.tape[self.now_tape]):
                self.tape[self.now_tape] = self.moves[current].transitions[i][1]
                self.now_state = self.moves[current].transitions[i][2]
                temp = self.moves[current].transitions[i][3]
                if temp == 'L':
                    self.now_tape -= 1
                elif temp == 'P':
                    self.now_tape += 1
        return True


if __name__ == "__main__":
    sims = Turing()
    sims.main()
    print(' '.join(sims.tape))
