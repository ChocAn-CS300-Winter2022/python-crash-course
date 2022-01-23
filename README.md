# Python Crash Course
Welcome to the non-comprehensive Python crash course! This is intended for students in the CS300 term project group who need some help learning Python before we begin.

Start with [example.py](example.py) for basic Python syntax as well as reading and writing to text files, then move on to [my_program.py](my_program.py) for JSON examples and data manipulation. Also check out [john_smith.json](john_smith.json) and [lorem_ipsum.txt](lorem_ipsum.txt) to see what kind of information you'll be loading. If you have any other questions, feel free to ask.

## A word of caution
Now that `example.py` reads and writes to a file, be careful! Don't enter any files that you don't want to lose data in, because they will likely be overwritten, even if you cancel the program (read the comments in the `write_file()` function in `example.py`).

## Infrequently Asked Questions and Statements
### These files are long and scary.
Rest assured that a lot of that length is only whitespace and comments!

### I messed up a bunch of information in John Smith's file! How do I get it back?
Don't panic! Open the command line, `cd` into the project directory, and enter this command:
```bash
git checkout HEAD -- john_smith.json
```
That will reset the file back to the last commit. The same concept applies to `lorem_ipsum.txt`.

### Why can't I edit John Smith's spouse and children, but I can change his marital status?
Jane Smith and their children are entirely different people. In an ideal situation, we would have separate files on all of them and connect them via numeric IDs or another unique identifier. As it is, we're just going to prevent editing them and pretend that they're stored in separate files.
