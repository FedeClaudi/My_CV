from rich.console import Console
from rich.pretty import install
from rich.table import Table
import pyinspect as pi

install()
pi.install_traceback()

from pyinspect._colors import salmon


from .info import *
from .render import *


# TODO color dates nicely
# TODO highlight titles and names
# TODO dim other stuff ?
# TODO make it prettier!
# TODO clean code

# TODO finish and fill in new info !!

# TODO add link/overview of scholar account

def make():
    hs = 'bold {salmon}'

    CV = pi.Report('Federico Claudi - CV')
    CV.width=(160)
    

    CV.add(f'[{hs}]         Education:')
    CV.add(render_education(education), 'obj')
    
    CV.spacer(2)
    CV.add(f'[{hs}]         Extracurricular education')
    CV.add(render_extracurr_education(extracurr_education), 'obj')
    
    CV.spacer(2)
    CV.add(f'[{hs}]         Research experience')
    CV.add(render_experience(research_experience), 'obj')
    
    CV.spacer(2)
    CV.add(f'[{hs}]         Teaching experience')
    CV.add(render_teaching(teaching_experience), 'obj')
    
    CV.spacer(2)
    CV.add(f'[{hs}]         Publications')
    CV.add(render_publications(publications), 'obj')
    
    CV.spacer(2)
    CV.add(f'[{hs}]         Poster presentations')
    CV.add(render_posters(posters), 'obj')
    
    CV.spacer(2)
    CV.add(f'[{hs}]         Awards and fellowships')
    CV.add(render_awards(awards), 'obj')


    CV.print()

make()


