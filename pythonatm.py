print("welcome")
balance=0
pin=1234
chance=0
while chance <3:
	epin=int(input("enter your pin :"))
	if pin == epin:
		chance=0
		print("weelcome")
		print("1.balance\n 2.pinchange 3.deposite\n 4.withdraw\n 5.exist")
		choose=int(input("enter your options :"))
		if choose==1:
			print("your balane",balance)
		elif choose ==2:
			npin=int(input("enter your pin:"))
			pin == npin
			print("pin successfully")
		elif choose == 3:
			amount=int(input("enter your amount"))
			balance += balance
			print("your balance is :")
		elif choose == 4:
			amount=int(input("enter amount:"))
			if amount > balance :
				print("insufficient balance")
			else:
				balance = balance - amount
				print("your currenyt balance is ",balance)
		elif choose==5:
			break
	else:
		print("incorrect pin")
		chance +=1