import click
import coloredlogs
import logging
import os


def load_config(debug: bool=False) -> None:
    if debug:
        logging.basicConfig(level=logging.DEBUG)
        fmt = '%(asctime)s - %(levelname)-2s [%(filename)s:%(lineno)d][%(funcName)1s] %(message)s'
        os.environ['COLOREDLOGS_LOG_FORMAT'] = fmt
        logger = logging.getLogger(__name__)
        coloredlogs.install(level='DEBUG', logger=logger)


class {{(cookiecutter.project_slug.title()).replace('_', '')}}(object):
    def __init__(self):
        pass

    def say_hello(self) -> None:
        print('hello!')


@click.command('hello', help='say hello')
@click.pass_context
def hello(ctx: object) -> None:
    print('hey!')
    logging.debug('debug')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug', is_flag=True, help='Debug mode on')
@click.pass_context
def cli(ctx: object, debug: bool):
    ctx.obj = {}
    ctx.obj['debug'] = debug

    load_config(debug)


commands = [hello]
for command in commands:
    cli.add_command(command)

if __name__ == '__main__':
    cli()

# eof
