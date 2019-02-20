def perulangan():


	print(" ")

	import random
	a = 0
	jumlah = int(input("Masukan jumlah	N	: "))

	print(" ")

	for x in range(0,jumlah):
		i=random.uniform(0.0,0.5)
		a+=1
		print("data ke-",a,"=>",i)
	print(" ")
	print("Terimakasih sudah menggunakan program ini ")
	print(" ")
	print("DILARANG MENG COPY PROGRAM INI")
	print(" ")


	jawab = "ya"
	hitung = 0
	while jawab == "ya":
		hitung += 1
		jawab = input("Ingin mengulang program ini ? (ya/tidak)")
		if jawab =="ya":
			return perulangan()
		elif jawab =="tidak":
			break
		print("Total perulangan : ",hitung)
perulangan()