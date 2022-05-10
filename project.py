"""
python dictionary have alot of dictionaries
to help programmers to search for specific concepts
"""


def main():
    general_search=0
    while general_search!=-1:
        general_search=int(input('type -1 to stop\n 1-show all references \n 2-for general search: '))
        if general_search==1:
            searchh()
        elif general_search!=1:
            general_search = input('TYPE WHAT YOU SEARCH FOR IN GENERAL HERE: ')
            all(general_search)






        #search function
def searchh():
    search = 0
    print("(ADD '-1' TO STOP)")
    while (search != -1):
        if search==-1:
            break
        search = int(input(
            '(CHOOSE NUMBER TO SEARCH FOR) \n 1-syntax \n 2-functions \n 3-key words \n 4-string methods \n 5-lists and array methods '
            '\n 6-dictionary methods \n 7-tuple \n 8-set \n 9-file methods \n 10-built in exceptions \n 11-data types: \n '))
        if search == 1:
            search = (input('syntax: '))
            syntax(search)
        elif search == 2:
            search = (input('fuctions: '))
            functions_dict(search)
        elif search == 3:
            search = (input('key words: '))
            key_word_dict(search)
        elif search == 4:
            search = (input('string : '))
            string_method(search)
        elif search == 5:
            search = (input('lists and array : '))
            list_method(search)
        elif search == 6:
            search = (input('dictionary : '))
            dict(search)
        elif search == 7:
            search = (input('tuple: '))
            tuple(search)
        elif search == 8:
            search = (input('set method: '))
            set(search)
        elif search == 9:
            search = (input('file method: '))
            file(search)
        elif search == 10:
            print("capitalize first letter")
            search = (input('built in exceptions: '))
            builtin_Except(search)
        elif search == 11:
            search = (input('data types: '))
            data_types(search)


