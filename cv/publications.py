from rich.panel import Panel
from rich.table import Table
from scholarly import scholarly
from rich import box

from myterial import grey, orange, pink, indigo


def sort_items(item):
    """Sort special variables first, then alphabetically."""
    try:
        return int(item["bib"]["pub_year"])
    except KeyError:
        return 0


class Publications:
    def __init__(self):
        super(Publications, self).__init__()
        myid = "8eDOmAQAAAAJ"  # google scholar ID
        self.mypubs = scholarly.search_author_id(myid, filled=True)

    def panel(self, tb):
        return Panel(
            tb,
            title=f"[b {pink}]Publications",
            title_align="center",
            border_style=indigo,
        )

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
        tb.add_column("year")
        tb.add_column("title")

        year = None
        for n, pub in enumerate(
            sorted(self.mypubs["publications"], key=sort_items, reverse=True)
        ):
            cites = pub["num_citations"]
            pub = scholarly.fill(pub)["bib"]
            authors = pub["author"].replace(" and", ",")

            try:
                if pub["pub_year"] != year:
                    _year = pub["pub_year"]
                    year = _year
                else:
                    _year = ""
            except KeyError:
                _year = 2020

            tb.add_row(str(_year), pub["title"])
            a = 1

        yield self.panel(tb)
