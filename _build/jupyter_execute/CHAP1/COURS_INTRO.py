#!/usr/bin/env python
# coding: utf-8

# # <a href="#ici000">Introduction à la programmation scientifique</a><a id="ici000" />

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('autosave', '300')
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML,display


# <div style="width:600px; overflow:auto;">
# <center>
# <a href="#sommaire"><img style=" float:center; display:inline; width:180px;" src="Figures/logo_trans.png" alt="LyonHPC" /></a>
# <img style=" float:center; display:inline; width:180px;" src="Figures/python-logo.gif" alt="LyonHPC"/>
# </center>
# </div>
# <img src="Figures/histoireinfo.png" alt="histoire des ordinateurs" style="width:250px; float:center;"/>

# ## <a href="#sommaire">Contenu de la leçon</a><a name="sommaire"/></a><a href="http://localhost:8888/notebooks/Plan.ipynb"><img style=" float:right; display:inline; width:120px;" src="Figures/logo_trans.png" alt="LyonHPC" /></a>
# 
# <h5>
#     
# 1. <a href="#format">Format du cours</a>
#     
# 2. <a href="#ordinateur">Que peut-on faire avec un ordinateur?</a>
#     
# 3. <a href="#utilite">Utilité d'un ordinateur en science?</a>
#     
# 4. <a href="#algorithme">L'algorithme: la base de la programmation</a>
#     
# 5. <a href="#python">Python comme langage de programmation</a>
#     
# 6. <a href="#objectifs">Objectifs du cours</a>
# </h5>

# <a href="#sommaire"><img style=" float:left" src="Figures/go-home.png"></a><a href="#format"><img style=" float:center" src="Figures/go-next.png"> </a>

# # <a href="#format">Format du cours</a> <a id="format"></a>
# 
# - Utilise un document écrit interactif (*IPython notebook*)
# avec du texte, des diagrammes, des exemples de code
# et des programmes interactifs
#    - Vidéo, notes de cours en PDF , notebook en HTML
# - A la fin de chaque leçon de cours: quiz et exercices en ligne
# - La programmation s'apprend en pratiquant !!
# - Cours basé sur des exemples
# 
# <img src="Figures/exemples.png" style="width:180px;"/>

# <a href="#sommaire"><img style=" float:left" src="Figures/go-home.png"></a><a href="#ordinateur"><img style=" float:center" src="Figures/go-next.png"> </a>

# # <a href="#ordinateur">Que peut-on faire avec un ordinateur ?</a> <a id="ordinateur"></a>
# 
# **Équation de base des ordinateurs (Nick Parlante)**
# >**Ordinateur = <font color='red'>Puissance</font> + <font color='green'>Stupidité</font>**
# 
# - <font color='red'>**puissance**:</font>
# un ordinateur peut traiter des masses de données en exécutant des milliards d'opérations par seconde.
# - <font color='green'>**stupidité**:</font> mais les opérations sont simples et mécaniques et l'ordinateur ne possède aucune capacité d'analyse.
# - <font color='blue'>**l'intelligence**:</font> vient du programme, c'est à dire de l'être humain !
# 
# "The effective exploitation of his powers of abstraction must be regarded as one of the most vital activities of a competent programmer" (Edsger W. Dijkstra)
# 
# Les ordinateurs sont cependant extrêmement utiles. 
# Mais toute l'intelligence est dans le logiciel, d'où *l'importance de connaître les principes de la programmation* pour maîtriser l'outil informatique, particulièrement en science.
# 
# Les ordinateurs actuels ne sont pas les ordinateurs **HAL 9000** (Heuristically programmed ALgorithmic computer), imaginés par de Stanley Kubrick dans *l'odyssée de l'espace* 
# 
# <center>
# <div style="width:600px; overflow:auto;">
# <img style=" float:left; display:inline; width:300px;" src="Figures/odysse1.jpeg" alt="odyssée de l'espace"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# <img style=" display:inline; width:240px;"src="Figures/odysse2.png" alt="odyssée de l'espace"/>
# </div>
# </center>

