# Analyse de Régression Linéaire

## Description

Ce projet effectue une analyse de régression linéaire entre les variables \(X\) et \(Y\) à l'aide de R. Il comprend des tests de diagnostic pour vérifier les hypothèses du modèle de régression.

## Tests d'hypothèses

1) **Test d'indépendance entre \(X\) et \(e\) (Test de Rainbow)**  
   \( H_0 : \) indépendance entre \(X\) et \(e\) vs \( H_1 : \) dépendance entre \(X\) et \(e\)  
   Résultat : p-value = 0.08 > 0.05, on accepte \(H_0\).

2) **Test d'autocorrélation des erreurs (Test de Durbin-Watson)**  
   \( H_0 : \) pas d'autocorrélation des résidus vs \( H_1 : \) autocorrélation des résidus  
   Résultat : p-value = 0.07 > 0.05, on accepte \(H_0\).

3) **Test d'hétéroscédasticité des résidus (Test de Breusch-Pagan)**  
   \( H_0 : \) homoscédasticité des résidus vs \( H_1 : \) hétéroscédasticité des résidus  
   Résultat : p-value = 0.90 > 0.05, on accepte \(H_0\).

4) **Test de normalité des résidus (Test de Shapiro-Wilk)**  
   \( H_0 : \) normalité des résidus vs \( H_1 : \) non normalité des résidus  
   Résultat : p-value = 0.72 > 0.05, on accepte \(H_0\).

## Résultats

Le modèle de régression prédit une valeur de \(Y\) pour \(X = x\).

## Conclusion

Ce script fournit une analyse de régression simple et des tests diagnostics essentiels pour évaluer la validité du modèle.
