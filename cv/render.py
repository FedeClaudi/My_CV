from rich.markdown import Markdown
from rich.table import Table
from rich import box

from myterial import orange, orange_light, pink


header = f"bold {orange}"
highlight = f"[{orange_light}]"


def make_table(columns, WIDTH):
    """
        Creates a table and  columns.

        Arguments:
            columns: list of render.COLUMN objects
            WIDTH: int

        Returns:
            Table object
    """
    # add table
    table = Table(
        box=box.SIMPLE_HEAD,
        padding=(0, 1),
        collapse_padding=False,
        show_header=True,
        show_footer=False,
        show_edge=False,
        pad_edge=None,
        expand=True,
        width=WIDTH - 20,
    )

    # add columns
    for column in columns:
        table.add_column(
            justify=column.justify,
            width=column.width,
            style=column.style,
            header=column.title,
        )

        if column.spacer:
            table.add_column(width=1)

    return table


class COLUMN:
    def __init__(
        self, justify=None, width=10, style="", spacer=False, title=""
    ):
        """Class for storing table columns parameters."""
        self.justify = justify
        self.width = width
        self.style = style
        self.spacer = spacer
        self.title = title


def education(info, WIDTH):
    """
        Make a table showing my education records

        Argument:
            info: dict of education info
    """
    # Make table
    columns = [
        COLUMN(justify="center", width=10, spacer=True, title=f"[bold]Date"),
        COLUMN(spacer=True, width=30, title=f"[{header}]Title"),
        COLUMN(spacer=True, width=30, title=f"[{header}]Supervisor"),
        COLUMN(justify="bold", width=20, title=f"[{header}]Insitute"),
    ]
    table = make_table(columns, WIDTH=WIDTH)

    # Populate table
    for key, (title, center, supervisor) in info.items():
        table.add_row(
            f"[dim]({key[0]} - {key[1]})",
            "",
            highlight + title,
            "",
            center,
            "",
            supervisor,
        )
    return table


def extracurr_education(info, WIDTH):
    """
        Make a table showing extra curricular education

        Argument:
            info: dict of extra curricular education
    """
    # Make table
    columns = [
        COLUMN(justify="center", width=10, spacer=True, title=f"[bold]Date"),
        COLUMN(spacer=True, width=30, title=f"[{header}]Title[/{header}]"),
        COLUMN(
            justify="bold",
            spacer=True,
            width=30,
            title=f"[{header}]Insitute[/{header}]",
        ),
        COLUMN(width=20),
    ]
    table = make_table(columns, WIDTH=WIDTH)

    # Populate table
    for key, (title, institution, other) in info.items():
        table.add_row(
            "[dim]" + str(key),
            "",
            highlight + title,
            "",
            institution + "[dim]  " + other,
        )
    return table


def experience(experience, WIDTH):
    """
        Make a table showing research experince

        Argument:
            info: dict of research experince
    """
    # Make table
    columns = [
        COLUMN(justify="center", width=10, spacer=True, title=f"[bold]Date"),
        COLUMN(
            justify="italic",
            width=30,
            spacer=True,
            title=f"[{header}]Name[/{header}]",
        ),
        COLUMN(
            justify="bold",
            width=30,
            spacer=True,
            title=f"[{header}]Insitute[/{header}]",
        ),
        COLUMN(
            justify="bold",
            spacer=True,
            title=f"[{header}]Supervisor[/{header}]",
            width=20,
        ),
    ]
    table = make_table(columns, WIDTH=WIDTH)

    # Populate table
    for key, (name, institution, supervisor) in experience.items():
        table.add_row(
            f"[dim]({key[0]} - {key[1]})",
            "",
            highlight + name,
            "",
            institution,
            "",
            supervisor,
        )

    # Render
    return table


def teaching(experience, WIDTH):
    """
        Make a table showing teaching experience

        Argument:
            info: dict of teaching experience
    """
    # Make table
    columns = [
        COLUMN(justify="center", width=10, spacer=True, title=f"[bold]Date"),
        COLUMN(
            justify="italic",
            spacer=True,
            width=30,
            title=f"[{header}]Name[/{header}]",
        ),
        COLUMN(
            justify="bold",
            spacer=True,
            width=30,
            title=f"[{header}]Insitute[/{header}]",
        ),
        COLUMN(width=20),
    ]
    table = make_table(columns, WIDTH=WIDTH)

    # Populate table
    for key, (name, institution) in experience.items():
        table.add_row(
            "[dim]" + str(key), "", highlight + name, "", institution,
        )

    # Render
    return table


def publications(pubs, WIDTH):
    """
        Make a table showing publications

        Argument:
            info: dict of publications
    """
    # Make table
    columns = [
        COLUMN(justify="center", width=10, spacer=True, title=f"[bold]Date"),
        COLUMN(
            width=30,
            justify="italic",
            spacer=True,
            title=f"[{header}]Title[/{header}]",
        ),
        COLUMN(width=30, spacer=True, title=f"[{header}]Authors[/{header}]"),
        COLUMN(width=20, title=f"[{header}]Journal[/{header}]"),
    ]
    table = make_table(columns, WIDTH=WIDTH)

    # Populate table
    for (_, key), (title, authors, journal, doi) in pubs.items():
        if len(authors) > 40:
            authors = authors.split(",")[0] + ", ...\n"

        table.add_row(
            "[dim]" + str(key),
            "",
            highlight + title + "\n",
            "",
            authors,
            "",
            journal + "[dim]\n" + doi,
        )

    # Render
    return table


def posters(pubs, WIDTH):
    """
        Make a table showing presented posters

        Argument:
            info: dict of presented posters
    """
    # Make table
    columns = [
        COLUMN(justify="center", width=10, spacer=True, title=f"[bold]Date"),
        COLUMN(
            justify="italic",
            width=30,
            spacer=True,
            title=f"[{header}]Title[/{header}]",
        ),
        COLUMN(
            justify="bold",
            width=30,
            spacer=True,
            title=f"[{header}]Authors[/{header}]",
        ),
        COLUMN(
            justify="bold",
            width=20,
            spacer=True,
            title=f"[{header}]Conference[/{header}]",
        ),
    ]
    table = make_table(columns, WIDTH=WIDTH)

    # Populate table
    for key, (title, authors, conference) in pubs.items():
        if len(authors) > 100:
            authors = authors[:96] + " ..."

            if "claudi" not in authors.lower():
                authors += f" [bold {pink}]F. Claudi[/bold {pink}] ..."

        table.add_row(
            "[dim]" + str(key),
            "",
            highlight + title,
            "",
            authors,
            "",
            conference,
        )

    # Render
    return table


def awards(awards, WIDTH):
    """
        Make a table showing awards

        Argument:
            info: dict of awards
    """
    # Make table
    columns = [
        COLUMN(justify="center", width=10, spacer=True, title=f"[bold]Date"),
        COLUMN(
            justify="italic",
            width=30,
            spacer=True,
            title=f"[{header}]Title[/{header}]",
        ),
        COLUMN(
            justify="bold",
            spacer=True,
            width=30,
            title=f"[{header}]Institution[/{header}]",
        ),
        COLUMN(width=20),
    ]
    table = make_table(columns, WIDTH=WIDTH)

    # Populate table
    for key, (title, institution) in awards.items():
        table.add_row(
            "[dim]" + str(key), "", highlight + title, "", institution
        )

    # Render
    return table


def make_header():
    """
        Make a markdown header
    """
    return Markdown("#TITLE\n##subtitle")
