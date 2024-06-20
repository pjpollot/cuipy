# Benchmark CuiPy 

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
python main.py --cui [(Optional) script's arguments]

# ... if you wish to change the port
python main.py --cui --cui_port <Port> [(Optional) script's arguments]
```