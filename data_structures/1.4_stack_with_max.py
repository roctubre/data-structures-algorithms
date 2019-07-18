#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__maxidx = []

    def Push(self, a):
        self.__stack.append(a)
        
        if not self.__maxidx or a >= self.__stack[self.__maxidx[-1]]:
            self.__maxidx.append(len(self.__stack)-1)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        if self.__maxidx[-1] == len(self.__stack):
            self.__maxidx.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__stack[self.__maxidx[-1]]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
