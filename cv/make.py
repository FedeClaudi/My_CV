from pyinspect._colors import *
import pyinspect as pi

from .info import *
from .render import *


def make_cv():

    hs = f'bold {lightblue2}'


    CV = pi.Report('Federico Claudi - CV', color=salmon, 
        accent=lightsalmon, dim=salmon)
    CV.width=(160)
    
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
    
    # ? publications
    CV.spacer(6)
    CV.add(f'[{hs}]         [underline]Publications')
    CV.spacer()
    CV.add(render_publications(publications), 'obj')
    
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