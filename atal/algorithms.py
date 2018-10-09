# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem decrescente de matriculas
def retorna_matriculas_decrescente(alist):
	n = len(alist)
	mergeSort(alist, 0, n-1)
	return alist

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # Listas temporarias
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copia elementos para listas temporarias L[] e R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Junta as listas temporarias antes de arr[l...r]
    i = 0     # Indice inicial da primeira sublista
    j = 0     # indice inicial da segunda sublista 
    k = l     # indice inicial das listas 'mergeadas'
  
    while i < n1 and j < n2 : 
        if L[i] >= R[j]: # Compara o contrario do merge tradicional
						# pois o esperado eh a lista decrescente
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copia elementos restantes de L[] 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copia elementos restantes de R[]
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r): 
    if l < r: 

        m = (l+(r-1))/2

        # Ordena primeira e segunda metade
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 