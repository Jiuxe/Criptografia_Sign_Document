import funciones
from hashlib import sha256

def comprobarFirmaDocumento(firma, documento, clave_publica):

	with open(clave_publica, 'r') as f:
		p, q = int(f.readline()), int(f.readline())
		a, y = int(f.readline()), int(f.readline())

	with open(firma,'r') as f:
		r, s = int(f.readline()), int(f.readline())

	inversa_s = funciones.inverso(s, q)

	with open(documento,'rb') as f:
		hm = int(sha256(f.read()).hexdigest(), 16)
	print(q)
	print(hm)

	u = (inversa_s*hm) % q
	v = (r * inversa_s) % q

	r2 = ((funciones.potencia_modular_optimizado(a,u,p) * funciones.potencia_modular_optimizado(y,v,p)) % p) % q

	if r2 == r:
		print("----- FIRMA CORRECTA -----")
	else:
		print("***** FIRMA INCORRECTA *****")

comprobarFirmaDocumento("FirmaDDS_textoParaFirmar.txt", "textoParaFirmar.txt", "publicKey")