# memory.py

from dataclasses import dataclass, field
from numpy import array, uint8


@dataclass
class Memory:
    __memory: array = field(
        init=False, default_factory=lambda: array([0] * 30000, dtype=uint8)
    )
    __stock: list[int] = field(init=False, default_factory=list)
    __pointer: int = field(init=False, default=0)

    @property
    def get_data(self):
        return self.__memory[self.__pointer]

    @property
    def stock(self):
        return self.__stock[-1] if self.__stock else None

    @property
    def pointer(self):
        return self.__pointer

    @pointer.setter
    def pointer(self, value):
        pointer_limit = 30000
        self.__pointer = value
        new_pointer = self.__pointer
        if new_pointer > pointer_limit - 1:
            new_pointer = 0
        elif new_pointer < -pointer_limit:
            new_pointer = 0

        self.__pointer = new_pointer

    def add(self, value):
        self.__memory[self.__pointer] += value

    def subract(self, value):
        self.__memory[self.__pointer] -= value

    def push_stock(self, value):
        self.__stock.append(value)

    def pop_stock(self):
        return self.__stock.pop() if self.__stock else None

    def view_memory(self, start=False, end=False):
        return self.__view(self.__memory, start, end)

    def view_stock(self, start=False, end=False):
        return self.__view(self.__stock, start, end)

    def __view(self, data, start, end):
        new_data = data
        if start and end:
            new_data = new_data[start:end]
        elif start:
            new_data = new_data[start:]
        elif end:
            new_data = new_data[:end]
        return new_data


def test():
    mem = Memory()
    mem = Memory()
    print(f"Current Memory {mem.get_data}")
    mem.add(10)
    print(f"Current Memory {mem.get_data}")
    mem.pointer = 1
    print(f"Current Memory {mem.get_data}")
    print(f"Pointer {mem.pointer}")
    print(f"View Memory {mem.view_memory(end=10)}")
    mem.add(20)
    print(f"Current Memory {mem.get_data}")
    print(f"Pointer {mem.pointer}")
    print(f"View Memory {mem.view_memory(end=10)}")
    mem.pointer = -10
    mem.add(30)
    print(f"Current Memory {mem.get_data}")
    print(f"Pointer {mem.pointer}")
    print(f"View Memory {mem.view_memory(start= -10)}")
    mem.pointer = 30010
    mem.add(50)
    print(f"Current Memory {mem.get_data}")
    print(f"Pointer {mem.pointer}")
    print(f"View Memory {mem.view_memory(end=20)}")


if __name__ == "__main__":
    test()
