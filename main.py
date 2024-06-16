from modules.memory import Memory
from modules.brainf_core import BrainfCore


def main():
    # Modify this later if I decided to add more to this project XD.
    source = input("#")
    pointer = 0
    memory = Memory()
    while pointer < len(source):
        core = BrainfCore(memory)
        optcode = source[pointer]
        output = core.translate_code(optcode, pointer)
        new_pointer = core.pointer
        if output:
            print(output, end="")

        if new_pointer is not None:
            pointer = new_pointer
            continue
        pointer += 1


if __name__ == "__main__":
    print("="*50)
    print("{} BrainFuck Interpreter".format(" "*12))
    print("="*50)

    while True:
        main()