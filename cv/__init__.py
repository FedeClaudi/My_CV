import pyinspect as pi
pi.install_traceback()


from .make import make_cv, make_pubs, make_projs, make_bio


# TODO BIO

# TODO fix links
# TODO fix header



def show():
    bio = make_bio()

    CV = make_cv()

    pubs = make_pubs()
    
    try:
        projs = make_projs()
    except Exception:  # too many API requests
        print('Could not get projs dammit')
        projs = ''


    pi.console.print( '\n', bio, '\n', CV, pubs, projs)



