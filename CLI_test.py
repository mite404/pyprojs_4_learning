import click


@click.command()
@click.option('--name', default="World", help='the name of the person to salute')
def salute_me(name):
    print(f"hello, {name}!")


if __name__ == '__main__':
    salute_me()
