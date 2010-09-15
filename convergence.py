"""
Script for running convergence tests.
"""
import pylab as pl

def ctest(methods,ivp,T,grids=[20,40,80,160,320,640]):
    """
        Runs a convergence test and creates a plot of the results.

        INPUTS:
            methods -- a list of ODEsolver instances
            ivp     -- an IVP instance
            T       -- a list of two numbers indicating the
                       initial and final times of integration.
                       If the first is omitted, it is assumed zero.
            grids   -- a list of grid sizes for integration.
                       optional; defaults to [20,40,80,160,320,640]

        EXAMPLES:

            import runge_kutta_method as rk
            from ivp import *
            rk44=rk.loadRKM('RK44')
            myivp=nlsin_fun()
            T=[0.,5.]
            ctest(methods,myivp,T)

            TODO: 
                - Option to plot versus f-evals or dt

    """
    pl.clf(); pl.draw(); pl.hold(True)
    # In case just one method is passed in (and not as a list):
    if not isinstance(methods,list): methods=[methods]
    err=[]
    for method in methods:
        print method.name
        err0=[]
        for i in range(len(grids)):
            N=grids[i]
            t,u=method(ivp.rhs,ivp.u0,T,N=N)
            err0.append(abs(u[-1]-ivp.exact(t[-1])))
        err.append(err0)
        work=[grid*len(method) for grid in grids]
        pl.loglog(work,err0,label=method.name)
        pl.xlabel('Function evaluations')
        pl.ylabel('Error at $t_{final}$')
    pl.legend()
    pl.hold(False)
    pl.draw()
    pl.ioff()
    return err