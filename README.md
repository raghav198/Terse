Terse
=====
Interpreter for the esoteric "Terse" programming 

<h3>Using Terse</h3>

The Terse interpreter comes in two different versions: open source and closed source. Both versions are free. To begin writing Terse programs, follow these steps:

1. Choose which interpreter you want to use

    The open source interpreter allows you to modify the language and contribute features, but it requires Python2.7 in 
    order to run. It is slightly slower than the closed source version. It can be used on any platform (Windows, Linux,       and MacOS)
    
    The closed source interpreter does not allow for any modifications, and comes in the form of a Windows .exe executable
    file. Although it runs faster than the open source, there are currently no versions for any OS other than Windows.
    
2. Download the relevant files for the interpreter that you chose and unzip them into a convenient directory.
3. To use the open source interpreter, run <code>python terse.py</code> at the command prompt. To use the closed source interpreter, simply run the <code>terse.exe</code> executable. The program will prompt you for the filename if none is specified, and it will then execute the code contained in the file. For example, to run <code>my_first_script.trs</code> with the open source interpreter:
<pre>
    python terse.py
    Filename? .trs
    Hello, world!
</pre>
You can also specify the filename as a command-line parameter to avoid this extra step. For example, the previous two steps could have been performed like this:
<pre>
    python terse.py my_first_script.trs
    Hello, world!
</pre>

<h3>Writing Terse</h3>
OK, you know how to run Terse source files. But what about writing them? You can see some sample programs and language references in the <code>/tutorial</code> directory of your Terse installation, 
