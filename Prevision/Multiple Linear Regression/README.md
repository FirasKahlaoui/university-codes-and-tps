# Régression Linéaire Multiple sur le Jeu de Données mtcars

Ce projet effectue une régression linéaire multiple sur le jeu de données `mtcars`, qui contient des informations sur différentes voitures. L'objectif est d'analyser comment divers facteurs influencent la consommation de carburant (mpg).

## Données

Le jeu de données `mtcars` contient les colonnes suivantes :

- **mpg** : Consommation de carburant (miles per gallon)
- **cyl** : Nombre de cylindres
- **disp** : Cylindrée (displacement)
- **hp** : Puissance (horsepower)
- **drat** : Rapport de transmission (rear axle ratio)
- **wt** : Poids (weight)
- **qsec** : Temps de quart de mile (quarter mile time)
- **vs** : V moteur (0 = V-shaped, 1 = straight)
- **am** : Type de transmission (0 = automatique, 1 = manuelle)
- **gear** : Nombre de rapports de transmission
- **carb** : Nombre de carburateurs

## Analyse

### Modèle de Régression Linéaire

Un modèle de régression linéaire multiple a été ajusté pour prédire `mpg` en fonction des variables explicatives.

### Tests Statistiques

Des tests statistiques ont été réalisés pour vérifier les hypothèses du modèle :

1. **Test d'indépendance (Test de Rainbow)**
   - Résultat : Acceptation de l'hypothèse nulle, indiquant aucune dépendance entre les variables explicatives et les résidus.

2. **Test d'autocorrélation (Test de Durbin-Watson)**
   - Résultat : Acceptation de l'hypothèse nulle, indiquant aucune autocorrélation significative des résidus.

3. **Test d'hétéroscédasticité (Test de Breusch-Pagan)**
   - Résultat : Acceptation de l'hypothèse nulle, indiquant une homoscédasticité des résidus.

4. **Test de normalité (Test de Shapiro-Wilk)**
   - Résultat : Acceptation de l'hypothèse nulle, indiquant que les résidus suivent une distribution normale.

## Conclusion

Les résultats de l'analyse indiquent que le modèle est adéquat et que les hypothèses de base de la régression linéaire sont respectées. Ce projet fournit une compréhension des facteurs influençant la consommation de carburant des voitures.
