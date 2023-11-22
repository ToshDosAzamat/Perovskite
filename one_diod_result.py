import matplotlib.pyplot as plt
from file_manager import *
from pv_parameter import *
from jv_fitting_function import *

def result():
    files = findfileinfolder(new_folder,".txt")


    Uoc=[]; Jsc=[]; PCE=[]; FF=[]
    Rs=[]; Rsh=[]; Jph=[]; n=[]
    for file in files:
        data = np.loadtxt(new_folder+"/"+file)
        U = data[:,2]; J = data[:,3]*1000
        Uoc.append(Uocfind(U,J))
        Jsc.append(abs(Iscfind(U,J)))
        PCE.append(abs(PCEfind(U,J, 100)))
        FF.append(abs(FFfind(U,J)))
        pv = one_diod_model_parameter(U, J)
        init_p = [0.01, 1, 1e-10, -16, 1]
        def cost_func(param):
            Rs, Rsh, J0, Jph, n = param
            Jfit = one_diod_model(U, Rs, Rsh, J0, Jph, n)
            cost = np.sum(np.abs(J - Jfit) ** 2)
            return cost


        bounds = [(0, None), (0, None), (None, None), (None, None), (1, 2)]
        res = optimize.minimize(cost_func, init_p, method='Nelder-Mead', bounds=bounds)
        Rs_opt, Rsh_opt, J0_opt, Jph_opt, n_opt = res.x
        Rs.append(Rs_opt*1000); Rsh.append(Rsh_opt*1000); Jph.append(Jph_opt); n.append(n_opt)

        Uu = np.linspace(min(list(U)), max(list(U)))
        Jfit = one_diod_model(Uu, Rs_opt, Rsh_opt, J0_opt, Jph_opt, n_opt)
        plt.plot(U, J, "o", label=f"{file[0:len(file)-4]}")
        plt.plot(Uu, Jfit)

    plt.tight_layout()
    plt.xlabel("V [Volt]")
    plt.ylabel("J [mA/sm2]")
    plt.axvline(0)
    plt.axhline(0)
    plt.grid(True)
    plt.legend()

    plt.savefig("Result/JV.png")



    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    axs[0, 0].plot(files, Uoc, "o-")
    axs[0, 0].set_ylabel("Uoc [Volt]")
    axs[0, 0].grid(True)
    axs[0, 0].set_xticklabels(files, rotation=45, fontsize=6)


    axs[0, 1].plot(files, Jsc, "o-")
    axs[0, 1].set_ylabel("Jsc [mA/sm2]")
    axs[0, 1].grid(True)
    axs[0, 1].set_xticklabels(files, rotation=45, fontsize=6)

    axs[1, 0].plot(files, PCE, "o-")
    axs[1, 0].set_ylabel("PCE [%]")
    axs[1, 0].grid(True)
    axs[1, 0].set_xticklabels(files, rotation=45, fontsize=6)

    axs[1, 1].plot(files, FF, "o-")
    axs[1, 1].set_ylabel("FF [%]")
    axs[1, 1].grid(True)
    axs[1, 1].set_xticklabels(files, rotation=45, fontsize=6)
    plt.savefig("Result/JV_param_1.png")


    figg, ax = plt.subplots(2, 2, figsize=(10, 10))
    ax[0, 0].plot(files, Rs, "o-")
    ax[0, 0].set_ylabel("Rs [Om*sm2]")
    ax[0, 0].grid(True)
    ax[0, 0].set_xticklabels(files, rotation=45, fontsize=6)

    ax[0, 1].plot(files, Rsh, "o-")
    ax[0, 1].set_ylabel("Rsh [Om*sm2]")
    ax[0, 1].grid(True)
    ax[0, 1].set_xticklabels(files, rotation=45, fontsize=6)

    ax[1, 0].plot(files, Jph, "o-")
    ax[1, 0].set_ylabel("Jph [mA/sm2]")
    ax[1, 0].grid(True)
    ax[1, 0].set_xticklabels(files, rotation=45, fontsize=6)

    ax[1, 1].plot(files, n, "o-")
    ax[1, 1].set_ylabel("Ideal Factor [no unit]")
    ax[1, 1].grid(True)
    ax[1, 1].set_xticklabels(files, rotation=45, fontsize=6)
    plt.savefig("Result/JV_param_2.png")





