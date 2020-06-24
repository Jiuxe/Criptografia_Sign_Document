import funciones
from random import randint

def generar_clave_DSS():

	q = funciones.siguiente_primo_bits(256)

	c = randint(2**768, 2**769)

	c += c%2
		
	p = (c*q) + 1

	while not funciones.test_miller_rabin(p,50)[0]:
		p += 2*q

	a = 1

	while a == 1:
		g = randint(2,p-2)
		a = funciones.potencia_modular_optimizado(g, (p-1)//q, p)

	x = randint(2,q-2)

	y = funciones.potencia_modular_optimizado(a,x,p)

	with open("publicKey","w") as f:
		 f.write(str(p) + "\n" + str(q) + "\n" + str(a) + "\n" + str(y))

	with open("privateKey","w") as f:
		f.write(str(x))

generar_clave_DSS()
print("***** Claves DSS generadas *****")
