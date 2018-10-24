#coding: utf-8

import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado

# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda

solucaoParcial = []
melhorSolucao = []
resolvido = False
melhorNumMoedas = -1

def retorna_minimo_moedas(valor, tipos_moedas):
	print valor, tipos_moedas
	global solucaoParcial
	global melhorSolucao
	global resolvido
	global melhorNumMoedas
	solucaoParcial = []
	melhorSolucao = []
	resolvido = False
	melhorNumMoedas = -1
	solucaoParcial = [0 for i in range(len(tipos_moedas))]
	melhorSolucao = [0 for i in range(len(tipos_moedas))]
	tipos_moedas.sort(reverse=True)
	retorna_minimo_moedas_backtrack(tipos_moedas, valor, 0)
	return melhorNumMoedas

def solucaoPossivel(numMoedas, valor):
	global resolvido
	global melhorNumMoedas
	if valor < 0:
		return False
	elif resolvido and valor > 0 and numMoedas+1 >= melhorNumMoedas:
		return False
	return True

def retorna_minimo_moedas_backtrack(tipos_moedas, valor, numMoedas):
	global melhorNumMoedas
	global solucaoParcial
	global melhorSolucao
	global resolvido
	for i in range(len(tipos_moedas)):
		solucaoParcial[i] += 1
		valor -= tipos_moedas[i]
		numMoedas += 1
		if solucaoPossivel(numMoedas, valor):
			if valor == 0:
				if not resolvido or numMoedas < melhorNumMoedas:
					melhorNumMoedas = numMoedas
					resolvido = True
			else:
				retorna_minimo_moedas_backtrack(tipos_moedas, valor, numMoedas)
		solucaoParcial[i] -= 1
		valor += tipos_moedas[i]
		numMoedas -= 1

# Outras tentativas backtracking, no entanto notei que o custo
# eh sempre quase igual ao custo de forca bruta para o problema do troco
""" def troco_backtrack(indice, tipos_moedas, valor):
	if valor == 0:
		return 0
	if indice < len(tipos_moedas) and valor > 0:
		valor_maximo = valor / tipos_moedas[indice]
		minMoedas = sys.maxint
		for i in range(valor_maximo):
			if valor >= (i * tipos_moedas[indice]):
				resultado = troco_backtrack(indice+1, tipos_moedas, valor - (i * tipos_moedas[indice]))
				if resultado != -1:
					minMoedas = min(minMoedas, resultado + i)
		
		return -1 if minMoedas == sys.maxint else minMoedas
	
	return -1

def backtrack(valor, tipos_moedas, numMoedas):
	resultados = [[]]
	for moeda in tipos_moedas:
		resultado = []
		resultado.append(moeda)
		valor_atual = valor - moeda
		if valor_atual >= 0:
			if valor_atual == 0:
				resultados.append(resultado)
			else:
				if numMoedas - 1 > 0:
					resultados_backtrack = backtrack(valor_atual, tipos_moedas, numMoedas - 1)
					for resultado_backtrack in resultados_backtrack:
						resultado_backtrack.append(moeda)
					resultados += resultados_backtrack
	return resultados
 """