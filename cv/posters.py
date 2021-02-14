from rich.panel import Panel

from myterial import grey, orange, pink, indigo

from cv._info import Base, Entry, highlight


class Posters(Base):
    entries = (
        Entry(
            "2020",
            "Fast unsupervised learning and innate heuristics support escape path selection",
            "[bold green]Federico Claudi[/bold green], Dario Campagner, Tiago Branco",
            "Bernstein Conference",
        ),
    )
    columns = ["Date", "Title", "Author", "venue", ""]

    def __init__(self):
        super(Posters, self).__init__()

    def panel(self, tb):
        return Panel(
            tb,
            title=f"[b {pink}]Posters",
            title_align="left",
            border_style=indigo,
        )
