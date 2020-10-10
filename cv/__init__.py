import pyinspect as pi
pi.install_traceback()


from .make import make_cv, make_pubs


# BIO

# TODO fix links
# TODO fix header



def show():
    CV = make_cv()

    pubs = make_pubs()

    pi.console.print(CV, pubs)

show()


