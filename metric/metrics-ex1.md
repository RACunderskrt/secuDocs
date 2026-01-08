# Exercice 1

| Classe             | LOC | NOM | Responsabilité |
|--------------------|-----|-----|----------------|
| BankAccount        | 462 | 21  | Élevée, car elle contient toute la logique entre les `Person` et les `Bank`. |
| ACHService         | 2   | 2   | Modérée, car c'est une interface standalone qui n'affectera que `ACHServiceImpl` si modifiée. |
| Person             | 325 | 23  | Élevée, elle définit l'objet `Person` utilisé dans les classes `Bank` et dans `BankAccountApp`. |
| BankAccountApp     | 491 | 2   | Faible, car elle utilise toutes les classes définies précédemment mais n'est pas utilisée par une autre classe. |
| ACHServiceImpl     | 10  | 3   | Modérée, car les fonctions retournent uniquement `false`. |
| Bank               | 413 | 14  | Élevée, car elle définit le fonctionnement et les attributs de l'objet `Bank` et est utilisée dans d'autres classes. |