def all(general_search):
    all_dict={'indentation' :'Indentation refers to the spaces at the beginning of a code line.',
              'variables' :'Variables are containers for storing data values.',
              'global Variables' : 'Variables that are created outside of a function (as in all of the examples above) are known as global variables.Global variables can be used by everyone, both inside of functions and outside',
              'comments':' Comments are code lines that will not be executed',
              'multi Line Comments':'How to insert comments on multiple lines',
              'text': 'str',
              'numeric': 'int, float, complex',
              'sequence': 'list, tuple, range',
              'mapping': 'dict',
              'set': 'set, frozenset',
              'boolean': 'bool',
              'binary': 'bytes, bytearray, memoryview',
              'add': '  	Adds an element to the set',
              'clear  ': '	Removes all the elements from the set',
              'copy': '  	Returns a copy of the set',
              'difference': 'Returns a set containing the difference between two or more sets',
              'difference_update ': 'Removes the items in this set that are also included in another, specified set',
              'discard': 'Remove the specified item',
              'intersection ': 'Returns a set, that is the intersection of two other sets',
              'intersection_update ': ' Removes the items in this set that are not present in other, specified set s',
              'isdisjoint ': 'Returns whether two sets have a intersection or not',
              'issubset ': ' 	Returns whether another set contains this set or not',
              'issuperset  ': '	Returns whether this set contains another set or not',
              'pop': ' 	Removes an element from the set',
              'remove': '  Removes the specified element',
              'symmetric_difference ': '	Returns a set with the symmetric differences of two sets',
              'symmetric_difference_update': '  	inserts the symmetric differences from this set and another',
              'union  ': '	Return a set containing the union of sets',
              'update': ' 	Update the set with the union of this set and others',
              'count': 'Returns the number of times a specified value occurs in a tuple',
              'index': 'Searches the tuple for a specified value and returns the position of where it was found',
              'abs': 'Returns the absolute value of a number',
              'all': 'Returns True if all items in an iterable object are true',
              'any': 'Returns True if any item in an iterable object is true',
              'ascii': 'Returns a readable version of an object. Replaces none-ascii characters with escape character',
              'bin': 'Returns the binary version of a number',
              'bool': 'Returns the boolean value of the specified object',
              'bytearray': 'Returns an array of bytes',
              'bytes': 'Returns a bytes object',
              'callable': 'Returns True if the specified object is callable, otherwise False',
              'chr': 'Returns a character from the specified Unicode code.',
              'classmethod': 'Converts a method into a class method',
              'compile': 'Returns the specified source as an object, ready to be executed',
              'complex': 'Returns a complex number',
              'delattr': 'Deletes the specified attribute (property or method) from the specified object',
              'dict': 'Returns a dictionary (Array)',
              'dir': 'Returns a list of the specified objects properties and methods',
              'divmod': 'Returns the quotient and the remainder when argument1 is divided by argument2',
              'enumerate': 'Takes a collection (e.g. a tuple) and returns it as an enumerate object',
              'eval': 'Evaluates and executes an expression',
              'exec': 'Executes the specified code (or object)',
              'filter': 'Use a filter function to exclude items in an iterable object',
              'float': 'Returns a floating point number',
              'format': 'Formats a specified value',
              'frozenset': 'Returns a frozenset object',
              'getattr': 'Returns the value of the specified attribute (property or method)',
              'globals': 'Returns the current global symbol table as a dictionary',
              'hasattr': 'Returns True if the specified object has the specified attribute (property/method)',
              'hash': 'Returns the hash value of a specified object',
              'help': 'Executes the built-in help system',
              'hex': 'Converts a number into a hexadecimal value',
              'id': 'Returns the id of an object',
              'input': 'Allowing user input',
              'int': 'Returns an integer number',
              'isinstance': 'Returns True if a specified object is an instance of a specified object',
              'issubclass': 'Returns True if a specified class is a subclass of a specified object',
              'iter': 'Returns an iterator object',
              'len': 'Returns the length of an object',
              'list': 'Returns a list',
              'locals': 'Returns an updated dictionary of the current local symbol table',
              'map': 'Returns the specified iterator with the specified function applied to each item',
              'max': 'Returns the largest item in an iterable',
              'memoryview': 'Returns a memory view object',
              'min': 'Returns the smallest item in an iterable',
              'next': 'Returns the next item in an iterable',
              'object': 'Returns a new object',
              'oct': 'Converts a number into an octal',
              'open': 'Opens a file and returns a file object',
              'ord': 'Convert an integer representing the Unicode of the specified character',
              'pow': 'Returns the value of x to the power of y',
              'print': 'Prints to the standard output device',
              'property': 'Gets, sets, deletes a property',
              'range': 'Returns a sequence of numbers, starting from 0 and increments by 1 (by default)',
              'repr': 'Returns a readable version of an object',
              'reversed': 'Returns a reversed iterator',
              'round': 'Rounds a numbers',
              'set': 'Returns a new set object',
              'setattr': 'Sets an attribute (property/method) of an object',
              'slice': 'Returns a slice object',
              'sorted': 'Returns a sorted list',
              '@staticmethod': 'Converts a method into a static method',
              'str': 'Returns a string object',
              'sum': 'Sums the items of an iterator',
              'super': 'Returns an object that represents the parent class',
              'tuple': 'Returns a tuple',
              'type': 'Returns the type of an object',
              'vars': 'Returns the __dict__ property of an object',
              'zip': 'Returns an iterator, from two or more iterators',
              'false': 'True and False are truth values in Python. They are the results of comparison operations or logical (Boolean) operations in Python',
              'await': 'The async and await keywords are provided by the asyncio library in Python. They are used to write concurrent code in Python',
              'async': 'The async and await keywords are provided by the asyncio library in Python. They are used to write concurrent code in Python',
              'none': 'None is a special constant in Python that represents the absence of a value or a null value.It is an object of its own datatype, the NoneType. We cannot create multiple None objects but can assign it to variables. These variables will be equal to one another.We must take special care that None does not imply False, 0 or any empty list, dictionary, string etc.',
              'and': 'and, or, not are the logical operators in Python.',
              'or': 'and, or, not are the logical operators in Python.',
              'class': 'class is used to define a new user-defined class in Python.Class is a collection of related attributes and methods that try to represent a real world situation. This idea of putting data and functions together in a class is central to the concept of object-oriented programming (OOP).Classes can be defined anywhere in a program. But it is a good practice to define a single class in a module.',
              'def': 'used to define a user-defined function.Function is a block of related statements, which together does some specific task. It helps us organize code into manageable chunks and also to do some repetitive task.',
              'del': 'del is used to delete the reference to an object. Everything is object in Python. We can delete a variable reference using del',
              'if': 'if, else, elif are used for conditional branching or decision making.When we want to test some condition and execute a block only if the condition is true, then we use if and elif. elif is short for else if. else is the block which is executed if the condition is false',
              'elif': 'if, else, elif are used for conditional branching or decision making.When we want to test some condition and execute a block only if the condition is true, then we use if and elif. elif is short for else if. else is the block which is executed if the condition is false',
              'raise': 'except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.',
              'try': 'except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.',
              'except': 'except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.',
              'else': 'if, else, elif are used for conditional branching or decision making.When we want to test some condition and execute a block only if the condition is true, then we use if and elif. elif is short for else if. else is the block which is executed if the condition is false',
              'in': 'in is used to test if a sequence (list, tuple, string etc.) contains a value. It returns True if the value is present, else it returns False',
              'is': 'is used in Python for testing object identity. While the == operator is used to test if two variables are equal or not, is is used to test if the two variables refer to the same object.',
              'lambda': 'lambda is used to create an anonymous function (function with no name). It is an inline function that does not contain a return statement. It consists of an expression that is evaluated and returned.',
              'nonlocal': 'The use of nonlocal keyword is very much similar to the global keyword. nonlocal is used to declare that a variable inside a nested function (function inside a function) is not local to it, meaning it lies in the outer inclosing function. If we need to modify the value of a non-local variable inside a nested function, then we must declare it with nonlocal. Otherwise a local variable with that name is created inside the nested function',
              'pass': 'pass is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder.',
              'return': 'return statement is used inside a function to exit it and return a value.If we do not return a value explicitly, None is returned automatically. ',
              'while': 'used for looping in Python.The statements inside a while loop continue to execute until the condition for the while loop evaluates to False or a break statement is encountered.',
              'with': 'with statement is used to wrap the execution of a block of code within methods defined by the context manager.Context manager is a class that implements __enter__ and __exit__ methods. Use of with statement ensures that the __exit__ method is called at the end of the nested block. This concept is similar to the use of try…finally block.',
              'yield': 'yield is used inside a function like a return statement. But yield returns a generator.Generator is an iterator that generates one item at a time. A large list of value will take up a lot of memory. Generators are useful in this situation as it generates only one value at a time instead of storing all the values in memory. ',
              'not': 'and, or, not are the logical operators in Python.',
              'finally': 'finally is used with try…except block to close up resources or file streams.Using finally ensures that the block of code inside it gets executed even if there is an unhandled exception',
              'import': 'from, import keyword is used to import modules into the current namespace. from…import is used to import specific attributes or functions into the current namespace.',
              'from': 'from, import keyword is used to import modules into the current namespace. from…import is used to import specific attributes or functions into the current namespace.',
              'global': 'global is used to declare that a variable inside the function is global (outside the function).If we need to read the value of a global variable, it is not necessary to define it as global. This is understood.If we need to modify the value of a global variable inside a function, then we must declare it with global. Otherwise a local variable with that name is created.',
              'for': 'for is used for looping. Generally we use for when we know the number of times we want to loop.',
              'as': 'as is used to create an alias while importing a module. It means giving a different name (user-defined) to a module while importing it.',
              'assert': 'assert is used for debugging purposes.While programming, sometimes we wish to know the internal state or check if our assumptions are true. assert helps us do this and find bugs more conveniently. assert is followed by a condition.If the condition is true, nothing happens. But if the condition is false, AssertionError is raised.',
              'break': 'are used inside for and while loops to alter their normal behavior.break will end the smallest loop it is in and control flows to the statement immediately below the loop. continue causes to end the current iteration of the loop, but not the whole loop.',
              'continue': 'are used inside for and while loops to alter their normal behavior.break will end the smallest loop it is in and control flows to the statement immediately below the loop. continue causes to end the current iteration of the loop, but not the whole loop.',
              'capitalize': 'Converts the first character to upper case',
              'casefold': 'Converts string into lower case',
              'center': 'Returns a centered string',
              'count': 'Returns the number of times a specified value occurs in a string',
              'encode': 'Returns an encoded version of the string',
              'endswith': 'Returns true if the string ends with the specified value',
              'expandtabs': 'Sets the tab size of the string',
              'find': 'Searches the string for a specified value and returns the position of where it was found',
              'format': 'Formats specified values in a string',
              'format_map': 'Formats specified values in a string',
              'index': 'Searches the string for a specified value and returns the position of where it was found',
              'isalnum': 'Returns True if all characters in the string are alphanumeric',
              'isalpha': 'Returns True if all characters in the string are in the alphabet',
              'isdecimal': 'Returns True if all characters in the string are decimals',
              'isdigit': 'Returns True if all characters in the string are digits',
              'isidentifier': 'Returns True if the string is an identifier',
              'islower': 'Returns True if all characters in the string are lower case',
              'isnumeric': 'Returns True if all characters in the string are numeric',
              'isprintable': 'Returns True if all characters in the string are printable',
              'isspace': 'Returns True if all characters in the string are whitespaces',
              'istitle': 'Returns True if the string follows the rules of a title',
              'isupper': 'Returns True if all characters in the string are upper case',
              'join': 'Joins the elements of an iterable to the end of the string',
              'ljust': 'Returns a left justified version of the string',
              'lower': 'Converts a string into lower case',
              'lstrip': 'Returns a left trim version of the string',
              'maketrans': 'Returns a translation table to be used in translations',
              'partition': 'Returns a tuple where the string is parted into three parts',
              'replace': 'Returns a string where a specified value is replaced with a specified value',
              'rfind': 'Searches the string for a specified value and returns the last position of where it was found',
              'rindex': 'Searches the string for a specified value and returns the last position of where it was found',
              'rjust': 'Returns a right justified version of the string',
              'rpartition': 'Returns a tuple where the string is parted into three parts',
              'rsplit': 'Splits the string at the specified separator, and returns a list',
              'rstrip': 'Returns a right trim version of the string',
              'split': 'Splits the string at the specified separator, and returns a list',
              'splitlines': 'Splits the string at line breaks and returns a list',
              'startswith': 'Returns true if the string starts with the specified value',
              'strip': 'Returns a trimmed version of the string',
              'swapcase': 'Swaps cases, lower case becomes upper case and vice versa',
              'title': 'Converts the first character of each word to upper case',
              'translate': 'Returns a translated string',
              'upper': 'Converts a string into upper case',
              'zfill': 'Fills the string with a specified number of 0 values at the beginning',
              'append': 'Adds an element at the end of the list',
              'clear': 'Removes all the elements from the list',
              'copy': 'Returns a copy of the list',
              'count': 'Returns the number of elements with the specified value',
              'extend': 'Add the elements of a list (or any iterable), to the end of the current list',
              'index': 'Returns the index of the first element with the specified value',
              'insert': 'Adds an element at the specified position',
              'pop': 'Removes the element at the specified position',
              'remove': 'Removes the first item with the specified value',
              'reverse': 'Reverses the order of the list',
              'sort': 'Sorts the list',
              'clear': 'Removes all the elements from the list',
              'copy': 'Returns a copy of the list',
              'count': 'Returns the number of elements with the specified value',
              'extend': 'Add the elements of a list (or any iterable), to the end of the current list',
              'index': 'Returns the index of the first element with the specified value',
              'insert': 'Adds an element at the specified position',
              'pop': 'Removes the element at the specified position',
              'remove': 'Removes the first item with the specified value',
              'reverse': 'Reverses the order of the list',
              'sort': 'Sorts the list',
              'clear': 'Removes all the elements from the dictionary',
              'copy': 'Returns a copy of the dictionary',
              'fromkeys': 'Returns a dictionary with the specified keys and value',
              'get': 'Returns the value of the specified key',
              'items': 'Returns a list containing a tuple for each key value pair',
              'keys': 'Returns a list containing the dictionarys keys',
              'pop': 'Removes the element with the specified key',
              'popitem': 'Removes the last inserted key-value pair',
              'setdefault': 'Returns the value of the specified key. If the key does not exist: insert the key, with the specified value',
              'update': 'Updates the dictionary with the specified key-value pairs',
              'values': 'Returns a list of all the values in the dictionary',
              'close': '	Closes the file',
              'detach ': '	Returns the separated raw stream from the buffer',
              'fileno': '	Returns a number that represents the stream, from the operating systems perspective',
              'flush ': '	Flushes the internal buffer',
              'isatty ': '	Returns whether the file stream is interactive or not',
              'read ': ' 	Returns the file content',
              'readable ': ' 	Returns whether the file stream can be read or not',
              'readline ': ' 	Returns one line from the file',
              'readlines ': '	Returns a list of lines from the file',
              'seek ': ' 	Change the file position',
              'seekable ': ' 	Returns whether the file allows us to change the file position',
              'tell ': ' 	Returns the current file position',
              'truncate ': ' 	Resizes the file to a specified size',
              'writeable ': '	Returns whether the file can be written to or not',
              'write ': '	Writes the specified string to the file',
              'writelines ': '	Writes a list of strings to the file',
              'ArithmeticError': '  Raised when an error occurs in numeric calculations',
              'AssertionError': '  Raised when an assert statement fails',
              'AttributeError ': ' Raised when attribute reference or assignment fails',
              'Exception': '  Base class for all exceptions',
              'EOFError': '  Raised when the input     method hits an   end of file   condition   EOF',
              'FloatingPointError': '  Raised when a floating point calculation fails',
              'GeneratorExit ': ' Raised when a generator is closed   with the close     method',
              'ImportError ': '  Raised when an imported module does not exist',
              'IndentationError ': '  Raised when indendation is not correct',
              'IndexError ': ' Raised when an index of a sequence does not exist',
              'KeyError ': ' Raised when a key does not exist in a dictionary',
              'KeyboardInterrupt ': '  Raised when the user presses Ctrl  c   Ctrl  z or Delete',
              'LookupError ': '  Raised when errors raised cant be found',
              'MemoryError ': ' Raised when a program runs out of memory',
              'NameError ': ' Raised when a variable does not exist',
              'NotImplementedError ': '  Raised when an abstract method requires an inherited class to override the method',
              'OSError ': ' Raised when a system related operation causes an error',
              'OverflowError ': ' Raised when the result of a numeric calculation is too large',
              'ReferenceError ': ' Raised when a weak reference object does not exist',
              'RuntimeError ': ' Raised when an error occurs that do not belong to any specific expections',
              'StopIteration ': ' Raised when the next     method of an iterator has no further values',
              'SyntaxError ': ' Raised when a syntax error occurs',
              'TabError ': ' Raised when indentation consists of tabs or spaces',
              'SystemError ': ' Raised when a system error occurs',
              'SystemExit ': ' Raised when the sys  exit     function is called',
              'TypeError ': '  Raised when two different types are combined',
              'UnboundLocalError ': ' Raised when a local variable is referenced before assignment',
              'UnicodeError ': ' Raised when a unicode problem occurs',
              'UnicodeEncodeError ': ' Raised when a unicode encoding problem occurs',
              'UnicodeDecodeError ': ' Raised when a unicode decoding problem occurs',
              'UnicodeTranslateError ': '  Raised when a unicode translation problem occurs',
              'ValueError ': ' Raised when there is a wrong value in a specified data type',
              'ZeroDivisionError ': ' Raised when the second operator in a division is zero'}
    keyy = all_dict[general_search]
    print(str(keyy))

