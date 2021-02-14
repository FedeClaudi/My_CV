from rich.panel import Panel
from rich.table import Table
from rich import box
from dataclasses import dataclass

from myterial import grey, orange, orange_light, grey, green_light

header = f"bold {orange}"
highlight = f"{orange_light}"


@dataclass
class Entry:
    date: int  # start of education period
    description: str  #  title
    supervisor: str  # name
    university: str  # where


class Base:
    entries = []
    columns = ["Date", "Title", "Supervisor", "Institute"]

    def make_columns(self, tb):
        tb.add_column(
            f"[b {header}]{self.columns[0]}",
            justify="left",
            width=6,
            style=grey,
        )
        tb.add_column(
            f"[b {header}]{self.columns[1]}", width=30, style=green_light
        )
        tb.add_column(
            f"[b {header}]{self.columns[2]}",
            width=10,
            style="dim",
            header_style="dim",
        )
        tb.add_column(
            f"[b {header}]{self.columns[3]}",
            width=20,
            style="dim",
            header_style="dim",
        )

    def panel(self, tb):
        raise NotImplementedError

    def __rich_console__(self, *args, **kwargs):
        tb = Table(
            box=box.SIMPLE_HEAD,
            padding=(0, 1),
            collapse_padding=False,
            show_header=True,
            show_footer=False,
            show_edge=False,
            pad_edge=None,
            expand=True,
        )

        self.make_columns(tb)

        for entry in self.entries:
            tb.add_row(
                entry.date,
                entry.description,
                entry.supervisor,
                entry.university,
            )

        yield self.panel(tb)
