import pyinspect as pi
pi.install_traceback()


from .make import make_cv, make_pubs, make_projs


# TODO BIO

# TODO fix links
# TODO fix header



def show():
    # CV = make_cv()

    # pubs = make_pubs()
    
    # projs = make_projs()

    pi.console.print(projs)

show()


