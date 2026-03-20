# -*- coding: utf-8 -*-
"""
Test sur Machine
04/12/2025
Nom - Prénom : 
"""
import numpy as np
import matplotlib.pyplot as plt
import random as rd

# POUR LES PROFS UNIQUEMENT - Ne pas modifier ni décommenter
#E11,E12,E21, E22, E41,E42,E43 = 0,0,0,0,0,0,0

# Exercice 1 : 

def norme(a, b):
    """
    In : a (flottant), b (flottant)
    Out: flottant (norme de a + ib)
    """    
    return (a**2 + b**2)**(0.5)

def trigo(a, b):
    """
    In : a (flottant), b (flottant)
    Out: liste [flottant, flottant] 
    Pour a, b != 0, 0 renvoie le cosinus et le sinus de l argument
    """  
    return [ a / norme(a, b) , b / norme(a, b) ]

E11 = norme(21, -67)
E12 = trigo(21, -67)


# Exercice 2 :

def suite(n):
    """
    In: n entier naturel
    Out: flottant
    Renvoie u_n
    """
    return ((n+1)**(1 / (n+1))) - (n**(1 / n))

def somme(n):
    """
    In: n entier naturel non nul
    Out: flottant
    Renvoie la somme des n premiers elements de u
    """
    cursomme = 0
    for i in range(1, n):
        cursomme += suite(i)
    return cursomme

E21 = suite(100)
E22 = somme(100)

# Exercice 3 :   

def premier(n):
    """
    In: n entier naturel non nul
    Out: bool
    Renvoie si n est premier
    """
    seuil = int(np.ceil( (n**(1/2)) )) 
    print(seuil)
    for i in range(2, seuil+1):
        if n % i == 0: 
            return False
    return True
    

# Exercice 4 :
TestPistons2 = """linformatiqueomnipresentedanslesdifferentesspheresdelentreprisedelarecherchedesservicesdelacultureetdesloisirsreposesurdesmecanismesfondamentauxdevantetremaitrisesparlesfutursingenieursenseignantsetchercheursquiaurontasenservirpouragirenconnaissancedecausedansleurvieprofessionnellelarapideevolutiondesoutilsinformatiquesetdessciencesdunumeriquedanstouslessecteursdelingenierieindustriellelogicielleetdesservicesetdelarechercherendindispensableunenseignementdelinformatiquespecifiquementconupourletudiantdecpgescientifiquesceluicidevrapouvoirdanssavieprofessionnellecommuniqueraveclesinformaticiensdesonentrepriseoudesonlaboratoireparticiperauxprisesdedecisionenmatieredesystemesdinformationpossederdesconnaissancesdebasenecessairesalacomprehensiondesdefaillancesetdesrisquesinformatiquesainsiquedessolutionspermettantdyremedieretexploiterabonescientlesresultatsdecalculsnumeriquespourcefaireildevracomprendredesconceptstelsquelaprecisionnumeriquelafaisabilitelefficacitelaqualiteetleslimitesdesolutionsinformatiquescequirequiertunecertainefamiliariteaveclesarchitecturesmateriellesetlogicielleslessystemesdexploitationlestockagedesdonneesetlesreseauxcettediversitedexigencesimposeuneformationalafoisfondamentaleetappliqueeauniveaufondamentalonsefixepourobjectiflamaitriseduncertainnombredeconceptsdebaseetavanttoutlaconceptionrigoureusedalgorithmesetlechoixderepresentationsapproprieesdesdonneesceciimposeuneexperiencepratiquedelaprogrammationetdelamanipulationinformatiquededonneesnotammentdorigineexperimentaleouindustrielleetparfoisdisponiblesenligneauniveaudesapplicationslarapiditedevolutiondestechnologieslogiciellesetmateriellesrenforcelinteretdepresenterdesconceptsfondamentauxperennessanssattacheroutremesurealadescriptiondetechnologiesprotocolesounormesactuelsenrevanchelaformationsattacheraacontextualiserleplussouventpossiblelesactivitespratiquesensappuyantsurlesautresdisciplinesscientifiqueschimiephysiquemathematiquessciencestechnologiquesetdelingenieurletudeetlamaitrisedequelquesalgorithmesfondamentauxlutilisationdestructuresdedonneesadapteesetlapprentissagedelasyntaxedulangagedeprogrammationchoisipermettentdedevelopperdesmethodesouparadigmesdeprogrammationappropriesfiablesetefficacesprogrammationimperativeapprochedescendanteprogrammationstructureeutilisationdebibliothequeslogiciellesnotionselementairesdecomplexiteentempsouenmemoiredocumentationdesprogrammesenvuedeleurreutilisationetpossiblesmodificationsulterieureslapratiqueregulieredelaresolutiondeproblemesparuneapprochealgorithmiqueetdesactivitesdeprogrammationquienresultentconstitueunaspectessentieldelapprentissagedelinformatiqueilesteminemmentsouhaitablequelesexempleschoisisainsiquecertainsexercicesdapplicationsoientdirectementinspiresparlesenseignementsdephysiqueetchimiedemathematiquesetdesciencesindustriellesetdelingenieurenfinlescompetencesacquiseseninformatiqueontvocationaparticiperpleinementalelaborationdestravauxdinitiativepersonnelleencadreetipeetaetrereutiliseesauseindesautresenseignementsscientifiques"""

