import click
import numexpr

def calculate(formula):
    try:
        print(f'The result: {numexpr.evaluate(formula)}')
    except KeyError:
        print('Error. Incorrect expression.')


@click.command()
@click.argument('formula')
def __main(formula):
    """
    This module performs the calculations you need.
    """
    calculate(formula)

if __name__ == "__main__":
    __main()