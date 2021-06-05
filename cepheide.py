# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:13:07 2021

@author: Saadia Bayou
"""

import numpy as np
import matplotlib.pyplot as plt


class Cepheide:
    
    
    def __init__ (self,namefile):
        
        self.courbeLumiere=namefile
         
    
    def __str__(self):
        s="\nLes données de cette etoile Cepheide"\
        " sont contenues dans le fichier : {} "\
        .format(self.courbeLumiere)
        return s

    def fileMat(self):
        """ Retourne une matrice à partir d'un fichier """
        m = np.loadtxt(self.courbeLumiere)
        return m

    def trJrMapp(l1,l2):
        """ Trace le nuage de points de la courbe de lumiere 
        mapp=f(jours)"""
        fig, (courbeLum) = plt.subplots(1)
        courbeLum.invert_yaxis()
        courbeLum.scatter(l1,l2,color="y")
#        courbeLum.plot(l1,l2,'.',color="y")
        plt.title("Courbe de lumiere")
        plt.xlabel ("jours")
        plt.ylabel(" magnetude apparente ")
        plt.savefig("Graphe-Courbe de lumiere Cepheide")
        grphCourbeLum=plt.show()
        return grphCourbeLum 

    def moyenne(l):
        """ Retourne la moyenne d'une liste """
        s=0
        for e in l:
            s+=e
        moy=round(s/len(l))
        return moy
    
    def periode(l,t):
        """" calcul la periode  """
        tmax=[]
        lmax=max(l)
        for i in range(len(l)):  
            if l[i]==lmax:
                tmax.append(t[i])
        p=tmax[1]-tmax[0]
        return p
    
    def trRelCalibree(p):
        pass
        """ Trace la courbe calibrée mabs=f(log(p)) """
    
    def magnAbs(p):
        """ Calcul mabsolue pour une Cepheide 
        à partir de mapp_moyenne de la Cepheide """
        mabs=-2.78*np.log10(p)-1.35
        return mabs
        
    def  distanceGal(mapp_moy,mabs):
        """ Calcul la distance D de la galaxie """
        # formule mapp_moy - mabs= 5*log(D) -5
        k=((mapp_moy-mabs+5)/5)
        D=10**k
        return D
    
    def matFile(namefile,mat):
        """ Créer un fichier à partir d'une matrice"""
        m=np.array(mat)
        f=np.savetxt(namefile,m)
        return f 

def main():
    
    lD=[]
    lmapp_moy=[]
    lp=[]
    
    # Instanciation Cepheide
    
    nf=3 # nombre de fichiers
    for i in range(1,nf+1):
        print("\nCepheide{}".format(i))
        f="dataCourbeLum"+str(i)+".txt"
        print("\nfichier =",f)
        # Instanciation Cepheide
        ceph=Cepheide(f)
        print(ceph)
        # Appel de la fonction fileMat 
        # -> Génère une matrice à partir du fichier de données
        mCeph=ceph.fileMat()
        print("\nmCeph{}={}".format(i,mCeph))
        
        xjr=ceph.fileMat()[:,0]
        ymapp=ceph.fileMat()[:,1]
        # Appel de la méthode de classe trJrMapp
        # -> qui trace la courbe de lumière de la cepheide
        Cepheide.trJrMapp(xjr,ymapp)
        
        jr=mCeph[:,0]
        mapp=mCeph[:,1]
        # Appel de la méthode qui calcule la magnetude apparente moyenne  
        mapp_moy=Cepheide.moyenne(mapp)
        print("mapp_moy_{}={}".format(i,mapp_moy))

        # Appel de la méthode qui calcule la periode     
        p=Cepheide.periode(mapp,jr)
        print("la periode p{}={} jours".format(i,p))
        
        # Appel de la méthode magnAbs qui calcule la magnetude absolue 
        # à partir de la relation calibrée mabs=-2.78*logp -1.35 
        mabs=Cepheide.magnAbs(p)
        print("La magnetude absolue mabs_{} = {}".format(i,round(mabs,2)))
        
        D=Cepheide.distanceGal(mapp_moy,mabs)
        print("La distance D{}={} pc".format(i,D))
        
        lmapp_moy.append(mapp_moy)
        lp.append(p)
        lD.append(D)
        # lD.append(Cepheide.distanceGal(mapp_moy,mabs))
        
    print("\nListe des distances: lD =",lD)
    D_moy=Cepheide.moyenne(lD)
    print("\nLa galaxie Messier 100 se situe à une distance Dmoy =",D_moy,"parsec")
        
    m_res=[lD,lmapp_moy,lp]   
    Cepheide.matFile("Resultats_Ceph.txt",m_res)
        
    # Tracé de la relation calibrée

if __name__=="__main__":
    main()
