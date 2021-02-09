import numpy as np
from rich.panel import Panel
from rich.table import Table
from scholarly import scholarly
from github import Github

import pyinspect as pi
from myterial import orange, orange_light, green, green_dark, amber, salmon_light, blue_grey, blue_grey_light

from .info import BIO, open_source_projs, education, research_experience, extracurr_education, teaching_experience, publications, posters, awards
from .render import render_education, render_extracurr_education, render_experience, render_teaching, render_publications, render_posters, render_awards, render_header
from .secrets import gh_pswd

WIDTH = 150


def make_bio():
    
    tb = Table(box=None, show_lines=None, show_edge=None, width=WIDTH)
    tb.add_column(justify='right')
    tb.add_column(justify='left')

    for n, (prop, val) in enumerate(BIO.items()):
        tb.add_row(f'[{orange if n <=1 else orange_light}]{prop}:', f'[bold]{val}')

        if n == 1:
            tb.add_row('', '')
    
    return tb

def make_projs():
    def sort_items(item):
        return git.get_repo(item[1]).stargazers_count

    # Use github API
    git = Github("FedeClaudi", gh_pswd)

    projs = pi.Report('Open source projects', color=green, accent=green, dim=green_Dark)
    projs.width = WIDTH
    projs.tb.expand = True

    # Sort projs by github stars
    sorted_projs = sorted(open_source_projs)

    # Make report
    for name in sorted_projs:
        descr, github, url = open_source_projs[name]

        projs.add(f'[{green}]' + name)
        projs.add(descr)

        projs.spacer()
        projs.add(f'[{blue_grey}]Github url:[/{blue_grey}] [dim]https://github.com/{github}', justify='right')

        if url is not None:
            projs.add(f'[{blue_grey}]Documentation:[/{blue_grey}] [dim]{url}', justify='right')

        repo = git.get_repo(github)
        projs.add(f'[{blue_grey_light}]Stars: [{orange}]{repo.stargazers_count}', justify='right')
        projs.spacer(2)

    return projs


def make_gscholar_bio(me):
    bio = pi.Report(color=orange, dim=dimorange)
    bio.width = WIDTH
    bio.tb.expand = True

    bio.add(f'[bold {orange_light}]{me.name}')

    # Interests
    bio.add(f'[{gray}]{me.affiliation}')
    bio.add(f'[dim i]Interests: ' + ''.join([i+' ' for i in me.interests]))

    # Numbers
    bio.add(f'[{blue_grey_light}]Total citations: [{orange}]{me.citedby}', justify='right')
    bio.add(f'[{blue_grey_light}]H-index: [{orange}]{me.hindex}', justify='right')

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

    pubs = pi.Report('Publications', accent=orange, dim=amber)
    pubs.width = WIDTH

    pubs.add(make_gscholar_bio(me), 'rich')
    pubs.spacer(2)

    year = None
    for n, pub in enumerate(sorted(me.publications, key=sort_items, reverse=True)):
        pub.fill()

        pub = pub.bib

        # Mark year
        if pub['year'] != year:

            if n > 0:
                pubs.line(amber)
                pubs.spacer()

            pubs.add(f'[bold {salmon_light}]{pub["year"]}', justify='center')
            year = pub['year']
            pubs.spacer()


        # add title
        pubs.add(f'[bold italic {orange_light}]' + pub['title']) 

        # add authors
        auths = pub['author'].replace(' and', ',')

        names = ['F Claudi', 'Federico Claudi', 'F. Claudi']
        formatted_auths = ''
        for author in auths.split(','):
            if author.strip() in names:
                formatted_auths += f'[bold green]{author}[/bold green],'
            else:
                formatted_auths += f'[{blue_grey}]{author}[/{blue_grey}],'

        pubs.add(formatted_auths)

        # Add journal
        if 'eprint' in pub.keys():
            url = pub['eprint']
        elif 'url' in pub.keys():
            url = pub['url']
        else:
            print(f'No URL found for pub {pub}')
        pubs.add(f'[i {blue_grey_light}]' + pub['journal'] + f'[/i {blue_grey_light}]' + '[dim]\n' + url)


        # Add citations
        pubs.add(f'[{blue_grey_light}]Citations: [{orange}]{pub["cites"]}', justify='right')

        pubs.spacer()

    return pubs


def make_cv():

    hs = f'bold {lightblue2}'


    CV = pi.Report('Curriculum Vitae', color=salmon, 
        accent=salmon_light, dim=salmon)
    CV.width = WIDTH
    
    # ? education
    CV.add(f'[{hs}]         [underline]Education:')
    CV.spacer()
    CV.add(render_education(education), 'rich')
    
    # ? extracurr education
    CV.spacer(2)
    CV.add(f'[{hs}]         [underline]Extracurricular education')
    CV.spacer()
    CV.add(render_extracurr_education(extracurr_education), 'rich')
    

    # ? research experience
    CV.spacer(4)
    CV.add(f'[{hs}]         [underline]Research experience')
    CV.spacer()
    CV.add(render_experience(research_experience), 'rich')
    
    # ? teaching experience
    CV.spacer(2)
    CV.add(f'[{hs}]         [underline]Teaching experience')
    CV.spacer()
    CV.add(render_teaching(teaching_experience), 'rich')
    
    # ?  posters
    CV.spacer(2)
    CV.add(f'[{hs}]         [underline]Poster presentations')
    CV.spacer()
    CV.add(render_posters(posters), 'rich')
    
    # ?  awards
    CV.spacer(4)
    CV.add(f'[{hs}]         [underline]Awards and fellowships')
    CV.spacer()
    CV.add(render_awards(awards), 'rich')

    return CV