def nbchar(lettre, chaine):
    """
    In: lettre (caractere), chaine (string)
    Out: entier 
    Renvoie de nombre de lettre dans chaine
    """
    c = 0
    for char in chaine:
        if lettre == char:
            c += 1
    return c

def multiple(chaine):
    """
    In: chaine (string)
    Out: bool 
    Renvoie s il existe une lettre qui apparait multiple fois
    """
    for char in chaine:
        if nbchar(char, chaine) > 1:
            return True
    return False

def desordre(mot):
    """
    In: mot (string)
    Out: string 
    """
    res = ""
    idx = [k for k in range(len(mot))]
    for i in range(len(mot)):
        r = rd.randint(0, len(idx)-1)
        curidx = idx[r]
        res += mot[curidx]
        idx = idx[:r] + idx[r+1:]
    return res
    

E41 = nbchar('s', TestPistons2)
E42 = multiple("Pistons2")
E43 = desordre("Pistons2")


# Exercice 5 :

def d6():
    """
    In: None
    Out: entier
    """
    return rd.randint(1, 6)

def d6pipe():
    """
    In: None
    Out: entier
    """
    return 6 if rd.randint(1, 2) == 2 else rd.randint(1, 5)

Tirage_NP = [d6() for i in range(10000)]
Tirage_P = [d6pipe() for i in range(10000)]

# Question 3 - Histogramme dé non pipé
# Pour afficher la figure, décommenter les 3 lignes suivantes
plt.figure(1)
plt.hist(Tirage_NP)
plt.show()


# Question 6 - Histogramme dé pipé
# Pour afficher la figure, décommenter les 3 lignes suivantes
plt.figure(2)
plt.hist(Tirage_P)
plt.show()



# POUR LES PROFS UNIQUEMENT - Ne pas modifier ni décommenter

print('Exercice 1')
print('E11 = ', E11,'\n')
print('E12 = ', E12,'\n')

print('Exercice 2')
print('E21 = ', E21)
print('E22 = ', E22, '\n')


print('Exercice 3')
print(premier(3)==True, premier(4)==False, premier(11)==True, premier(12)==False, premier(73)==True, premier(222)==False)

print('Exercice 4')
print('E41 = ', E41)
print('E42 = ', E42, '\n')
print('E43 = ', E43, '\n')

print('Exercice 4')
print('Tirage_NP = ', Tirage_NP, '\n')
print('Tirage_P = ', Tirage_P, '\n')