# <a href="#sommaire"><img style=" float:left" src="Figures/go-home.png"></a><a href="#utilite"><img style=" float:center" src="Figures/go-next.png"> </a>

# # <a href="#utilite">Utilité d'un ordinateur en Science?</a> <a id="utilite"></a>

# Un ordinateur exécute très rapidement des instructions élémentaires codées en binaire: $\approx 4*6000$ MIPS ou bogoMIPS (millions d'instruction par seconde) sur un ordinateur de bureau (Intel Core I5 4 coeurs). Et il les exécute de façon mécanique.

# **Question:**  Comment peut-on utiliser un ordinateur pour simuler un problème physique ?
# 
# Par exemple calculer le mouvement d'un pendule simple, puisque l'ordinateur ne connaît ni la mécanique, ni les équations, ni les méthodes de résolutions de ces équations !
# 
# ## <a href="#ici011">Modélisation numérique</a><a id="ici011" />
# 
# <center><img src="Figures/programmation1.png" alt="Programmation" style="width:400px;"/></center>
# 
# ###<a href="#ici012">**méthode**</a><a id="ici012"></a> 
# le scientifique imagine un algorithme pour résoudre le problème de façon mécanique, et le traduit ensuite dans un langage de programmation pour être exécuté par un ordinateur. Il peut ensuite faire l'étude paramétrique du problème comme avec une expérience.
# 
# 
# <table>
# <tr>
#  <td><img src="Figures/penduleschema.png" alt="Physique" style="width:200px;"/> 
#  </td>
#  <td style="vertical-align:top;"> 
#  **Modèle mathématique** <br>
#  
#  $$ m l \frac{d^2 \theta}{d t^2} = m g \sin(\theta) $$ 
#  $$ Y = [ \theta, \frac{d \theta}{dt} ] $$     
#  $$ Y_0=[\theta_0, 0]$$
#  
#  $$ \frac{d Y}{dt} = F(Y,t) $$     
#  </td>
#  <td style="vertical-align:top;">
# **Algorithme RK2** <br>
# 
# Y = Y0<br>
# Pour i de 1 a n<br>
# &nbsp;&nbsp; Y1 = Y + 0.5 * dt *F(Y,t)<br>
# &nbsp;&nbsp; Y = Y +  dt *F(Y1,t+dt/2)<br>
# &nbsp;&nbsp; t=t+dt<br>
# Fin Pour<br>
#  </td>
# </tr>
# </table>

# ## <a href="#ici013">programmation sous Python</a><a id="ici013"></a>

# In[2]:


import numpy as np
from anim_pendule import Trace
# parametres
g, l = 9.81, 1.
omega = np.sqrt(g/l)
#  second membre de l'EDO
def F(Y):
    return np.array([Y[1], -omega**2*np.sin(Y[0])])
# condition initiale: angle à t=0
theta0 = 0.5*np.pi
Y = np.array([theta0, 0.])
# n=nbre points par période, etude sur 3 periodes
n = 128
dt = 2 * np.pi / omega / n
N = 3 * n
# calcul solution theta
t = np.zeros(N)
theta = np.zeros(N)
theta[0] = theta0
# boucle d'intégration en temps
for i in range(1, N):
    t[i] = t[i-1] + dt
    Y1 = Y + 0.5 * dt * F(Y)
    Y = Y + dt * F(Y1)
    theta[i] = Y[0]
# trace et animation
anim=Trace(l,theta,t)


# In[3]:


HTML(anim.to_html5_video())


# <a href="#sommaire"><img style=" float:left" src="Figures/go-home.png"></a><a href="#algorithme"><img style=" float:center" src="Figures/go-next.png"> </a>

# # <a href="#algorithme">Algorithme</a> <a id="algorithme"></a> 
# <div style="width:600px; overflow:auto;">
# <center>
# <img style=" float:center; display:inline;width:150px;" src="Figures/Euclid_2.jpg" alt="Euclide"/>
# <img style=" float:center; display:inline;width:200px;" src="Figures/Euclide.png" alt="Algorithme"/> 
# <img style=" float:center; display:inline; width:80px;"
# src="Figures/al-khawarizmi.jpg" alt="al-Khwarizmi"/>
# </center>
# </div>

