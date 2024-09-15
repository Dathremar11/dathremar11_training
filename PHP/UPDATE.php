<? /*
Обновление данных (UPDATE)

Пишем SQL-запрос на обновление данных.
В переменную $update запишем наш запрос:

UPDATE gb - (обновление gb),
SET text - (в поле text),
CONCAT (text, '|||') - объединеняем строковые значения text и '|||',
WHERE id > 4 - где id > 4,
or die - или умри и,
mysqli_error($db) - выведи ошибку.*/
?>

-- файл index.php --

<?php
header ( "Content-type: text/html; charset=utf-8" );
error_reporting (- 1 );

// Подключение к базе данных
$db = @mysqli_connect( '127.0.0.1', 'root', '', 'gb' ) or die ( 'Ошибка соединения с БД' );
if (! $db ) die (mysqli_connect_error());

// Установка кодировки соединения
mysqli_set_charset ( $db , "utf8" ) or die ( 'Не установлена кодировка');

// Запрос к базе данных (обновляем данные в нашей таблице)
// готовим запрос
$update = "UPDATE gb SET text = CONCAT (text, '|||') WHERE id > 4" ;
// выполняем запрос
$res_update = mysqli_query( $db , $update ) or die (mysqli_error( $db ));
?>