def syntax(search):
    syntax={'indentation' :'Indentation refers to the spaces at the beginning of a code line.',
            'variables' :'Variables are containers for storing data values.',
            'global Variables' : 'Variables that are created outside of a function (as in all of the examples above) are known as global variables.Global variables can be used by everyone, both inside of functions and outside',
            'comments':' Comments are code lines that will not be executed',
            'multi Line Comments':'How to insert comments on multiple lines'

            }
    keyy=syntax[search]
    print(str(keyy))
def data_types(search):
    data_types={'text':	'str',
                'numeric':	'int, float, complex',
                'sequence':	'list, tuple, range',
                'mapping':'dict',
                'set':'set, frozenset',
                'boolean':'bool',
                'binary':'bytes, bytearray, memoryview'}
    keyy = data_types[search]
    print(str(keyy))

def set():
    set={'add':'  	Adds an element to the set',
         'clear  ':'	Removes all the elements from the set',
         'copy':'  	Returns a copy of the set',
         'difference' :'Returns a set containing the difference between two or more sets',
         'difference_update ': 'Removes the items in this set that are also included in another, specified set',
         'discard': 'Remove the specified item',
         'intersection ': 'Returns a set, that is the intersection of two other sets',
         'intersection_update ':' Removes the items in this set that are not present in other, specified set s',
         'isdisjoint ':'Returns whether two sets have a intersection or not',
         'issubset ':' 	Returns whether another set contains this set or not',
         'issuperset  ':'	Returns whether this set contains another set or not',
         'pop':' 	Removes an element from the set',
         'remove':'  Removes the specified element',
         'symmetric_difference ':'	Returns a set with the symmetric differences of two sets',
         'symmetric_difference_update':'  	inserts the symmetric differences from this set and another',
         'union  ':'	Return a set containing the union of sets',
         'update':' 	Update the set with the union of this set and others'}
    keyy = set[search]
    print(str(keyy))


