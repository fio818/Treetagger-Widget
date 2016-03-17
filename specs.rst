#########################################
Specification: Widget Textable TreeTagger
#########################################

htrtzd

1 Introduction
**************

1.1 But du projet
=================
Créer un Widget Textable Treeanalysis qui utilise TreeTagger_ pour annoter un texte segmenté.

.. [#] Dernière version en python 2 disponible
.. _TreeTagger: http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/

1.2 Aperçu des etapes
=====================
* Premiere version de la specification: 17 mars 2016
* Remise de la specification: 24 mars 2016
* Version alpha du projet:  28 avril 2016
* Remise et presentation du projet:  26 mai 2016

1.3 Equipe et responsabilitées
==============================


*Xavier Barros: xavier.barros@unil.ch
        -code
        -test
        -github dealer

*Fiona Testuz: fiona.testuz@unil.ch
        -code
        -documentation
        -specification
        -interface
        
*Michael Wuethrich: michael.t.wuethrich@live.fr
        -test
        -code
        -specification
        
*Chloe Beutler: chloe.beutler@unil.ch
        -code
        -documentation
        -specification
        
*Gaetan Schneider: gaetan.schneider@unil.ch
        -code
        -documentation



2. Technique
************
Orange 2.7
Orange Textable 1.5.2
Treetagger  
Python Subprocess


2.1 Mock-up de l'interface
==========================



2.2 Fonctionnalités minimales
=============================
..
  - input: segments (textes)
  - output: segments annotées (annotation: TAG, annotation: segment d'origine)
  
  +------------------+      +-------+------------------------+----------------------+
  | segment 1 PHRASE | -->  | Mot 1 | annotation: segment: 1 | annotation: TAG: NOM |
  +------------------+      +-------+ -----------------------+----------------------+
  | segment 2 TEXTW  |
  +------------------+
  - annoter 2 langues (disponibles)
    en, fr (français par défaut)
  - quelques autres options
  

2.3 Fonctionnalités principales
===============================
Segmentation Treetagger
Utilisation de lemmes
Output autant de segmentations que de tokens


2.4 Fonctionnalités optionelles
===============================
Choix de langue 


2.5 Tests
=========
Le widget fonctionne si les fonctionnalités minimales et principales fonctionnent (2.2 et 2.3)


3. Etapes
*********
Création d'un compte Github
Cahier des charges
Interface
Recherche et documentation

Codage 
Intégration à Orange Textable

Tester le widget raccourci Treetagger 
Le raccourci Treetagger passe par la fonction recode 
Une fois le recode accompli, utilisation de la fonction xml

3.1 Version alpha
=================
* L'interface graphique est complétement construite.
* Les fonctionnalités minimales sont prises en charge par le logiciel.



3.2 Remise et présentation
==========================
* Les fonctionnalités principales sont complétement prises en charge par le logiciel.
* La documentation du logiciel est complète.
* Le logiciel possède des routines de test de ses fonctionnalitées (principales ou optionelles.


4. Infrastructure
=================
Le projet est disponible sur GitHub à l'adresse https://github.com/xbarros/Treetagger-Widget 
