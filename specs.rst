#########################################
Specification: Widget Textable TreeTagger
#########################################



1 Introduction
**************


1.1 But du projet
=================
Créer un Widget Textable [#]_ qui utilise TreeTagger_ pour annoter un texte.

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

* Jean Dupont `jean.dupont@unil.ch`_ :

.. _jean.dupont@unil.ch: mailto:jean.dupont@unil.ch

    - Documentation
    - Test

* Anselme Matheux `Anselme@exemple.net`_ :

.. _Anselme@exemple.net: mailto:anselme@exemple.net

    - Specification
    - Interface
    - GitHub


2. Technique
************
  


2.1 Mock-up de l'interface
==========================
..
  pensez à bien définir toutes les fenêtres.


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
    en, fr
  - quelques autres options
  

2.3 Fonctionnalités principales
===============================
..
    - plus d'options

2.4 Fonctionnalités optionelles
===============================



2.5 Tests
=========



3. Etapes
*********



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
Le projet est disponible sur GitHub à l'adresse ...
