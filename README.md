# Python Crash Course
Welcome to the non-comprehensive Python crash course! This is intended for students in the CS300 term project group who need some help learning Python before we begin.

Start with [example.py](example.py) and then move on to [my_program.py](my_program.py). Also check out [john_smith.json](john_smith.json) to see what kind of information you'll be loading. If you have any other questions, feel free to ask.

## Infrequently Asked Questions and Statements
### These files are long and scary.
Rest assured that a lot of that length is only whitespace and comments!

### I messed up a bunch of information in John Smith's file! How do I get it back?
Don't panic! Open the command line, `cd` into the project directory, and enter this command:
```bash
git checkout HEAD -- john_smith.json
```
That will reset the file back to the last commit.

### Why can't I edit John Smith's spouse and children, but I can change his marital status?
Jane Smith and their children are entirely different people. In an ideal situation, we would have separate files on all of them and connect them via numeric IDs or another unique identifier. As it is, we're just going to prevent editing them and pretend that they're stored in separate files.
