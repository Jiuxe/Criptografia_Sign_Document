from random import randint

def potencia_modular_optimizado(a,b,m):

	p=1
	while b > 0:
		if b%2==1:
			p=(p*a)%m
		b= b//2
		a = (a*a)%m

	return p

def funcion_descomposicion(n):
	u = 0
	s = n

	while s%2 == 0:
		u = u+1
		s = s//2
	return u,s

def test_miller_rabin(n,a=-1):

	# Descomponemos n-1 como 2**u * s (s es impar)
	u, s = funcion_descomposicion(n-1)
	
	# Si no introducimos ningun argumento en a se genera un testigo aleatorio
	if a == -1:
		a = randint(2,n-2)
	
	testigo = a

	# Calculamos a = a**s mod n
	a = potencia_modular_optimizado(a,s,n)

	# Si a = 1 o a = n-1 --> n es probable primo
	if a == 1 or a == n-1:
		return True, testigo

	# Desde i = 1 hasta n-1
	for i in range(u-1):
		
		# a = a**2 mod n
		a = (a*a)%n

		# Si a = 1 --> n no es primo
		if a == 1:
			return False, testigo

		# Si a = n-1 --> n es probable primo
		if a == n-1:
			return True, testigo

	# n no es primo
	return False, testigo

def comprobar_primo(n,m=20):

	siprimo=0
	for i in range(m):
		primo, testigo = test_miller_rabin(n)
		if primo == False:
			return False

	return True

def siguiente_primo(num):
	if num%2 == 0:
		sig_primo=num+1
	else:
		sig_primo=num+2
	
	while comprobar_primo(sig_primo,20) != True:
		sig_primo=sig_primo+2
	
	return sig_primo

def siguiente_primo_fuerte(num):

	segundo_primo = siguiente_primo(num//2)
	  
	while comprobar_primo((segundo_primo*2)+1,20) != True:
		segundo_primo = siguiente_primo(segundo_primo)

	return (segundo_primo*2)+1

def siguiente_primo_fuerte_bits(num):

	a = randint(2**(num-1), 2**(num))
	primo_fuerte = siguiente_primo_fuerte(a)
	  
	return primo_fuerte

def siguiente_primo_bits(num):

	a = randint(2**(num-1), 2**(num))
	primo = siguiente_primo(a)
	  
	return primo

def mcd_ex(a,b):
    (u0,u1)=(1,0)
    (v0,v1)=(0,1)
    while b > 0:
        (c,r) = (a//b, a%b)
        (u0,u1) = (u1,u0-c*u1)
        (v0,v1) = (v1,v0-c*v1)
        (a,b) = (b, a%b)
    return [a,u0,v0]

def inverso(a,n):
    u = mcd_ex(a,n)
    if u[0] == 1:
        return(u[1])
    else:
        print('No existe el inverso')
        return(0)