# *Un algorithme est une suite finie et non ambigüe d’opérations ou d'instructions permettant de résoudre un problème*. Les algorithmes sont connus depuis l'antiquité (Euclide). 
# 
# Le mot **algorithme** vient du nom du mathématicien perse du 9ième siècle (AJC) *Abu Abdullah Muhammad ibn Musa al-Khwarizmi*. L'algorithmique correspond à la phase préparatoire avant une quelconque programmation. Elle permet de décrire un problème sous une forme que l'on peut ensuite programmer sur un ordinateur et ceci dans un langage naturel, indépendant d'un langage de programmation. 
# 
# > **algorithme numérique**  suite finie et non ambiguë d’opérations ou d'instructions sur des nombres permettant de résoudre un problème.
# 
# Et il n'est pas nécessaire d'avoir un ordinateur pour exécuter un algorithme (machine de Turing inventé en 1936 avant l’ordinateur)!
# 
# ### <a href="#ici031">Quelques repères historiques</a><a id="ici031"></a>
# 
# - Boulier (12e siècle): 1er abaque (dans # civilisations)
# - Pascaline (1642): 1ere machine à calculer mécanique
# - Arithmométre (1820) (cylindre de Leibnitz 1706)
# - Principe d'un ordinateur (Babbage 1834): machine analytique à partir de cartes perforées
# - Première définition d'un ordinateur (machine de Turing 1936)
# - Premier ordinateur à lampe ENIAC (1943)
# - Premier ordinateur à base de transistors IBM 7000 (1960)
# - Création d'Internet (Arpanet 1969)
# - Premier micro-ordinateur: Micral et Altair 8000 (1973)
# - Micro-ordinateurs personnels : Apple (1976), IBM PC (1981)
# - Loi de Moore (1965) : doublement de la puissance des ordinateurs tous les 18 mois
# - Naissance du système Linux (Linus Torvalds 1991)
# - Supercalculateur Curie (2012) $10^{10}$ fois plus puissant qu'un IBM PC de 1981
# 
# **Puissance de calcul de Curie**  en 1s $\equiv 10^{15} flops $ (peta flops) $\approx$  calcul pendant 48h de la population du globe équipée de boulier  
# 
# <center>
# <img src="Figures/histoireinfo.png" alt="histoire des ordinateurs" style="width:400px;"/>
# </center>

# <a href="#sommaire"><img style=" float:left" src="Figures/go-home.png"></a><a href="#python"><img style=" float:center" src="Figures/go-next.png"> </a>

# # <a href="#python">Python langage de programmation scientifique</a> <a id="python"></a>
# <img src="Figures/zen-of-python.png" style="width:150px;"/>
# 
# ## <a href="#ici041">Historique</a><a id="ici041"></a>
# 
# Créé en 1989 par Guido van Rossum
# 
# - « Benevolent Dictator For Life » (BDFL)
# - **Gratuit, libre et multi-plateformes (portable)** 
# - Le nom provient de la série britannique 
#  - «Monty Python’s Flying Circus» (voir [http://fr.wikipedia.org/wiki/Monty_Python])
# <center>
# <div style="width:600px; overflow:auto;">
# <img style=" float:left; display:inline; width:200px;" src="Figures/ungood-guido-van-rossum.jpeg" alt="Guido_van_Rossum"/>
# <img style=" float:left; display:inline; width:200px;" src="Figures/python.png" alt="Python"/>
# <img style=" float:left; display:inline; width:150px;" src="Figures/Monty-python-flying-circus-theredlist.jpg" alt="Monty-python"/>
# </div>
# </center>
# 
# ## <a href="#ici042">Propriétés</a><a id="ici042"></a>
# 
# - Langage **interprété** (facile à utiliser)
# - **Usage général**: on peut tout faire
#     - interfaces graphiques
#     - calcul scientifique
#     - applications webs
#     - base de données
#     - etc. 
# - **Vaste librairie de modules** (bibliothèques)
# - **Syntaxe cohérente** 
#     - Langage orienté objet 
#     - Langage fonctionnel 
# - **Facile** à apprendre / agréable à utiliser 
# - Excellent premier langage de programmation
# - **Interfaçage facile** avec les autres langages (C/C++, Fortran, Java) 
# - **Défauts ?**
#     - selon les circonstances, les programmes écrits en Python peuvent comporter des problèmes de performance 
#     - mais c’est le cas de tous les langages interprétés

