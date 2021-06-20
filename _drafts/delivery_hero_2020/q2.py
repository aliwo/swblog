

class MachineException(Exception):
    CODE = -1

class OverFlowException(MachineException):
    pass

class UnderFlowException(MachineException):
    pass

class EmptyResultException(MachineException):
    pass

class RunOutOfStackException(MachineException):
    pass


class Machine:
    MIN = 0
    MAX = 2 ** 20 - 1

    def __init__(self):
        '''
        self.COMMANDS 를 만들 때 다음과 같은 경우를 고려했습니다.
            getattr 사용 -> 함수 이름을 command 와 일치 시켜야 함.
            lambda 사용 -> one-liner 로 만들기 어려움.
            {'문자열': 메소드} 의 dict 로 결정
        '''
        self._stack = []
        self.COMMANDS = {
            'POP': self._pop,
            'DUP': self._duplicate,
            '+': self._add,
            '-': self._sub,
        }

    def peek(self):
        if not self._stack:
            raise EmptyResultException()
        return self._stack[-1]

    def execute(self, command):
        if command.isnumeric():
            self._stack.append(int(command))
            return
        if not self._stack:
            raise RunOutOfStackException()
        self.COMMANDS[command]()

    def _pop(self):
        self._check_stack_length(1)
        return self._stack.pop()

    def _duplicate(self):
        self._check_stack_length(1)
        self._stack.append(self._stack[-1])

    def _add(self):
        self._check_stack_length(2)
        self._stack.append(self._stack.pop() + self._stack.pop())
        self._check_over_flow()

    def _sub(self):
        self._check_stack_length(2)
        self._stack.append(self._stack.pop() - self._stack.pop())
        self._check_under_flow()

    def _check_stack_length(self, length):
        if len(self._stack) < length:
            raise RunOutOfStackException()

    def _check_over_flow(self):
        if self._stack[-1] > self.MAX:
            raise OverFlowException()

    def _check_under_flow(self):
        if self._stack[-1] < self.MIN:
            raise UnderFlowException()

def solution(S):
    # write your code in Python 3.6
    commands = S.split()
    machine = Machine()
    try:
        for command in commands:
            machine.execute(command)
        result = machine.peek()
    except MachineException as e:
        return e.CODE
    else:
        return result

# print(solution('13 DUP 4 POP 5 DUP + DUP + -'))
# print(solution('1048575 3 +')) # OverFlow
# print(solution('1 3 POP POP')) # EmptyResult
# print(solution('3 DUP 5 - -')) # UnderFLow
# print(solution('10 10 10')) # 10
print(solution('')) # 10