from rich.panel import Panel

from myterial import grey, orange, pink, indigo

from cv._info import Base, Entry, highlight


class Research(Base):
    entries = (
        Entry(
            "2017 - now",
            "PhD research project [dim](4 years)",
            "Dr. Tiago Branco.",
            "Sainsbury Wellcome Centre,[dim] UK",
        ),
        Entry(
            "2016 - 2017",
            "Visiting scientist [dim](1 year)",
            "Dr. Ian Duguid.",
            "University of Edinburgh,[dim] UK",
        ),
        Entry(
            "2015 - 2016",
            "Master project [dim](1 year)",
            "Dr. Ian Duguid.",
            "University of Edinburgh,[dim] UK",
        ),
        Entry(
            "2015 - 2015",
            "Bachelor dissertation project [dim](4 months)",
            "",
            "Katholiege Universitei,[dim] Leuven, Belgium",
        ),
        Entry(
            "2011 - 2011",
            "Summer internship [dim](1 month)",
            "Dr. Filippo Mancia",
            "Columbia university,[dim] New York City, USA",
        ),
        Entry(
            "2011 - 2011",
            "Summer internship [dim](1 month)",
            "",
            "Università degli Studi,[dim] Milano, Italy",
        ),
        Entry(
            "2010 - 2010",
            "Summer internship [dim](1 month)",
            "Dr. Filippo Mancia",
            "Columbia university,[dim] New York City, USA",
        ),
    )

    def __init__(self):
        super(Research, self).__init__()

    def panel(self, tb):
        return Panel(
            tb,
            title=f"[b {pink}]Research",
            title_align="left",
            border_style=indigo,
        )
