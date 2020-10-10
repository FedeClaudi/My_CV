import pyinspect as pi
pi.install_traceback()


from .make import make_cv, make_pubs, make_projs, make_bio

from rich.console import Console



def show():
    bio = make_bio()

    CV = make_cv()

    pubs = make_pubs()
    
    try:
        projs = make_projs()
    except Exception:  # too many API requests
        print('Could not get projs dammit')
        projs = ''

    # To write to text
    txtconsole = Console(file=open('cv.txt', 'w'))
    txtconsole.print('\n', bio, '\n', CV,  pubs, projs)

    # To print to terminal
    pi.console.print('\n', bio, '\n', CV,  pubs, projs)