def tuple(search):
    tuple={'count':'Returns the number of times a specified value occurs in a tuple',
           'index':'Searches the tuple for a specified value and returns the position of where it was found'}
    keyy = tuple[search]
    print(str(keyy))





def functions_dict(search):
    functionss={'abs' : 'Returns the absolute value of a number',
              'all'	: 'Returns True if all items in an iterable object are true',
              'any' : 'Returns True if any item in an iterable object is true',
              'ascii'	: 'Returns a readable version of an object. Replaces none-ascii characters with escape character',
              'bin' : 'Returns the binary version of a number',
              'bool' :'Returns the boolean value of the specified object',
              'bytearray'	:'Returns an array of bytes',
              'bytes'	:'Returns a bytes object',
              'callable' : 'Returns True if the specified object is callable, otherwise False',
              'chr':'Returns a character from the specified Unicode code.',
              'classmethod' :	'Converts a method into a class method',
              'compile':'Returns the specified source as an object, ready to be executed',
              'complex':	'Returns a complex number',
              'delattr' :'Deletes the specified attribute (property or method) from the specified object',
              'dict':	'Returns a dictionary (Array)',
              'dir':'Returns a list of the specified objects properties and methods',
              'divmod':'Returns the quotient and the remainder when argument1 is divided by argument2',
              'enumerate':'Takes a collection (e.g. a tuple) and returns it as an enumerate object',
              'eval':	'Evaluates and executes an expression',
              'exec'	:'Executes the specified code (or object)',
              'filter':'Use a filter function to exclude items in an iterable object',
              'float':'Returns a floating point number',
              'format':'Formats a specified value',
              'frozenset':'Returns a frozenset object',
              'getattr':'Returns the value of the specified attribute (property or method)',
              'globals':'Returns the current global symbol table as a dictionary',
              'hasattr':'Returns True if the specified object has the specified attribute (property/method)',
              'hash':'Returns the hash value of a specified object',
              'help':	'Executes the built-in help system',
              'hex':'Converts a number into a hexadecimal value',
              'id':'Returns the id of an object',
              'input':'Allowing user input',
              'int':'Returns an integer number',
              'isinstance':'Returns True if a specified object is an instance of a specified object',
              'issubclass':'Returns True if a specified class is a subclass of a specified object',
              'iter':'Returns an iterator object',
              'len':'Returns the length of an object',
              'list':'Returns a list',
              'locals':'Returns an updated dictionary of the current local symbol table',
              'map':'Returns the specified iterator with the specified function applied to each item',
              'max':'Returns the largest item in an iterable',
              'memoryview':'Returns a memory view object',
              'min':	'Returns the smallest item in an iterable',
              'next':'Returns the next item in an iterable',
              'object':'Returns a new object',
              'oct':'Converts a number into an octal',
              'open':'Opens a file and returns a file object',
              'ord':'Convert an integer representing the Unicode of the specified character',
              'pow':'Returns the value of x to the power of y',
              'print':'Prints to the standard output device',
              'property':'Gets, sets, deletes a property',
              'range':'Returns a sequence of numbers, starting from 0 and increments by 1 (by default)',
              'repr':'Returns a readable version of an object',
              'reversed':'Returns a reversed iterator',
              'round':'Rounds a numbers',
              'set':'Returns a new set object',
              'setattr':'Sets an attribute (property/method) of an object',
              'slice':'Returns a slice object',
              'sorted':'Returns a sorted list',
              '@staticmethod':'Converts a method into a static method',
              'str':'Returns a string object',
              'sum':'Sums the items of an iterator',
              'super':'Returns an object that represents the parent class',
              'tuple':'Returns a tuple',
              'type':'Returns the type of an object',
              'vars':'Returns the __dict__ property of an object',
              'zip':'Returns an iterator, from two or more iterators'}
    keyy=functionss[search]
    print(str(keyy))



