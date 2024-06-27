# Command User Interface for Python (CuiPy)

## Usage

Write `main.py` file:

```python
from argparse import ArgumentParser, Namespace

from cuipy import CuiApp

def main(args: Namespace):
    # main function that takes the parser arguments
    ...

if __name__ == "__main__":
    # define your argument parser
    parser = ArgumentParser()
    parser.add_argument(
        ...
    )
    ...
    # call the Cui application
    app = CuiApp(fn=main, parser=parser)
    app.run()
```

On the terminal, you can run the script with either of the following commands:

```sh
# dry run (no gui)
python main.py [(Mandatory) script's arguments]

# cuipy's gui run 
python main.py --cui
```

## Installation

For users:

```sh
git clone https://github.com/pjpollot/cuipy.git
cd cuipy
pip install .
```

For devs (make sure to install [poetry](https://python-poetry.org/) package manager beforehand): 
```
git clone https://github.com/pjpollot/cuipy.git
cd cuipy
poetry install
```

## Further improvements 

```python
# cuipy's gui run + script's arguments
python main.py --cui [(Optional) script's arguments]

# ... if you wish to change the port
python main.py --cui --cui_port <Port> [(Optional) script's arguments]
```

Plus, 
- [ ] Beautiful GUI.
- [ ] Folder search.
- [ ] If an argument includes a choice, create a selection menu in the GUI.
- [ ] Extend action list (see [code](https://github.com/pjpollot/cuipy/blob/main/cuipy/actions.py)).
- [ ] Pydoc.

