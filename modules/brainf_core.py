class BrainfCore:
    def __init__(self, memory):
        self.__memory = memory
        self.__pointer = None

    @property
    def pointer(self):
        return self.__pointer

    def translate_code(self, optcode, pointer):
        if optcode == "[":
            self.__memory.push_stock(pointer)
        elif optcode == "]" and not self.__memory.get_data:
            # print("MEMORY VALUE IS ZERO: %s" % (self.__memory.get_data))
            self.__memory.pop_stock()
        elif optcode == "]" and self.__memory.get_data:
            # print("MEMORY VALUE IS NOT ZERO: %s" % (self.__memory.get_data))
            new_pointer = self.__memory.pop_stock()
            # print("NEW POINTER: %s OLD: %s" % (new_pointer, self.__pointer))
            self.__pointer = new_pointer
        elif optcode == ">":
            self.__memory.pointer += 1
        elif optcode == "<":
            self.__memory.pointer -= 1
        elif optcode == "+":
            self.__memory.add(1)
        elif optcode == "-":
            self.__memory.subract(1)
        elif optcode == ",":
            self.__memory.add(ord(input))
        elif optcode == ".":
            return chr(self.__memory.get_data)
        return None