def key_word_dict(search):
    key_word={'false':'True and False are truth values in Python. They are the results of comparison operations or logical (Boolean) operations in Python' ,
              'await' :'The async and await keywords are provided by the asyncio library in Python. They are used to write concurrent code in Python',
              'async':'The async and await keywords are provided by the asyncio library in Python. They are used to write concurrent code in Python',
              'none' : 'None is a special constant in Python that represents the absence of a value or a null value.It is an object of its own datatype, the NoneType. We cannot create multiple None objects but can assign it to variables. These variables will be equal to one another.We must take special care that None does not imply False, 0 or any empty list, dictionary, string etc.',
              'and':'and, or, not are the logical operators in Python.' ,
              'or':'and, or, not are the logical operators in Python.',
              'class':'class is used to define a new user-defined class in Python.Class is a collection of related attributes and methods that try to represent a real world situation. This idea of putting data and functions together in a class is central to the concept of object-oriented programming (OOP).Classes can be defined anywhere in a program. But it is a good practice to define a single class in a module.',
              'def':'used to define a user-defined function.Function is a block of related statements, which together does some specific task. It helps us organize code into manageable chunks and also to do some repetitive task.',
              'del':'del is used to delete the reference to an object. Everything is object in Python. We can delete a variable reference using del',
              'if':'if, else, elif are used for conditional branching or decision making.When we want to test some condition and execute a block only if the condition is true, then we use if and elif. elif is short for else if. else is the block which is executed if the condition is false',
              'elif':'if, else, elif are used for conditional branching or decision making.When we want to test some condition and execute a block only if the condition is true, then we use if and elif. elif is short for else if. else is the block which is executed if the condition is false',
              'raise':'except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.',
              'try': 'except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.',
              'except':'except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.',
              'else':'if, else, elif are used for conditional branching or decision making.When we want to test some condition and execute a block only if the condition is true, then we use if and elif. elif is short for else if. else is the block which is executed if the condition is false',
              'in':'in is used to test if a sequence (list, tuple, string etc.) contains a value. It returns True if the value is present, else it returns False',
              'is':'is used in Python for testing object identity. While the == operator is used to test if two variables are equal or not, is is used to test if the two variables refer to the same object.',
              'lambda':'lambda is used to create an anonymous function (function with no name). It is an inline function that does not contain a return statement. It consists of an expression that is evaluated and returned.',
              'nonlocal':'The use of nonlocal keyword is very much similar to the global keyword. nonlocal is used to declare that a variable inside a nested function (function inside a function) is not local to it, meaning it lies in the outer inclosing function. If we need to modify the value of a non-local variable inside a nested function, then we must declare it with nonlocal. Otherwise a local variable with that name is created inside the nested function',
              'pass':'pass is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder.',
              'return':'return statement is used inside a function to exit it and return a value.If we do not return a value explicitly, None is returned automatically. ',
              'while':'used for looping in Python.The statements inside a while loop continue to execute until the condition for the while loop evaluates to False or a break statement is encountered.',
              'with':'with statement is used to wrap the execution of a block of code within methods defined by the context manager.Context manager is a class that implements __enter__ and __exit__ methods. Use of with statement ensures that the __exit__ method is called at the end of the nested block. This concept is similar to the use of try…finally block.',
              'yield':'yield is used inside a function like a return statement. But yield returns a generator.Generator is an iterator that generates one item at a time. A large list of value will take up a lot of memory. Generators are useful in this situation as it generates only one value at a time instead of storing all the values in memory. ',
              'not':'and, or, not are the logical operators in Python.',
              'finally':'finally is used with try…except block to close up resources or file streams.Using finally ensures that the block of code inside it gets executed even if there is an unhandled exception',
              'import': 'from, import keyword is used to import modules into the current namespace. from…import is used to import specific attributes or functions into the current namespace.',
              'from':'from, import keyword is used to import modules into the current namespace. from…import is used to import specific attributes or functions into the current namespace.',
              'global':'global is used to declare that a variable inside the function is global (outside the function).If we need to read the value of a global variable, it is not necessary to define it as global. This is understood.If we need to modify the value of a global variable inside a function, then we must declare it with global. Otherwise a local variable with that name is created.',
              'for':'for is used for looping. Generally we use for when we know the number of times we want to loop.',
              'as':'as is used to create an alias while importing a module. It means giving a different name (user-defined) to a module while importing it.',
              'assert' :'assert is used for debugging purposes.While programming, sometimes we wish to know the internal state or check if our assumptions are true. assert helps us do this and find bugs more conveniently. assert is followed by a condition.If the condition is true, nothing happens. But if the condition is false, AssertionError is raised.' ,
              'break':'are used inside for and while loops to alter their normal behavior.break will end the smallest loop it is in and control flows to the statement immediately below the loop. continue causes to end the current iteration of the loop, but not the whole loop.',
              'continue':'are used inside for and while loops to alter their normal behavior.break will end the smallest loop it is in and control flows to the statement immediately below the loop. continue causes to end the current iteration of the loop, but not the whole loop.'}
    keyy=key_word[search]
    print(str(keyy))


