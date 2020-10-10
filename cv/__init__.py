import pyinspect as pi
pi.install_traceback()


from .make import make_cv



# TODO: detailed publications Report
# TODO: scholar report

# TODO fix links
# TODO fix header



def show():
    CV = make_cv()


    pi.console.print(CV)

show()


