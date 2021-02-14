from rich.panel import Panel

from myterial import grey, orange, pink, indigo

from cv._info import Base, Entry, highlight


class Education(Base):
    entries = (
        Entry(
            "2017 - now",
            f'PhD in [{highlight}]"Experimental and theoretical systems neuroscience"[/{highlight}]',
            "Dr. Tiago Branco",
            "Sainsbury Wellcome Centre [dim]UCL",
        ),
        Entry(
            "2015 - 2016",
            f'Master in Research in [{highlight}]"Integrative Neuroscience"[/{highlight}]',
            "Dr. Ian Duguid",
            "University of Edinburgh",
        ),
        Entry(
            "2012 - 2015",
            f'Bachelor in [{highlight}]"Medical Biotechnologies"[/{highlight}]',
            "Dr. Ian Duguid",
            "University of Edinburgh",
        ),
    )

    def __init__(self):
        super(Education, self).__init__()

    def panel(self, tb):
        return Panel(
            tb,
            title=f"[b {pink}]Education",
            title_align="left",
            border_style=indigo,
        )