def string_method(search):
    stringg={'capitalize':'Converts the first character to upper case',
             'casefold':	'Converts string into lower case',
             'center':'Returns a centered string',
             'count':'Returns the number of times a specified value occurs in a string',
             'encode':'Returns an encoded version of the string',
             'endswith':'Returns true if the string ends with the specified value',
             'expandtabs':'Sets the tab size of the string',
             'find':'Searches the string for a specified value and returns the position of where it was found',
             'format':'Formats specified values in a string',
             'format_map':'Formats specified values in a string',
             'index':'Searches the string for a specified value and returns the position of where it was found',
             'isalnum':'Returns True if all characters in the string are alphanumeric',
             'isalpha':'Returns True if all characters in the string are in the alphabet',
             'isdecimal':'Returns True if all characters in the string are decimals',
             'isdigit':'Returns True if all characters in the string are digits',
             'isidentifier':'Returns True if the string is an identifier',
             'islower':'Returns True if all characters in the string are lower case',
             'isnumeric':'Returns True if all characters in the string are numeric',
             'isprintable':'Returns True if all characters in the string are printable',
             'isspace':'Returns True if all characters in the string are whitespaces',
             'istitle':'Returns True if the string follows the rules of a title',
             'isupper':'Returns True if all characters in the string are upper case',
             'join':'Joins the elements of an iterable to the end of the string',
             'ljust':'Returns a left justified version of the string',
             'lower':'Converts a string into lower case',
             'lstrip':'Returns a left trim version of the string',
             'maketrans':'Returns a translation table to be used in translations',
             'partition':'Returns a tuple where the string is parted into three parts',
             'replace':'Returns a string where a specified value is replaced with a specified value',
             'rfind':'Searches the string for a specified value and returns the last position of where it was found',
             'rindex':'Searches the string for a specified value and returns the last position of where it was found',
             'rjust':'Returns a right justified version of the string',
             'rpartition':'Returns a tuple where the string is parted into three parts',
             'rsplit':'Splits the string at the specified separator, and returns a list',
             'rstrip':'Returns a right trim version of the string',
             'split':'Splits the string at the specified separator, and returns a list',
             'splitlines':'Splits the string at line breaks and returns a list',
             'startswith':'Returns true if the string starts with the specified value',
             'strip':'Returns a trimmed version of the string',
             'swapcase':'Swaps cases, lower case becomes upper case and vice versa',
             'title':'Converts the first character of each word to upper case',
             'translate':'Returns a translated string',
             'upper'	:'Converts a string into upper case',
             'zfill':'Fills the string with a specified number of 0 values at the beginning'}
    keyy = stringg[search]
    print(str(keyy))

