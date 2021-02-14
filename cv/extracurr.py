from rich.panel import Panel

from myterial import grey, orange, pink, indigo

from cv._info import Base, Entry, highlight


class Extracurricular(Base):
    entries = (
        Entry(
            "2015 - 2015",
            f'Online Course in [{highlight}]"Medical Neuroscience"',
            "Attended on: coursera.org",
            "Duke University, USA",
        ),
        Entry(
            "2015 - 2015",
            f'Online Course in [{highlight}]"Synapses, Neurons and Brain"',
            "Attended on: coursera.org",
            "Hebrew University, Jerusalem, Israel",
        ),
    )

    def __init__(self):
        super(Extracurricular, self).__init__()

    def panel(self, tb):
        return Panel(
            tb,
            title=f"[b {pink}]Extracurricular",
            title_align="left",
            border_style=indigo,
        )
