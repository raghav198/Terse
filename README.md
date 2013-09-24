Terse
=====

Interpreter for the esoteric "Terse" programming language

Instructions:

The Terse interpreter is very simply to use! Just download the .zip file containing the interpreter and create a .trs Terse
source file. Run "python terse.py" and type the file name (ending with .trs) at the prompt and your program will be 
executed! Writing the source file is probably the hardest part. 


Terse Instructions
==================

Terse is a very small interpreted language whose syntax resembles that of assembly. There are no datatypes, but types are inferred from usage (i.e., during addition integer or float is inferred)
A Terse program consists of lines that each contain two columns: the command and the arguments.

example:
    command    arg1 arg2 arg3 (etc.)

the command is followed by a tab ("\t") and the arguments are separated by spaces

the most basic command is "out", which prints to stdout:

    out    "Hello world!"
prints "Hello world!" to the standard output

the "in" command reads a line from stdin:

    out    in

would duplicate whatever the user typed at the prompt.

variables are declared using the "decl" keyword. New variables are preceded with an ampersand ("&") whereas global variables being accessed are preceded with "@". Local variables are preceded with "$". Variables are by default global.

To set a variable, type the variable name as a command and pass a value as an argument:

    decl    &name
    @name   "Tim"
    out     @name

would print "Tim"


functions are declared with the "func" keyword, which is in itself a function. The first argument is the name, and any other arguments are parameters. Any lines following the "func" but before "end" are part of the function block. All parameters are local variables.

    func    greet &name
    out     "Hello " $name "!"
    end
    greet   "Tim"

prints "Hello, Tim!" to the console.
This also demonstrates string interpolation.

Comments must always appear at the beginning of the line, and last throughout the line. Comments are delimited by a semicolon (";")

Terse also has a simple "stack" which is very useful when doing mathematics. Use "push" and "pop" to deal with the stack:

    add   1 2
    push
    out   pop

prints "3" to the console (1 and 2 are added, the result is pushed to the stack, and the "out" command is passed the first value from the stack. "3" is now removed from the stack after being printed.)

Unlike many traditional languages, there is no "if" statement in Terse: the conditional is simply interpreted. To execute a conditional, one of 5 comparison commands are used, and given two values as arguments. Any commands after such a line and before the "end" are part of the conditional block, and are executed only if the first statement evaluates to "+", one of two "boolean" values in Terse (the other being, of course, "-")

example:

    decl    &age
    out     "How old are you? "
    @age    in
    gt      age 18
    out     "You are at least 19 years old!"
    end
    le      age 18
    out     "You are under 19 years old!"
    end

The program would prompt the user for their age, and print out whether the user is at least 19. Note that there is no equivalent of an "else" statement in Terse.

The comparison operators include:
    lt (<)
    gt (>)
    le (<=)
    ge (>=)
    eq (==)


This description can also be found at http://www.esolangs.org/wiki/Terse
