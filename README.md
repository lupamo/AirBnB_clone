# This new Repository contains the files for the Airbnb project

We will be creating an Airbnb clone website.. This is the console

## The cmd

The interpreter uses a loop to read all lines from its input, parse them, and then dispatch the command to an appropriate command handler.
The Cmd class provides a simple framework for writing line-oriented command interpreters. These are often useful for test harnesses,
administrative tools, and prototypes that will later be wrapped in a more sophisticated interface.
An interpreter instance will recognize a command name foo if and only if it has a method do_foo().
cmdloop() is the main processing loop of the interpreter. You can override it, but it is usually not necessary, since the preloop() and postloop() hooks are available.

## The UUID

This module provides immutable UUID objects (the UUID class) and the functions uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5 UUIDs as specified in RFC 4122.
If all you want is a unique ID, you should probably call uuid1() or uuid4(). Note that uuid1() may compromise privacy since it creates a UUID containing the computer’s network address. uuid4() creates a random UUID.
