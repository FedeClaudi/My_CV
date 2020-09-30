from rich.console import Console
from rich.style import Style
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.pretty import Pretty
from rich.text import Text
from rich.style import Style
from rich import box

def render_panel(func):
    def wrapper(*args):      
        table, color, title = func(*args)
        return Panel(
                    table,
                    title='[bold white]' + title,
                    title_align='left',
                    border_style=Style.parse(color),
                    width=250,
                    padding=(1, 2, 0, 2),
                )
    return wrapper

def make_table(columns):
    table = Table(
            box=box.SIMPLE_HEAD,
            padding=(0, 1),
            collapse_padding=False,
            show_header=True,
            show_footer=False,
            show_edge=False,
            pad_edge=None,
            expand=False,
    )

    titles = []
    for (justify, width, style, add_spacer, title) in columns:
        table.add_column(justify=justify, width=width, style=style, header=title if title is not None else '')


        if add_spacer:
            table.add_column(width=add_spacer) 

    return table