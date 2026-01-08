# Exercice 2

Je vais me baser sur la fonction `withdrawMoney` de la classe `BankAccount`.
```java
public boolean withdrawMoney(double withdrawAmount) {
	if (withdrawAmount >= 0 && balance >= withdrawAmount && withdrawAmount < withdrawLimit
			&& withdrawAmount + amountWithdrawn <= withdrawLimit) {
		balance = balance - withdrawAmount;
		success = true;
		amountWithdrawn += withdrawAmount;
	} else {
		success = false;
	}
	return success;
}
	
```

Le CC de cette fonction est de 5.
Dans cette fonction, les 5 points de décisions sont :
- Dans le `if`, avec les 4 comparaisons.
- Dans le `else`.

On pourrait minimiser ce chiffre en créant une fonction `checkWithDrawAmount` qui retourne un bool et qui sera utilisé par la fonction `withdrawMoney`.

```java
private boolean checkWithdrayAmount(double withdrawAmount){
	return withdrawAmount >= 0 && balance >= withdrawAmount && withdrawAmount < withdrawLimit && withdrawAmount + amountWithdrawn <= withdrawLimit
}

public boolean withdrawMoney(double withdrawAmount) {
	if (checkWithdrayAmount(withdrawAmount)) {
		balance = balance - withdrawAmount;
		success = true;
		amountWithdrawn += withdrawAmount;
	} else {
		success = false;
	}
	return success;
}
```