import numpy as np
import pandas as pd
from scipy import linalg

def RCA(pivot):

    country_share = pivot.div(pivot.sum(axis=1), axis=0)
    product_share = pivot.sum(axis=0) / pivot.sum(axis=0).sum()
    rca = country_share / product_share
    M = np.heaviside(rca - 1, 1.0)
    
    return M

def M_to_Mhat(M):
    # k_c = country . k_p = product. D = diversity, U = ubiquity
    M = M.dropna().values

    k_c = M.sum(axis=0) # diversity
    k_p = M.sum(axis=1) # ubiquity
    D = np.diag(k_c)
    U = np.diag(k_p)

    S_tilde = (M.T).dot(np.linalg.inv(U)).dot(M)
    S_hat = (M).dot(np.linalg.inv(D)).dot(M.T)

    M_tilde = np.linalg.inv(D).dot(S_tilde)
    M_hat = np.linalg.inv(U).dot(S_hat)

    return M_hat, M_tilde

def Mtilde_to_complexity(M_tilde, M, type='eci'):
    # the PCI is the eigenvector associated with the second largest right eigenvalue of M_hat: M_hat * eci = lambda*eci
    # from the docs: a   eigvec[:,i] = eigval[i]        b   eigvec[:,i]
    eigenValues, eigenVectors = linalg.eig(M_tilde)

    idx = eigenValues.argsort()[::-1]   
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:,idx]

    # take second largest eigenvector
    pci = np.real(eigenVectors[:, 1])
    
    idx = pci.argsort()[::-1]
    if type == 'eci':
        pci_list = M.dropna(axis=1).columns[idx]
    elif type == 'pci':
        pci_list = M.dropna().index[idx]

    return pci, pci_list

def pivot_to_eci_pci(pivot):
    M = RCA(pivot)
    M_hat, M_tilde = M_to_Mhat(M)

    
    eci, eci_list = Mtilde_to_complexity(M_tilde, M, type='eci')
    pci, pci_list = Mtilde_to_complexity(M_hat, M, type='pci')

    #normalise
    eci = (eci - eci.mean()) / eci.std()
    pci = (pci - pci.mean()) / pci.std()
    
    return M, eci, eci_list, pci, pci_list