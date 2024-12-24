import pandas as pd
def razdelenie_po_polu():
    df = pd.read_csv('random/NISPUF17.csv')

    got_vac=df[df['P_NUMVRC']>0] 
    ms=got_vac[got_vac['SEX']==1]
    mnocpox=len(ms[ms['HAD_CPOX']==2])
    menratio=len(ms[ms['HAD_CPOX']==1])/mnocpox
 
 
    ws=got_vac[got_vac['SEX']==2]
    wnocpox=len(ws[ws['HAD_CPOX']==2])  
    wratio=len(ws[ws['HAD_CPOX']==1])/wnocpox
    sootn={'male':menratio,'female':wratio}

    return sootn


print(razdelenie_po_polu())