def list_method(search):
    lists={'append':'Adds an element at the end of the list',
           'clear':'Removes all the elements from the list',
           'copy':	'Returns a copy of the list',
           'count':'Returns the number of elements with the specified value',
           'extend':'Add the elements of a list (or any iterable), to the end of the current list',
           'index':'Returns the index of the first element with the specified value',
           'insert':'Adds an element at the specified position',
           'pop':'Removes the element at the specified position',
           'remove':'Removes the first item with the specified value',
           'reverse':'Reverses the order of the list',
           'sort':'Sorts the list',
           'clear':'Removes all the elements from the list',
           'copy':	'Returns a copy of the list',
           'count':'Returns the number of elements with the specified value',
           'extend':'Add the elements of a list (or any iterable), to the end of the current list',
           'index':'Returns the index of the first element with the specified value',
           'insert':'Adds an element at the specified position',
           'pop':'Removes the element at the specified position',
           'remove':'Removes the first item with the specified value',
           'reverse':'Reverses the order of the list',
           'sort':'Sorts the list'}
    keyy = lists[search]
    print(str(keyy))

def dict(search):
    dictt={'clear':'Removes all the elements from the dictionary',
           'copy':'Returns a copy of the dictionary',
           'fromkeys':'Returns a dictionary with the specified keys and value',
           'get':'Returns the value of the specified key',
           'items':'Returns a list containing a tuple for each key value pair',
           'keys':'Returns a list containing the dictionarys keys',
           'pop':'Removes the element with the specified key',
           'popitem':'Removes the last inserted key-value pair',
           'setdefault':'Returns the value of the specified key. If the key does not exist: insert the key, with the specified value',
           'update':'Updates the dictionary with the specified key-value pairs',
           'values':'Returns a list of all the values in the dictionary'}
    keyy = dictt[search]
    print(str(keyy))

