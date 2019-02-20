def perulangan():

	print(" ")

	max=0
	while True :
		a=int(input("Masukan Bilangan = "))
		if max < a:
			max = a
		if a==0:

			print(" ")
			print("Bilangan Terbear =" ,max)
			print(" ")
			print("Terimakasih Telah Menggunakan Program Ini")
			print(" ")
			print("DILARANG MENG COPY PROGRAM INI")
			PRINT(" ")
			jawab = "ya"
			while jawab =="ya":
				jawab =input("Ingin Mengulang Program Ini ? (ya/tidak)")
				if jawab == "ya":
					return perulangan()
				elif jawab =="tidak":
					break
				print(" ")
perulangan()