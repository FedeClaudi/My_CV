from rich.panel import Panel

from myterial import grey, orange, pink, indigo

from cv._info import Base, Entry, highlight


class Awards(Base):
    entries = (
        Entry(
            "2020",
            "Wellcome Trust 4-Year PhD Fellowship.",
            "",
            "Sainsbury Wellcome Centre,[dim] University College London",
        ),
        Entry(
            "2015",
            "Erasmus scholarship for the bachelor project in Leuven, Belgium. ",
            "",
            "Università degli Studi,[dim] Milano, Italy",
        ),
    )

    columns = ["Date", "Title", "", "Institute"]

    def __init__(self):
        super(Awards, self).__init__()

    def panel(self, tb):
        return Panel(
            tb,
            title=f"[b {pink}]Awards",
            title_align="left",
            border_style=indigo,
        )
