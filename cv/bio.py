from rich.panel import Panel
from rich.table import Table

from myterial import grey, orange, pink


class Bio:
    info = {
        "name": "Federico Claudi",
        "email": "federico.claudi.17@ucl.ac.uk",
        "website": "https://fedeclaudi.github.io",
        "github": "https://github.com/FedeClaudi",
        "twitter": "https://twitter.com/Federico_claudi",
    }

    def __rich_console__(self, *args, **kwargs):
        tb = Table(box=None)
        tb.add_column(justify="right", style=grey)
        tb.add_column(justify="left", style=f"b {orange}")

        for k, v in self.info.items():
            tb.add_row(k, v)
        yield Panel(tb, title=f"[b {pink}]Bio")
