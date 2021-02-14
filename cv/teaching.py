from rich.panel import Panel

from myterial import grey, orange, pink, indigo

from cv._info import Base, Entry, highlight


class Teaching(Base):
    entries = (
        Entry(
            "2020 - 2020",
            f"Teaching Assistant at [{highlight}]NeuroMatchAcademy.",
            "Neuromatch Academy",
            "",
        ),
        Entry(
            "2019 - 2019",
            f"[link=https://www.xhmfoundation.com/braincamp-kosovo-2019]Teacher at [{highlight}]Braincamp",
            "ATOMI institute,[dim] Pristina",
            "",
        ),
        Entry(
            "2016 - 2016",
            "Training of colleagues in microsurgical and behavioural techniques",
            "University of Edinburgh,[dim] Edinburgh",
            "",
        ),
    )
    columns = ["Date", "Title", "Venue", "", "Institute"]

    def __init__(self):
        super(Teaching, self).__init__()

    def panel(self, tb):
        return Panel(
            tb,
            title=f"[b {pink}]Teaching",
            title_align="left",
            border_style=indigo,
        )
