booklist=["Tom gates","Harry potter","Diary of a wimpy kid"]
while(True):
	print("press 1 to ;list the books")
	print("press 2 to ;give a new book")
	print("press 3 to ;delete a book")
	ops=int(input("what you want to do"))
	if ops==1:
		print(booklist)
	if ops==2:
		newbook=str(input("give me new book"))
		booklist.append(newbook)
		print(booklist)
	if ops==3:
		x=int(input("which book do you want to delete"))
		del booklist[x]


