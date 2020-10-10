from pyinspect._colors import *
import pyinspect as pi
import numpy as np
from rich.panel import Panel
from scholarly import scholarly


from .info import *
from .render import *

WIDTH = 150

def make_gscholar_bio(me):
    bio = pi.Report(color=orange, dim=dimorange)
    bio.width = WIDTH
    bio.tb.expand = True

    bio.add(f'[bold {lightorange}]{me.name}')

    # Interests
    bio.add(f'[{gray}]{me.affiliation}')
    bio.add(f'[dim i]Interests: ' + ''.join(me.interests))

    # Numbers
    bio.add(f'[{lightgray}]Citations: [{orange}]{me.citedby}', justify='right')
    bio.add(f'[{lightgray}]H-index: [{orange}]{me.hindex}', justify='right')

    return Panel(
            bio.tb,
            expand=True,
            # width=WIDTH,
            border_style=bio.dim,
            padding=(0, 2, 1, 2),
    )

def make_pubs():
    def sort_items(item):
        """Sort special variables first, then alphabetically."""
        year = item.bib['year']
        return year


    myid = '8eDOmAQAAAAJ'  # google scholar ID
    me = scholarly.search_author_id(myid).fill()

    pubs = pi.Report('Publications', accent=orange, dim=mocassin)
    pubs.width = WIDTH

    pubs.add(make_gscholar_bio(me), 'obj')
    pubs.spacer(2)

    year = None
    for n, pub in enumerate(sorted(me.publications, key=sort_items, reverse=True)):
        pub.fill()

        pub = pub.bib

        # Mark year
        if pub['year'] != year:

            if n > 0:
                pubs.line(lightorange)
                pubs.spacer()

            pubs.add(f'[bold {lightsalmon}]{pub["year"]}', justify='center')
            year = pub['year']
            pubs.spacer()


        # add title
        pubs.add(f'[bold italic {lightorange}]' + pub['title']) 

        # add authors
        auths = pub['author'].replace(' and', ',')

        names = ['F Claudi', 'Federico Claudi', 'F. Claudi']
        formatted_auths = ''
        for author in auths.split(','):
            if author.strip() in names:
                formatted_auths += f'[bold green]{author}[/bold green],'
            else:
                formatted_auths += f'[{gray}]{author}[/{gray}],'


        # Add journal
        if 'eprint' in pub.keys():
            url = pub['eprint']
        elif 'url' in pub.keys():
            url = pub['url']
        else:
            print(f'No URL found for pub {pub}')
        pubs.add(f'[i {lightgray}]' + pub['journal'] + f'[/i {lightgray}]' + '[dim]\n' + url)


        # Add citations
        pubs.add(f'[{lightgray}]Citations: [{orange}]{pub["cites"]}', justify='right')

        pubs.spacer()

    return pubs


def make_cv():

    hs = f'bold {lightblue2}'


    CV = pi.Report('Curriculum Vitae', color=salmon, 
        accent=lightsalmon, dim=salmon)
    CV.width = WIDTH
    
    # ? education
    CV.add(f'[{hs}]         [underline]Education:')
    CV.spacer()
    CV.add(render_education(education), 'obj')
    
    # ? extracurr education
    CV.spacer(2)
    CV.add(f'[{hs}]         [underline]Extracurricular education')
    CV.spacer()
    CV.add(render_extracurr_education(extracurr_education), 'obj')
    

    # ? research experience
    CV.spacer(6)
    CV.add(f'[{hs}]         [underline]Research experience')
    CV.spacer()
    CV.add(render_experience(research_experience), 'obj')
    
    # ? teaching experience
    CV.spacer(2)
    CV.add(f'[{hs}]         [underline]Teaching experience')
    CV.spacer()
    CV.add(render_teaching(teaching_experience), 'obj')
    
    # ?  posters
    CV.spacer(2)
    CV.add(f'[{hs}]         [underline]Poster presentations')
    CV.spacer()
    CV.add(render_posters(posters), 'obj')
    
    # ?  awards
    CV.spacer(6)
    CV.add(f'[{hs}]         [underline]Awards and fellowships')
    CV.spacer()
    CV.add(render_awards(awards), 'obj')

    return CV