def file():
    file={'close':'	Closes the file',
          'detach ':'	Returns the separated raw stream from the buffer',
          'fileno':'	Returns a number that represents the stream, from the operating systems perspective',
          'flush ':'	Flushes the internal buffer',
          'isatty ':'	Returns whether the file stream is interactive or not',
          'read ':' 	Returns the file content',
          'readable ':' 	Returns whether the file stream can be read or not',
          'readline ':' 	Returns one line from the file',
          'readlines ':'	Returns a list of lines from the file',
          'seek ':' 	Change the file position',
          'seekable ':' 	Returns whether the file allows us to change the file position',
          'tell ':' 	Returns the current file position',
          'truncate ':' 	Resizes the file to a specified size',
          'writeable ':'	Returns whether the file can be written to or not',
          'write ':'	Writes the specified string to the file',
          'writelines ':'	Writes a list of strings to the file'}
    keyy = file[search]
    print(str(keyy))

def builtin_Except():
    builtin={'ArithmeticError':'  Raised when an error occurs in numeric calculations',
             'AssertionError':'  Raised when an assert statement fails',
             'AttributeError ':' Raised when attribute reference or assignment fails',
             'Exception':'  Base class for all exceptions',
             'EOFError':'  Raised when the input     method hits an   end of file   condition   EOF',
             'FloatingPointError':'  Raised when a floating point calculation fails',
             'GeneratorExit ':' Raised when a generator is closed   with the close     method',
             'ImportError ':'  Raised when an imported module does not exist',
             'IndentationError ':'  Raised when indendation is not correct',
             'IndexError ':' Raised when an index of a sequence does not exist',
             'KeyError ':' Raised when a key does not exist in a dictionary',
             'KeyboardInterrupt ':'  Raised when the user presses Ctrl  c   Ctrl  z or Delete',
             'LookupError ':'  Raised when errors raised cant be found',
             'MemoryError ':' Raised when a program runs out of memory',
             'NameError ':' Raised when a variable does not exist',
             'NotImplementedError ':'  Raised when an abstract method requires an inherited class to override the method',
             'OSError ':' Raised when a system related operation causes an error',
             'OverflowError ':' Raised when the result of a numeric calculation is too large',
             'ReferenceError ':' Raised when a weak reference object does not exist',
             'RuntimeError ':' Raised when an error occurs that do not belong to any specific expections',
             'StopIteration ':' Raised when the next     method of an iterator has no further values',
             'SyntaxError ':' Raised when a syntax error occurs',
             'TabError ':' Raised when indentation consists of tabs or spaces',
             'SystemError ':' Raised when a system error occurs',
             'SystemExit ':' Raised when the sys  exit     function is called',
             'TypeError ':'  Raised when two different types are combined',
             'UnboundLocalError ':' Raised when a local variable is referenced before assignment',
             'UnicodeError ':' Raised when a unicode problem occurs',
             'UnicodeEncodeError ':' Raised when a unicode encoding problem occurs',
             'UnicodeDecodeError ':' Raised when a unicode decoding problem occurs',
             'UnicodeTranslateError ':'  Raised when a unicode translation problem occurs',
             'ValueError ':' Raised when there is a wrong value in a specified data type',
             'ZeroDivisionError ':' Raised when the second operator in a division is zero'}
    keyy = builtin[search]
    print(str(keyy))


if __name__ == '__main__':
    main()