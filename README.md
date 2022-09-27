# Python Multiprocessing Class (Extendable)


**! NOTE ! --> YOU NEED TO HAVE PYTHON 3.3 OR ABOVE INSTALLED**

You will notice three files in the project:

- `src/app.py`
- `src/mp.py`
- `src/number_processor.py`

Here is the overview of this project: 

*`app.py` imports the number_processor.NumberProcessor class, which is defined in `number_processor.py`. The NumberProcessor class is an extension of the `Multiprocessor` class, which is from `mp.py`.*

The example extension of the generic `Multiprocessor` class is `NumberProcessor`, which only needs to define it's `run()` function. This run function can define any number of arguments. 

Tradeoff: Python intellisense in any editors will not throw errors until runtime if the number/types of the arguments to an extension-based class `run()` function due to the generic nature of the `Multiprocessor` class.

## How do I start?

The first thing to do is create a Python *virtual environment*. This step isn't *necessarily* required as there are no third party packages used in this repository.

An easy way to instantiate a virtual environment is by using the Make recipe: `make venv`

With or without the virtual environment, you can start the test in this repository by running `make start`, which is equivalent to `python src/app.py`.

## Running it went great! Where do I go from here?

Bring the `Multiprocessor` class with you wherever you go to do a bunch of iterable work! Create an extension of the class that runs batches of arguments against the same function, or test it out on a piece of code you think could be faster by asynchronously feeding arguments into the same function! You can bring this anywhere where the version of Python is 3.3 or above.