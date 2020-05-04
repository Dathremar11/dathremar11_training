#include <iostream>

int euclid_gcd(int a, int b)
{   // Алгоритм Евклида поиска НОД адаптация С на Ассемблер
loop_begin:
    if (a ==b) goto loop_end;        // Обратное условие к циклу while // Условие выпрыгивание из цикла
    if (!(a > b)) goto else_action;  // Ответвление
    a -= b;                          // Then action, если состоялся то after_if
    goto after_if;
else_action:
    b -= a;
after_if:
    goto loop_begin;                 // Зацикливание
loop_end:                            // Выход из цикла
    return a;
}
