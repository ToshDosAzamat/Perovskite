
import numpy as np
from scipy import optimize
from scipy.special import lambertw


def one_diod_model(V, Rs, Rsh, J0, Jph, n):
    k=1.38e-23; T=300; e=1.6e-19
    Vt=k*T/e
    z= ((Rs*J0)/(n*Vt*(1+(Rs/Rsh))))*np.exp((Rs*(Jph+J0)+V)/(n*Vt*(1+(Rs/Rsh))))
    J = ((Jph+J0-(V/Rsh))/(1+(Rs/Rsh)))-(n*Vt/Rs)*lambertw(z)
    return -J.real
init_p = [0.01, 1, 1e-10, -18, 1]
def one_diod_model_parameter(U,J):
    def cost_func(param):
        Rs, Rsh, J0, Jph, n = param
        Jfit = one_diod_model(U, Rs, Rsh, J0, Jph, n)
        cost = np.sum(np.abs(J - Jfit) ** 2)
        return cost
    res = optimize.minimize(cost_func, init_p, method='Nelder-Mead')
    Rs_opt, Rsh_opt, J0_opt, Jph_opt, n_opt = res.x
    return [Rs_opt, Rsh_opt, J0_opt, Jph_opt, n_opt]


