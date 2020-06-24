import funciones
from random import randint
from hashlib import sha256

def firmarFichero(documento, clave_publica, clave_privada):

	with open(clave_publica,'r') as f:
		p, q = int(f.readline()), int(f.readline())
		a, y = int(f.readline()), int(f.readline())

	with open(clave_privada,'r') as f:
		x = int(f.readline())

	# Obtenemos el resumen del documento usando SHA2
	with open(documento, 'rb') as f:
		hm = int(sha256(f.read()).hexdigest(), 16)

	k = randint(2, q-2)

	r = funciones.potencia_modular_optimizado(a,k,p)%q

	inverso = funciones.inverso(k,q)

	s = ((hm + x*r) * inverso) % q

	with open("FirmaDDS_" + documento, 'w') as f:
		f.write(str(r) + "\n" + str(s))

firmarFichero("textoParaFirmar.txt","publicKey","privateKey")
print("*---- Fichero Firmado Correctamente ----*")