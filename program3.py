nama = input ("nama			:")
nim = int(input("nim 		:"))
print(" ")
a= int(input("Masukan laba			: Rp. "))
print(" ")
for x in range(1,9):
	if(x>=1 and x<=2):
		b=a*0
		print("Laba Bulan Ke -",x,"	:Rp. ",b)
		if(x>=3 and x<=4):
			c=a*0.1
			print("Laba Bulan Ke -",x,"	:Rp. ",c)
		if(x>=5 and x<=7):
			d=a*0.5
			print("Laba Bulan Ke -",x,"	 :Rp. ",d)
		if(x==8):
			e=a*0.2
			print("Laba Bulan Ke -",x,"	:Rp. ",e)
total=b+b+c+c+d+d+d+e
print(" ")
print("nama 		:",nama)
print("NIM 			:",nim)
print(" ")
print("\nTotal Laba Adalah		:Rp. ",total)
print(" ")
print("~Terimakasih Sudah Menggunakan Program Ini~")
