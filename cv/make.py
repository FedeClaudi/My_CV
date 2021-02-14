from rich.panel import Panel
from rich.table import Table
from scholarly import scholarly
from github import Github

import pyinspect as pi
from myterial import (
    blue_light,
    orange,
    orange_light,
    green_light,
    amber,
    salmon_light,
    blue_grey,
    blue_grey_light,
    green,
    orange_dark,
    salmon,
    grey,
    pink,
)

from cv import info


try:
    from cv import secrets
except ImportError:
    raise ValueError(f"You need my secrets to get github data")

from cv import render


def bio(WIDTH):
    """
        Makes a table with biographic data.

        Arguments:
            WIDTH: int, table width
    """
    tb = Table(box=None, show_lines=None, show_edge=None, width=WIDTH)
    tb.add_column(justify="right")
    tb.add_column(justify="left")

    for n, (prop, val) in enumerate(info.BIO.items()):
        tb.add_row(
            f"[{orange if n <=1 else orange_light}]{prop}:", f"[bold]{val}"
        )

        if n == 1:
            tb.add_row("", "")

    return tb


def projs(WIDTH):
    def sort_items(item):
        return git.get_repo(item[1]).stargazers_count

    # Use github API
    git = Github("FedeClaudi", secrets.gh_pswd)

    projs = pi.Report(
        "Open source projects",
        color=green_light,
        accent=green_light,
        dim=green,
    )
    projs.width = WIDTH
    projs.tb.expand = True

    # Sort projs by github stars
    sorted_projs = sorted(info.open_source_projs)

    # Make report
    for name in sorted_projs:
        descr, github, url = info.open_source_projs[name]

        projs.add(f"[{green_light}]" + name)
        projs.add(descr)

        projs.spacer()
        projs.add(
            f"[{blue_grey}]Github url:[/{blue_grey}] [dim]https://github.com/{github}",
            justify="right",
        )

        if url is not None:
            projs.add(
                f"[{blue_grey}]Documentation:[/{blue_grey}] [dim]{url}",
                justify="right",
            )

        repo = git.get_repo(github)
        projs.add(
            f"[{blue_grey_light}]Stars: [{orange}]{repo.stargazers_count}",
            justify="right",
        )
        projs.spacer(2)

    return projs


def gscholar_bio(me, WIDTH):
    """
        Create a panel with an overvio of my google scholar profile
    """
    bio = pi.Report(color=orange, dim=orange_dark)
    bio.width = WIDTH
    bio.tb.expand = True

    bio.add(f"[bold {orange_light}]{me['name']}")

    # Interests
    bio.add(f"[{grey}]{me['affiliation']}")
    bio.add(
        f"[dim i]Interests: " + "".join([i + " " for i in me["interests"]])
    )

    # Numbers
    bio.add(
        f"[{blue_grey_light}]Total citations: [{orange}]{me['citedby']}",
        justify="right",
    )
    bio.add(
        f"[{blue_grey_light}]H-index: [{orange}]{me['hindex']}",
        justify="right",
    )

    return Panel(
        bio.tb, expand=True, border_style=bio.dim, padding=(0, 2, 1, 2),
    )


def pubs(WIDTH):
    def sort_items(item):
        """Sort special variables first, then alphabetically."""
        try:
            return int(item["bib"]["pub_year"])
        except KeyError:
            return 0

    myid = "8eDOmAQAAAAJ"  # google scholar ID
    me = scholarly.search_author_id(myid, filled=True)

    pubs = pi.Report("Publications", accent=orange, dim=amber)
    pubs.width = WIDTH

    pubs.add(gscholar_bio(me, WIDTH), "rich")
    pubs.spacer(2)

    year = None
    for n, pub in enumerate(
        sorted(me["publications"], key=sort_items, reverse=True)
    ):
        cites = pub["num_citations"]
        pub = scholarly.fill(pub)["bib"]

        if "pub_year" not in pub.keys():
            continue

        # Mark year
        if pub["pub_year"] != year:

            if n > 0:
                pubs.line(amber)
                pubs.spacer()

            pubs.add(
                f'[bold {salmon_light}]{pub["pub_year"]}', justify="center"
            )
            year = pub["pub_year"]
            pubs.spacer()

        # add title
        pubs.add(f"[bold italic {orange_light}]" + pub["title"])

        # add authors
        try:
            auths = pub["author"].replace(" and", ",")
        except KeyError:
            auths = ""

        names = ["F Claudi", "Federico Claudi", "F. Claudi"]
        formatted_auths = ""
        for author in auths.split(","):
            if author.strip() in names:
                formatted_auths += f"[bold {pink}]{author}[/bold {pink}],"
            else:
                formatted_auths += f"[{blue_grey}]{author}[/{blue_grey}],"

        pubs.add(formatted_auths)

        # Add journal
        if "eprint" in pub.keys():
            url = pub["eprint"]
        elif "url" in pub.keys():
            url = pub["url"]
        else:
            url = ""

        try:
            journal = pub["journal"]
        except KeyError:
            journal = ""

        pubs.add(
            f"[i {blue_grey_light}]"
            + journal
            + f"[/i {blue_grey_light}]"
            + "[dim]\n"
            + url
        )

        # Add citations
        pubs.add(
            f"[{blue_grey_light}]Citations: [{orange}]{cites}",
            justify="right",
        )

        pubs.spacer()

    return pubs


def cv(WIDTH):
    hs = f"bold {blue_light}"

    CV = pi.Report(
        "Curriculum Vitae", color=salmon, accent=salmon_light, dim=salmon
    )
    CV.width = WIDTH

    # ? education
    CV.add(f"[{hs}]         [underline]Education:")
    CV.spacer()
    CV.add(render.education(info.education, WIDTH), "rich")

    # ? extracurr education
    CV.spacer(2)
    CV.add(f"[{hs}]         [underline]Extracurricular education")
    CV.spacer()
    CV.add(render.extracurr_education(info.extracurr_education, WIDTH), "rich")

    # ? research experience
    CV.spacer(4)
    CV.add(f"[{hs}]         [underline]Research experience")
    CV.spacer()
    CV.add(render.experience(info.research_experience, WIDTH), "rich")

    # ? teaching experience
    CV.spacer(2)
    CV.add(f"[{hs}]         [underline]Teaching experience")
    CV.spacer()
    CV.add(render.teaching(info.teaching_experience, WIDTH), "rich")

    # ?  posters
    CV.spacer(2)
    CV.add(f"[{hs}]         [underline]Poster presentations")
    CV.spacer()
    CV.add(render.posters(info.posters, WIDTH), "rich")

    # ?  awards
    CV.spacer(4)
    CV.add(f"[{hs}]         [underline]Awards and fellowships")
    CV.spacer()
    CV.add(render.awards(info.awards, WIDTH), "rich")

    return CV