# ## <a href="#ici045">Le Zen de Python</a><a id="ici045"></a> <img style="display:inline; width:40px;" src="Figures/zen.png" />
# 
# Voici 19 règles de programmation Python d'après le BDFL, que l'on trouve sur tout interpréteur python en tapant

# In[4]:


import this


# ## traduction de Cécile Trevian et [Bob Cordeau](http://perso.limsi.fr/pointal/python:courspython3)
# 
# 1. Préfère la beauté à la laideur,
# - Préfère l’explicite à l’implicite,
# - Préfère le simple au complexe
# - Préfère le complexe au compliqué,
# - Préfère le déroulé à l’imbriqué,
# - Préfère l’aéré au compact.
# - Prends en compte la lisibilité.
# - Les cas particuliers ne le sont jamais assez pour violer les règles.
# - Mais, à la pureté, privilégie l’aspect pratique.
# - Ne passe pas les erreurs sous silence, ou bâillonne-les explicitement.
# - Face à l’ambiguïté, à deviner ne te laisse pas aller.
# - Sache qu’il ne devrait avoir qu’une et une seule façon de procéder, même si, de prime abord, elle n’est pas évidente, à moins d’être Néerlandais.
# - Mieux vaut maintenant que jamais.
# - Cependant jamais est souvent mieux qu’immédiatement.
# - Si l’implémentation s’explique difficilement, c’est une mauvaise idée.
# - Si l’implémentation s’explique aisément, c’est peut-être une bonne idée.
# - Les espaces de nommage! Sacrée bonne idée! Faisons plus de trucs comme ça.

# <a href="#sommaire"><img style=" float:left" src="Figures/go-home.png"></a><a href="#objectifs"><img style=" float:center" src="Figures/go-next.png"> </a>

# # <a href="#objectifs">Objectifs du cours</a><a id="objectifs"></a>
# 
# - A la fin de ce cours, vous serez capable d'écrire des programmes à partir d'algorithmes pour résoudre des problèmes scientifiques.
# <img src="Figures/exemples.png" style="display:center; width:200px;"/>
# - Vous maîtriserez les bases du langage de programmation **Python** pour faire du calcul scientifique.
# 
# - Attention: certains aspects du langage Python ne seront pas traités.
# 
# - Mais n'oubliez pas, la programmation, si elle peut être une science ou un art, peut aussi être **ludique**. 
# 
# >*"Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program".*
# 
# Linus Torvalds (créateur de Linux)
# 
# <center>
# <div style="width:600px; overflow:auto;">
# <img style=" float:left; display:inline; width:200px;" src="Figures/LinuxFun.png" alt="Linux"/>&nbsp;&nbsp;&nbsp;&nbsp;
# <img style=" display:inline; width:100px;" src="Figures/linus.jpg" alt="Linux"/>&nbsp;&nbsp;&nbsp;&nbsp;
# <img style=" display:inline; width:180px;" src="Figures/steam_linux.png" alt="Linux"/>
# </div>
# </center>

# # <a href="#fin">Fin de la leçon</a><a id="fin" />
# <div style="width:600px; overflow:auto;">
# <center>
# <img style=" float:center; display:inline; width:180px;" src="Figures/logo_trans.png" alt="LyonHPC" />
# <img style=" float:center; display:inline; width:200px;" src="Figures/python-logo.gif" alt="LyonHPC"/>
# </center>
# </div>
# <img src="Figures/histoireinfo.png" alt="histoire des ordinateurs" style="width:240px;"/>

# In[ ]:




