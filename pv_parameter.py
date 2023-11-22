
def Uocfind(Uu,Ii):
    U = list(Uu); I = list(Ii)
    I_mus=[i for i in I if i>0]
    I_mus_min=min(I_mus)
    I_mis_min_index=I.index(I_mus_min)
    return U[I_mis_min_index]
def Iscfind(Uu,Ii):
    U = list(Uu);I = list(Ii)
    U_mus=[u for u in U if u>0]
    U_mus_min=min(U_mus)
    U_mis_min_index=U.index(U_mus_min)
    return I[U_mis_min_index]
def Umaxfind(Uu,Ii):
    U = list(Uu);I = list(Ii)
    pv_list=[u*i for u,i in zip(U,I)]
    pv_list_min=min(pv_list)
    pv_min_index=pv_list.index(pv_list_min)
    return U[pv_min_index]
def Imaxfind(Uu,Ii):
    U = list(Uu);I = list(Ii)
    pv_list=[u*i for u,i in zip(U,I)]
    pv_list_min=min(pv_list)
    pv_min_index=pv_list.index(pv_list_min)
    return I[pv_min_index]
def Pmaxfind(Uu,Ii):
    U = list(Uu);
    I = list(Ii)
    return Umaxfind(U,I)*Imaxfind(U,I)

def FFfind(Uu,Ii):
    U = list(Uu);I = list(Ii)
    FF=(Pmaxfind(U,I))*100/(Uocfind(U,I)*Iscfind(U,I))
    return FF

def PCEfind(Uu,Ii,Inten):
    U = list(Uu);I = list(Ii)
    PCE=(Pmaxfind(U,I))*100/(Inten)
    return PCE
