from cv.render_utils import render_panel, make_table


@render_panel
def render_education(info):
    # Make table
    columns = [
        ('center', 13, None, 2, '[bold magenta]Date[/bold magenta]'),
        (None, None, 'italic', 2, '[bold magenta]Title[/bold magenta]'),
        (None, None, 'bold', 1, '[bold magenta]Insitute[/bold magenta]'),
        ('center', None, 'bold', 2, None),
        (None, None, None, False, '[bold magenta]Supervisor[/bold magenta]'),
    ]
    table = make_table(columns)


    # Populate table
    for key, (title, center, institution, supervisor) in info.items():
        table.add_row(
            f'({key[0]} - {key[1]})',
            '',
            title,
            "",
            center,
            '',
            institution,
            '',
            supervisor
        )
    return table, 'green', 'Education'

@render_panel
def render_extracurr_education(info):
    # Make table
    columns = [
        ('center', 13, None, 2, '[bold magenta]Date[/bold magenta]'),
        (None, None, 'italic', 2, '[bold magenta]Title[/bold magenta]'),
        (None, None, 'bold', 1, '[bold magenta]Insitute[/bold magenta]'),
        ('center', None, 'bold', False, None),

    ]
    table = make_table(columns)

    # Populate table
    for key, (title, institution, other) in info.items():
        table.add_row(
            str(key),
            '',
            title,
            '',
            institution,
            '',
            other
        )
    return table, 'green', 'Extracurricular education'


@render_panel
def render_experience(experience):
    # Make table
    columns = [
        ('center', 13, None, 2, '[bold magenta]Date[/bold magenta]'),
        (None, None, 'italic', 2, '[bold magenta]Name[/bold magenta]'),
        (None, None, 'bold', 2, '[bold magenta]Insitute[/bold magenta]'),
        (None, None, 'bold', 2, '[bold magenta]Supervisor[/bold magenta]'),

    ]
    table = make_table(columns)

    # Populate table
    for key, (name, institution, supervisor) in experience.items():
        table.add_row(
            f'({key[0]} - {key[1]})',
            '',
            name,
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
        ('center', 13, None, 2, '[bold magenta]Date[/bold magenta]'),
        (None, None, 'italic', 2, '[bold magenta]Name[/bold magenta]'),
        (None, None, 'bold', 2, '[bold magenta]Insitute[/bold magenta]'),

    ]
    table = make_table(columns)

    # Populate table
    for key, (name, institution) in experience.items():
        table.add_row(
            str(key),
            '',
            name,
            "",
            institution,
        )


    # Render
    return table, 'blue', 'Teaching'


@render_panel
def render_publications(pubs):
    # Make table
    columns = [
        ('center', 13, None, 2, '[bold magenta]Date[/bold magenta]'),
        (None, None, 'italic', 2, '[bold magenta]Title[/bold magenta]'),
        (None, None, 'bold', 2, '[bold magenta]Authors[/bold magenta]'),
        (None, None, 'bold', 2, '[bold magenta]Journal[/bold magenta]'),
        (None, None, 'bold', 2, '[bold magenta]DOI[/bold magenta]'),

    ]
    table = make_table(columns)

    # Populate table
    for key, (title, authors, journal, doi) in pubs.items():
        if len(authors) > 100:
            authors = authors[:96] + ' ...'

            if 'claudi' not in authors.lower():
                authors += ' [bold green]F. Claudi[/bold green] ...'

        table.add_row(
            str(key),
            '',
            title,
            "",
            authors,
            '',
            journal,
            '',
            doi
        )


    # Render
    return table, 'blue', 'Teaching'