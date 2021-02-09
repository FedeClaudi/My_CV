from cv.render_utils import render_panel, make_table
from rich.markdown import Markdown

from myterial import orange, orange_light

header = f'bold {orange}'
highlight = f'[{orange_light}]'


@render_panel
def render_education(info):
    # Make table
    columns = [
        ('center', 13, None, 1, f'[bold]Date'),
        (None, None, None, 1, f'[{header}]Title[/{header}]'),
        (None, None, None, 1, f'[{header}]Supervisor[/{header}]'),
        (None, None, 'bold', False, f'[{header}]Insitute[/{header}]'),
    ]
    table = make_table(columns)


    # Populate table
    for key, (title, center, supervisor) in info.items():
        table.add_row(
            f'[dim]({key[0]} - {key[1]})',
            '',
            highlight + title,
            "",
            center,
            '',
            supervisor
        )
    return table, 'green', 'Education'

@render_panel
def render_extracurr_education(info):
    # Make table
    columns = [
        ('center', 13, None, 1, f'[bold]Date'),
        (None, None, None, 1, f'[{header}]Title[/{header}]'),
        (None, None, 'bold', 1, f'[{header}]Insitute[/{header}]'),

    ]
    table = make_table(columns)

    # Populate table
    for key, (title, institution, other) in info.items():
        table.add_row(
            '[dim]'+str(key),
            '',
            highlight + title,
            '',
            institution + '[dim]  ' +other,
        )
    return table, 'green', 'Extracurricular education'


@render_panel
def render_experience(experience):
    # Make table
    columns = [
        ('center', 13, None, 1, f'[bold]Date'),
        (None, None, 'italic', 1, f'[{header}]Name[/{header}]'),
        (None, None, 'bold', 1, f'[{header}]Insitute[/{header}]'),
        (None, None, 'bold', 1, f'[{header}]Supervisor[/{header}]'),

    ]
    table = make_table(columns)

    # Populate table
    for key, (name, institution, supervisor) in experience.items():
        table.add_row(
            f'[dim]({key[0]} - {key[1]})',
            '',
            highlight + name,
            "",
            institution,
            '',
            supervisor,
        )


    # Render
    return table, 'blue', 'Research'

@render_panel
def render_teaching(experience):
    # Make table
    columns = [
        ('center', 13, None, 1, f'[bold]Date'),
        (None, None, 'italic', 1, f'[{header}]Name[/{header}]'),
        (None, None, 'bold', 1, f'[{header}]Insitute[/{header}]'),

    ]
    table = make_table(columns)

    # Populate table
    for key, (name, institution) in experience.items():
        table.add_row(
            '[dim]'+str(key),
            '',
            highlight + name,
            "",
            institution,
        )


    # Render
    return table, 'blue', 'Teaching'


@render_panel
def render_publications(pubs):
    # Make table
    columns = [
        ('center', 13, None, 1, f'[bold]Date'),
        (None, 50, 'italic', 1, f'[{header}]Title[/{header}]'),
        (None, 20, None, 1, f'[{header}]Authors[/{header}]'),
        (None, None, None, None, f'[{header}]Journal[/{header}]'),

    ]
    table = make_table(columns)

    # Populate table
    for (_, key), (title, authors, journal, doi) in pubs.items():
        if len(authors) > 40:
            # authors = authors[:31 - 4] + ' ...\n'
            authors = authors.split(',')[0] + ', ...\n'

            # if 'claudi' not in authors.lower():
            #     authors += ' [bold green]F. Claudi[/bold green] ...'

        table.add_row(
            '[dim]'+str(key),
            '',
            highlight + title + '\n',
            "",
            authors,
            '',
            journal + '[dim]\n'+doi
        )


    # Render
    return table, 'blue', 'Publications'


@render_panel
def render_posters(pubs):
    # Make table
    columns = [
        ('center', 13, None, 1, f'[bold]Date'),
        (None, None, 'italic', 1, f'[{header}]Title[/{header}]'),
        (None, None, 'bold', 1, f'[{header}]Authors[/{header}]'),
        (None, None, 'bold', 1, f'[{header}]Conference[/{header}]'),

    ]
    table = make_table(columns)

    # Populate table
    for key, (title, authors, conference) in pubs.items():
        if len(authors) > 100:
            authors = authors[:96] + ' ...'

            if 'claudi' not in authors.lower():
                authors += ' [bold green]F. Claudi[/bold green] ...'

        table.add_row(
            '[dim]'+str(key),
            '',
            highlight + title,
            "",
            authors,
            '',
            conference,
        )

    # Render
    return table, 'white', 'Posters'

@render_panel
def render_awards(pubs):
    # Make table
    columns = [
        ('center', 13, None, 1, f'[bold]Date'),
        (None, None, 'italic', 1, f'[{header}]Title[/{header}]'),
        (None, None, 'bold', 1, f'[{header}]Institution[/{header}]'),

    ]
    table = make_table(columns)

    # Populate table
    for key, (title, institution) in pubs.items():
        table.add_row(
            '[dim]'+str(key),
            '',
            highlight + title,
            "",
            institution
        )

    # Render
    return table, 'white', 'Awards & Fellowships'


def render_header():
    return Markdown('#TITLE\n##subtitle')
