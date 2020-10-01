from rich.console import Console
from rich.pretty import install
from rich.table import Table
import pyinspect

install()
# pyinspect.install_traceback()


from .info import *
from .render import *

def make():
    console = Console()

    table = Table(show_edge=False, show_lines=False, box=None,  show_header=False,
            show_footer=False,)
    table.add_column(justify='right', style='bold red', width=15)
    table.add_column()


    table.add_row('\n\n[bold]Education:', render_education(education))
    table.add_row('\n\nExtracurricular education', render_extracurr_education(extracurr_education))
    table.add_row('\n\nResearch experience', render_experience(research_experience))
    table.add_row('\n\nTeaching experience', render_teaching(teaching_experience))
    table.add_row('\n\nPublications', render_publications(publications))
    table.add_row('\n\nPoster presentations', render_posters(posters))
    table.add_row('\n\nAwards and fellowships', render_awards(awards))

    console.print(table)

    # console.print(
    #     render_education(education), 
    #     render_extracurr_education(extracurr_education),
    #     render_experience(research_experience),
    #     render_teaching(teaching_experience),
    #     render_publications(publications),
    #     render_posters(posters),
    #     render_awards(awards),

    #     render_header(),

    #     sep='\n\n'
    #     )

make()


