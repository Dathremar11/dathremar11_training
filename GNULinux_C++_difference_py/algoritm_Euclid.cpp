#include <iostream>

int euclid_gcd(int a, int b)
{   // Алгоритм Евклида поиск НОД
    while (a != b) {
        if (a > b) {     // Если в if одно действие,  
            a -=b;       // то фигурные скобки в цикле if не обязательны, однако (!):
//         cout << "1"; - команда не в цикле if 
        } else {      // отрывается от if
            b -= a;   // добавление {} в циклах решает эту проблему
        }             // Доп. Дурокоустойчивость
    }
    return a;
//  cout << "Never" // Строка не выполняется никогда
}                   // так как return выполняется перед cout
                    // и возвращает a
int main()
{   // В IDE есть переход на парную скобку
    using namespace std;
    int x, y;

    cout << "Enter integer. x =";
    cin >> x;
    cout << "Enter integer. y =";
    cin >> y;
    cout << "GCD(x, y =" << euclid_gcd(x, y) << endl

    return 0;
}
