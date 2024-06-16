# Brainf*ck Interpreter
Simple interpreter written in Python3

### Definition
Brainfuck is a minimalistic esoteric programming language designed by Urban Müller in 1993. It is characterized by its extremely simple syntax and minimalistic set of commands, making it challenging to write programs in but also a fascinating exercise in computational theory. Here are the full details of Brainfuck:

### Syntax and Commands
Brainfuck operates on an array of memory cells, each initially set to zero. It has a simple set of 8 commands, each represented by a single character:

1. **`>`**: Move the memory pointer to the right (increment the pointer).
2. **`<`**: Move the memory pointer to the left (decrement the pointer).
3. **`+`**: Increment the byte at the memory pointer.
4. **`-`**: Decrement the byte at the memory pointer.
5. **`.`**: Output the byte at the memory pointer as a character.
6. **`,`**: Input a character and store it in the byte at the memory pointer.
7. **`[`**: Jump past the matching `]` if the byte at the memory pointer is zero.
8. **`]`**: Jump back to the matching `[` if the byte at the memory pointer is nonzero.

### Memory
- Brainfuck has an array of memory cells, each initially set to zero.
- The number of cells in the array can vary depending on the interpreter, but traditionally it starts at 30,000 cells.
- The cells are accessed by a data pointer that starts at the beginning of the array.

### Execution
- Brainfuck programs start execution from the first command (`>`).
- Commands are executed sequentially unless control flow (`[` and `]`) changes the execution order based on the value of the current memory cell.

### Language Characteristics
- **Minimalistic**: Brainfuck has one of the smallest instruction sets among programming languages.
- **Turing Completeness**: Despite its simplicity, Brainfuck is Turing-complete, meaning it can theoretically compute anything that a Turing machine can.
- **Esoteric**: It is primarily used for educational purposes, code golfing (writing the smallest possible programs), and entertainment rather than practical applications.

### Example Program
Here's an example of a Brainfuck program that prints "Hello World!":

```brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```
Prints "Extended Ascii Chart":
```ASCII CHART EXTENDED
+.[+.]
```
