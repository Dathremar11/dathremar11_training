<?php /*
mysqli_real_escape_string()



- эта функция экранирует специальные символы в строке для использования в SQL-выражении .
- первым параметром принимает индификатор соединения - $db
- вторым параметром - строку, которую требуется экранировать - $str .
Возвращает экранированную строку.
*/
?>

-- файл index.php --

<?php
...
...
...

// создадим строку с апострофом
$str = "d'Artanian";
// вернем в переменную $str, обработанную функцией нашу же переменную $str
$str = mysqli_real_escape_string($db , $str );

// Запрос к базе данных (добавим новые данные в нашу таблицу - строку с апострофом)
$query = "INSERT INTO gb (name, text) VALUES ( $str , 'Имя с апострофом')"; // готовим запрос
mysqli_query ($db , $query ) or die(mysqli_error($db )); // выполняем запрос

// Запрос к базе данных (выбираем данные из нашей таблицы)
$res = mysqli_query( $db , "SELECT name, text, date FROM gb ORDER BY id DESC" ); // выполняем запрос

$date = mysqli_fetch_all($res , MYSQLI_ASSOC); // получаем данные в ассоциативный массив

// пройдемся в цикле по массиву $date и выведем полученные данные
foreach ( $date as $item ){
echo "Name: { $item [ 'name' ]} <br>" ;
echo "Text: { $item [ 'text' ]} <br>" ;
echo "Date: { $item [ 'date' ]} <br>" ;
echo '<hr>' ;
}
?>
выведет:
Name: d'Artanian
Text: Имя с апострофом
Date: 2019-05-26 21:51:08
...
...
...