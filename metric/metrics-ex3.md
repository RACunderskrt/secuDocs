# Exercice 3

| Classe       | LOC | WMC | CBO | LOCM |
|-------------|-----|-----|-----|------|
| Bank        | 413 | 14  | 3   | 0    |
| BankAccount | 462 | 20  | 2   | 44   |
| Person      | 325 | 23  | 0   | 39   |


Classe avec le CBO le plus élevé : Bank.
Classe avec le WMC le plus élevé : BankAccount.

Grâce à ces informations, on peut déterminer qu'il faudra faire particulièrement attention à la classe `BankAccount` car elle est fortement couplée aux autres classes du projet.