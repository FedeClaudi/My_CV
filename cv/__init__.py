from rich import print
from rich.pretty import install
import pyinspect

install()
# pyinspect.install_traceback()


from .info import *
from .render import *

def make():
    print(
        render_education(education), 
        render_extracurr_education(extracurr_education),
        render_experience(research_experience),
        render_teaching(teaching_experience),
        render_publications(publications),

        sep='\n\n'
        )

make()


