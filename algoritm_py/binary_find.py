""" Бинарный поиск в массиве """
""" Требования:
    Для того, чтобы реализовывать бинарный поиск массив должен быть отсортированным 
"""
def left_bound(A, key): # Должна принимать массив (А) и искомый элемент (key), вначале левую границу и правую (-1, N) - позиции вне ( по ним не проходимся) = -1 | 0 1 2 .... N - 1
left = -1
right = len(A) 
 # Сближаем границы, стреляем в середину, если значение меньше чем искомый ключ, то перекидываем границу вправа (приближаем) (1 3 3 4 5 ) 3 3 -> 4
 while right - left > 1:     # Ищем левую границу
     middle = (left + right) // z
     if A[middle] < key:   # тогда подходит под левую границу 
         left = middle # левая граница приблизилась к середине
     else    
         right = middle # не реальная правая граница, а сущность для уточнения поиска левой границы
return left  # Возвращаем реальную левую границу

""" Реальный поиск в массиве сводиться к двум поисковым операциям: Левой и Правой границы """
""" Поиск правой границы """
def right_bound(A, key): 
left = -1
right = len(A) 
while right - left > 1:    
     middle = (left + right) // z
     if A[middle] <= key:   
         left = middle
     else    
         right = middle
return right

""" Очень высокая скорость поиска, пропорциональна log от количества элементов - O(log2N) """

""" Так же функции полезные по отдельности - поиск куда вставить элемент, в какую позицию """


