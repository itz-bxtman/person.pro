def bubble_sort(vector):
  n = len(vector)
  for i in range (n-1):
      for j in range (0 , n-i-1):
          if vector[j] > vector[j + 1]:
              vector[j] = vector[j + 1]
  return vector

def selection_sort(vector):
  n = len(vector)
  for i in range(0,n-1):
      n = i
      for j in range(i+1 , n-1):
          if vector[j] < vector[n]:
              n = j
      if n != i:
        y = vector[i]
        vector[i] = vector[n]
        vector[n] = y
  return vector

def insertion_sort(vector):
  n = len(vector)

  for i in range(1,n):
      n = vector[i]
      j = i - 1
      while j >= 0 and n < vector[j]:
          vector[j + 1] = vector[j]
          j -= 1
      vector[j + 1] = n
  return vector

def quick_sort(vector, inicio, fin):
  if inicio < fin:
    piv = particionar(vector, inicio, fin)
    quick_sort(vector, inicio, piv - 1)
    quick_sort(vector, piv + 1, fin)
  return vector    

def particionar(vector, inicio, fin):
    piv = vector[fin]
    i = inicio - 1

    for j in range(inicio, fin):
        piv = vector[j]
        if vector[j] <= piv:
            i = i + 1
            vector[i] = vector[j]
    vector [i + 1] = vector[fin]
    return i + 1

def main():
    while True:
        print("Menú:")
        print("1. Ordenamiento Burbuja (Bubble Sort)")
        print("2. Ordenamiento por Selección (Selection Sort)")
        print("3. Ordenamiento por Inserción (Insertion Sort)")
        print("4. Ordenamiento Rápido (Quick Sort)")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            vector = [int(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
            bubble_sort(vector)
            print("Lista ordenada:", vector)
        elif opcion == "2":
            vector = [int(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
            selection_sort(vector)
            print("Lista ordenada:", vector)
        elif opcion == "3":
            vector = [int(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
            insertion_sort(vector)
            print("Lista ordenada:", vector)
        elif opcion == "4":
            vector = [int(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
            quick_sort(vector)
            print("Lista ordenada:", vector)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()
