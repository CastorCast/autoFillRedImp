# autoFillRedImp

L'objectif de ce projet est de créer un script python pour pouvoir remplir le formulaire 2041-RD qui indique un "Reçu des dons et versements effectués par les particuliers au titre des article 200 et 978 du code général des impôts". Ce formulaire étant sous la forme d'un PDF, n'est pas modifiable sans utiliser un logiciel tierce payant comme Adobe ou gratuit comme InkScape ou LibreOffice et encore lorsque le formulaire est modifié par ces derniers logiciels, il se retrouve graphiquement "cassé". Ce logiciel rentre aussi dans le cadre de l'Association Nijikai.

Le projet sera divisé en trois sous-objectif permettant de guider le projet :
- Un script permettant d'indiqué à l'utilisateur par un prompt/terminal, le formulaire qu'il souhaite remplir, afficher son texte (sur les deux pages) et indiquer les parties qu'il souhaite modifier. Exemple :
Nom ou dénomination :
...........................................................................................
Modification sur "Nom ou dénomination" : Association Nijikai
->
Nom ou dénomination :
Association Nijikai

- Une interface graphique, permettant à l'utilisateur de modifier en direct le document (affichage par PyQt, à voir comment on pourrait faire ça)

- Un script permettant de créer et de remplir automatiquement les formulaires à partir d'un tableur regrouppant l'ensemble des dons et des donnateurs.
