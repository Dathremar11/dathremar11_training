""" Socket в Python, Библиотеки socket, socketserver, Frameworks """
""" Стандартный модуль socket """
import socket
""" Серверный сокет (прослушивает/ожидает) """ # UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # Создаем экземпляр класса socket, передаем в конструктор 2 константы: /
# 1) AF_INET - означает, будем использовать IPV4 (AF_INET6 - для IPV6)
# 2) SOCK_DGRAM - отвечает за использование протокола UDP, (Socket Datagram)
# Создаем экземпляр на основе этих двух констант
sock.bind(('127.0.0.1', 8888))  # У класса socket описан  /
# метод bind, который используется для резервирования порта на нашей локальной машине
# В данном случае мы должны передать кортеж из двух значений:
# 1) IP-адрес или интерфейс сети "127.0.0.1"
# 2) Порт "8888", если ОС не заняла этот порт другой программой
# // Можно резервировать все интерфесы '0.0.0.0' или '0', можно не указывать IP-адрес '' - резервирем все интерфесы
result = sock.recv(1024)        # Пытаемся принять сообщение из сети, используя метод recv (recive - принять, количество в размере 1024)
# 1024 - потому что можем сюда передать размер буфера, который будет использоваться для порционального чтения данных
# // если будем принимать по 8 байт, то напишем выше "8", зависит от размера сообщений
# Можно реализовать таким образом - разбиваем приходящее сообщение на две части:
# 1) Длина реального информационного сообщения
# 2) Реальное информационное сообщение
# Принимаем первое сообщение int 125(длина сообщения, Байт), конвертируем, в result=sock=recv(1024), вторая попытка чтения сокета, т.к. знаем реальный размер информационного собщения
# лучше использовать небольшую степень двойки, для лучшей совместимости железа и софта // прописано в документации 
""" Функция recv блокирует интерпретатор - блокирующий режим, находимся в нем, ожидая попытки подключения к нам """ # т.к. UDP - ждем датаграмму
print('Message', result.decode('utf-8'))
# После того как мы получили сообщение и нету необходимости держать открытым/запущенным наш сокет сервер, необходимо
# освободить порт, который был зарезервирован методом bind
# Вызывается метод close класса socket, программа завершается, порт освободждается
sock.close() # Необходимо обрабатывать исключения, например:
# Получили данные, но не смогли декодировать байт строку в utf-8 - обрамлять обработчиками исключений
# UTF-8 от англ. Unicode Transformation Format, 8-bit — «формат преобразования Юникода, 8-бит») — распространённый стандарт кодирования символов,
#  позволяющий более компактно хранить и передавать символы Юникода, используя переменное количество байт (от 1 до 4), и обеспечивающий полную обратную 
# совместимость с 7-битной кодировкой ASCII. 
"""
В реальности необходимо чтобы сервер работал постоянно и ожидал прихода 100*** датаграм
"""


""" Пользовательский сокет (отправка/получение) """ # Клиент
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Test message', ('127.0.0.1', 8888))      # Отправка пользовательской датаграммы, используется метод sendto
 # sendto - отправляет сообщение - байт строку на конкретный IP-адрес и порт
 # можно также отправить на домен: 'localhost'

# Сервер с циклом try / except          # // Использование бесконечного цикла и постоянное чтение датаграм из сети
while True:                             # Бесконечный цикл
    try:
        result = sock.recv(1024)        # Пытаемся принять сообщение из сокета // постоянное чтение датаграм из сети // для N клиентов
    except KeyboardInterrupt:           # Отлавливание исключений // ctr + c
        sock.close()
        break
    else:                               # Если исключений не произошло
        print('Message', result.decode('utf-8'))
# После того, как пришло сообщение, попадаем в ветку else, если не отловили исключение, после чего декодируем сообщение, печатаем
# и возращаемся опять в try: recv, получается постоянный запуск чтения датаграммы с сети, пока не произойдет исключение, либо
# пока работа не будет остановлена принудительно

""" UNIX Сервер """
""" В качестве точки обмена выступает ФАЙЛ, в рамках одного компьютера, IP/порт не используется """ # (Docker)
# Файл - опциональная вещь, которуб можно настраивать, находиться в папке программы или зарезервированной папке ОС"
import os
import socket
unix_sock_name = 'unix.sock'         # В качестве названия файла (точки обмена) используем название 'unix.sock', которое сорхранили в переменную 
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)     # Сохраняем в качестве константы сокет, чтобы везде использовать переменную, а не выражение
# Используем отдельный вид сокета - UNIX, создаем точку обмена - файл socket.AF_UNIX, используя протокол UDP socket.SOCK_DGRAM
if os.path.exists(unix_sock_name):  # Проверяем, создавали ли ранее мы это файл, пытались ли ранее до этого запуска работать с этим сокетом, в ОС такой сокет может уже существовать (выведется ошибка)
    os.remove(unix_sock_name)   # Пересоздаем файл, если уже существует, то удаляем. 

sock.bind(unix_sock_name)   # Резервируем этот файл

while True:                 # Бесконечный цикл
    try:
        result = sock.recv(1024)   # Читаем датаграмму из файла unix.sock // так как не писали полный путь к файлу, он создался в папке скрипта
    except KeyboardInterrupt:      # Инетрпретатор заблокировал выполнение, до получения датаграмм
        sock.close()
        break
    else:
        print('Message', result.decode('utf-8'))

""" Клиент UNIX """
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b'Test message', ('unix.sock'))     # Отправлет сообщение на имя файла, а не на кортеж как с IP

""" Сервер TCP """
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Создаем экземпляр класса socket, используя TCP протокол socket.SOCK_STREAM, в конструктор сокета передаем socket.AF_INET, socket.SOCK_STREAM
sock.bind(('127.0.0.1', 8888))      # метод bind, для резервирования порта 8888 на интерфейле 127.0.0.1
sock.listen(5)  # Размер очереди, сколько соединений мы хотим слушать, в тот момент, когда мы примем и будем его обрабатывать, какому количеству сообинений (количеству клиентов) необходимо ждать, до их обработки (количество очереди, до тех пор, пока обрабатываемый сокет (первый), не закроется)
while True:
    try:
        client, addr = sock.accept() # Принимаем сооединение методом accept - смотрит очереди на наличие установленного соединения с клиентом, если очередь пуста - ожидает, если нет - то вытаскивает клиента на обработку
    except KeyboardInterrupt:        # метод accept возвращает кортеж из двух элементом 1) client - экземпляр класса сокет (клиентский), каждое отдельное подлючение это новый клиент
        sock.close                   # 2) addr - адрес IP/порт - 127.0.0.1/63691 - порт выделела ОС 
        break           # Подключаемся на порт 8888, если опрт открыт(есть TCP сервер), берем это соединение и создаем клиекта client, addr = sock.accept() и перекидывает его на порт 63691
    else:               
        result = client.recv(1024)  # Используем клиент как обычный сокет, пытаемся записать и прочитать из него инфоррмацию
        client.close()  # после обмена данными закрываем сокет
        print('Message', result.decode('utf-8'))    # Печатаем сообщение и идем в начала цикла while, для ожидаения приема нового клиента,
            # где метод accept проверяет очередь на наличие запроса на подключение
# Отличие от UDP - мы не просто читаем сообщение из серверного сокета (result = sock.recv(1024) - UDP сервер), а мы читаем сообщение от клиента result = client.recv(1024), 
# который ПОДКЛЮЧЕН, где метод accept client, addr = sock.accept() взял из очереди на подключение клиента sock.listen(5) который ожидает обмена данными и передает его
# на чтение и запись result = client.recv(1024) (можно запустить здесь отдельный цикл на то, что нужно сделать с сообщением)
""" Клиент TCP """
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))    # '' - любой адрес
sock.send(b'Test message')  # не нужно конкретно указывать адресата, котому что мы создали TCP сессию с помощью sock.connect(('', 8888)) 
sock.close  # после обмена данными закрываем сокет 



""" Сервер с блокировками """
# Выше перечисленные примеры - сервер блокирует интерпретатор, до тех пор, пока не вернется какой нибдуь клиент на пример путем выполнения методом client, addr = sock.accept()
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Создаем эземпляр класса socket
sock.bind(('127.0.0.1', 8888))          # Резервируем порт
sock.listen(5)                          # Устанавливаем размер очередь
sock.setblocking(False)                 # Метод setblocking устанавливает блокировку сокета (блокируюищий / не блокирующий режим)
"""
sock.setblocking(True) # Блокирующий режим
Мы заблокированы до тех пор, пока к нам не подключится клиент, когда к нам подключаться, только в тот момент в очередь попадет новый клиент и метод accept вернет клиента из очереди на выполнение
  // Если мы хотим написать интерактивную программу, которая периодически проверяет сеть на наличие клиентов, и если они есть, то обрабатывает их, а если нет
то выполняет свою логику, которую можно написать - обновление статусов, проверка почты и тп (sock.setblocking(True))

sock.setblocking(False) - Не блокирующий режим
Когда попытаемся вызвать метод accept в случает отсутствия клиентов в очереди, мы будем получать исключение Resource te,porarily unavailable (некого читать)
"""
client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Message', result.decode('utf-8'))


""" Доработанный предыдущий пример, с использованием блокировок / СЕРВЕР """
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))      # Резервируем порт
sock.listen(5)                      # Длина очереди
sock.setblocking(False)             # Не блокирующий режим

while True:                         # Бесконечный цикл
    try:
        client, addr = sock.accept()       # Пытаемся читать новые подключения методом accept обернув его в try/except
    except socket.error:          # socket.error - Исключение, которое возникает в случае отсутствия каких либо клиентов при не блокирующем режиме
        print('no clients')       # Сообщенгие печатается, если клиентов нету, попали в ветку except по исключению socket.error (никого нет в очереди) и успешно его обработали
    except KeyboardInterrupt
        break
    else:               # Попадаем в эту ветку, если клент к нам подключился, ветка успешного выполнения оператора try
        client.setblocking(True)        # Установили клиенту блокирующий режим, если используем блокирующим режим, то его нужно оборачивать в try / except
        result = client.recv(1024)      # При попытке чтения данных никаких исключений не возникнет
        client.close()                  # Закрываем соединение на стороне клиента
        print('Message', result.decode('utf-8'))    # Печатаем сообщение и возвращаемся вначала цикла while
# Удобно при постоянном ожидании подключения или сообщения от клиентов. В случае если клиент не посылает обновления своего статуса, а это статус
# к примеру держиться на протяжении одного часа, то мы не можем позволить блокировать интерпретатор и программу целый час, тогда нужно использовать
# не блокирующий режим и пытаться обработать исключение определенной логикой 

""" Аналоги Блокирубщего / Не Блокирующего режима """
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Создаем эземпляр класса socket
sock.bind(('127.0.0.1', 8888))          # Резервируем порт
sock.listen(5)                          # Устанавливаем размер очередь
sock.setblocking(True)                  # Блокирубщий / не блокирующий режим
sock.settimeout(5)
# Пытаемся прочесть из очереди наше соединение, как только пройдет 5 секунд, мы попадем на ветку except и обработаем исключение (выход из режима ожидания) 
# (переход в блокирующий режим по времиени), спустя 5 секунд переходи в блокирующий режим с выбросом исключения socket.error
sock.settimeout(0)      -> sock.blocking(False)
# Равносильмо не блокирующему режиму
sock.settimeout(None)   -> sock.blocking(True)
# Равносилен блокирующему режиму, блокируем интерпретатор
# sock.settimeout() - используется для установления ожидания на наши операции типа метода accept() 

try:
    client, addr = sock.accept()
except socket.error:
    print('No connections')
# except socket.timeout
#     print('time out')
else:
    result = clietn.recv(1024)
    client,close()
    print('Message', result.decode('utf-8'))

""" Сервер с использованием оператора with __ as __ """
import socket

# ___enter___ / ___exit___
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:  # Создание экхемпляра класса socket в операторе with
    print('8888 is bind')               # with создаст нам сокет и сохранит его в переменную sock
    sock.bind(('127.0.0.1', 8888))      # Не используем обработку исключений на recv, потому что при выходе из оператора with вызывается метод __exit__
    # Метод __exit__ у сокета реализован и он закрывает соединения, освободждая порт 8888, что позволяет заного запускать программу

    while True:
        result = sock.recv(1024)                    # Пытаемся читать сообщение
        print('Message', result.decode('utf-8'))    # Печатаем и попадаем в начала цикла while
# ctrl + c - освобождаем порт 8888, за счет того, что оператор with выполняет метод __exit__, в строке result = sock.recv(1024) выбрасывается исключение
# KeyboardInterrupt, оператор with обрабатывает его и закрывает сокет. (принудительно вызывает sock.close)
""" Дополнительные возможности установить опции сокета """
import socket
# Если мы хотим отправлять широковещательные сообщения, которые должны приходить на каждый сокет в сети (для всех получателей на адрес 255.255.255.255, датаграмма будет приходить для каждого клиента из отдельно)
sock. socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind(('127.0.0.1', 8888))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
sock.setsockopt(socket.SO_SOCKET, socket.SO_REUSEADDR, 1)   # Переискользование адреса
# Возникаются ситуации - мы зарезервировали порт, отправляем датаграмму, закрываем сокет. Есть определенное время, для чтения из буфера сообщения, отправить на сокет и закрыть все соединения
# В тот момент, когда в буфере еще остались данные (которые обрабатываются), то он может заблокировать возможность резервирования или переиспользования нашего адреса, который указан в методе bind
# Чтобы дать возможность исполниться меотду socket.close - порт должен быть освобожден, но он не успевает освободиться за счет того, что буфер еще не полностью очистился
# еще не  полностью все данные были прочитаны/отправлены и в этот момент, если кто-то бдует пытаться резервировать порт, то возникнет исключение
# При установлении socket.SO_REUSEADDR, 1, исключения не возникнет, и новый сервер/программа успешно зарезервируют данный порт
client, addr = sock.accept()
result = client.recv(1024)
client.close

print('Message', result.decode('utf-8'))

""" Объектно-ориентированный модуль socketserver """       # Включает в себя sock
# Предназначен для создания сокет серверов
# Набор классов, которые позволяют в стиле ООП создавать сокет сервера
import socketserver     # Стандарный модуль python
""" UDP Сервер """
class EchoUDPHandler(socketserver.BaseRequestHandler):  # Объявляем класс, который будет обрабатывать датаграммы (сообщения), которые будут приходить на сервер
# Класс EchoUDPHandler наследуется от BaseRequestHandler - реализован в рамках стандартного модуля socketserver
# Класс EchoUDPHandler - реализует набор методов
    # Когда приходит сообщение создается экземпляр класса EchoUDPHandler и вызывается метод handle
    def handle(self):   # Переотпределяем метод handle и пишем свою собственную логику - что делать с сообщением
        data, socket = self.request     # Получаем кортеж из двух значений data, socket которые храняться в self.request//self.request - это тоже самое, что мы получали информацию data и IP-адрес нашего клиента socket
        print('Address: {}'.format(self.client_address[0])) # Печатем адрес
        print('Data: {}'format(data.decode()))              # Печатаем декодированное сообщение
        socket.sendto(data, self.client_address)            # Отправляем обратно на сокет датаграмму, если клиент ожидает чего-то в ответ // можно не делать, только в случае если клиент читает датаграммы
 
if __name__ == '__main__':      # Определили класс
    with socketserver.UDPServer('0', 8888, EchoUDPHandler) as server: # Создание сервера// UDPServer - класс UDP сервер, передаем ему кортеж из двух значений '0', 8888 IP/port, 
        server.serve_forever()  # и передаем обработчик EchoUDPHandler - класс (не экземпляр), на каждое новое сообщение(датаграмму) будет создаваться экземпляр
# класса EchoUDPHandler и вызываться метод handle
# Запускаем сервер используя стандарнтый метод serve_forever() - запускает бесконечный цикл для ожидания новых клиентов

""" TCP Сервер """
class EchoTCPHandler(socketserver.BaseRequestHandler):      
 def handle(self):   # Переопределяем метод handle используя свою логику, которая необходима для создания сокет сервера // определяется логика работы с клиентом (операции чтения/запись из сокета в сокет)
        data = self.request.recv(1024).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'format(data.decode()))
        socket.request.sendall(data)
# Echo сервер отправляет то же самое, что мы отправляли от клиента
if __name__ == '__main__':      
    with socketserver.TCPServer('', 8888, EchoUDPHandler) as server:   # '' - Нулевой интерфейст
        server.serve_forever()
# Если в методе handle возникает исключение то модуль socketserver обрыбытывает это исключение и handle не ломается, вызов метода handle происходит в try/except

""" Внутренности handle """
class BaseRequestHandler    # Класс, который не наследуется ни от какого внутреннего класса.
# Конструктор __init__ вызывается для каждого запроса, если это UDP, то на каждую датаграму будет создаваться экземпляр класса BaseRequestHandler и создаваться конструктор __init__
    def __init__(self, request, client_address, server):
        self.request = request                  # Присваиваение запроса, 
        self.client_address = client_address    # это датаграммы и адреса
        self.server = server                    # Ссылка на server в операторе with__as__(который мы создаем), который будет автоматически биндится в экземпляр класса handle 
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()   # Будет выполнен в не зависимости от результата выполнения метода handle
# После выполнения метода finish(), работа класса BaseRequestHandler закончиться, после того, как выходим из переопределенного метода handle, мы считаем, что он завершил работу по обработки какого-либо запроса
    def setup(self):    # Метод setup, библиотека socketserver позволяет переопределиться данный метод и присвоить свою логику (обращение к базе данных, файловой системе или к чему то еще/ произвести авторизацию, аутентификацию и тп)
        pass

    def handle(self):   # Переопредели выше и написали свою логику в рамках нашей задачи
        pass

    def finish(self):
        pass

""" Работа TCP сервера в модуле socketserver """  # // TCPServer
address_family = socket.AF_INET     # Семейство сокетов по IP-адресу, IPv4
socket_type = socket.SOCK_STREAM    # TCP протокол
# Присваиваем переменные в экземпляр класса socket, то есть создаем сокет, инкапсулируем его внутри класса сервера TCPServer, и работает с ним далее через поле
# Данное поле участвует в методе server_bind(), где мы пытаемся зарезервировать адрес self.socket.bind(self.server_address), server_address - это кортеж из двух значений ''. 8888 - который мы передаем
# 
request_queue_size = 5
allow_reuse_address = False

def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
    """ Constructor. May be extended, do not override """ # Не переопределять
    BaseServer.__init__(self, server_address, RequestHandlerClass)              $1 # См. ниже - конструктор сервера
    self.socket = socket.socket(self.address_family, self.socket_type) # Используется экземпляр класса socket, с
# Стандартная абстракция над стандартным модулем socket
    if bind_and_activate:                       # 
        try:
            self.server.bind()                  # Зарезервировали необходимый порт
            self.server.bind_and_activate()     # Установили размер очереди см. ниже /BaseServer.__init__
        except:
            self.server_close()
            raise

def server_bind(self):
    """ Called by constructor to bind the socket 
    May be overriden
    """
    if self.allow_reuse_address:
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind(self.server_address)
    self.serve_address = self.socket.getsockname()

    $1  """ Конструктор сервера / BaseServer.__init__(self, server_address, RequestHandlerClass)    """ 
    timeout = None
    def __init__(self, server_address, RequestHandlerClass):
        self.serve_address = server_address                 # server_address - это кортеж из двух значений ''. 8888 - который мы передаем
        self.RequestHandlerClass = RequestHandlerClass      # Вызываем на каждый запрос (на каждого нового клиента), см. выше
        self.__is_shut_down = threading.Evant()
        self.__shutdown_request = False
    
    def server_activate(self):
        """ Called by constructor to activate the server
        May be overriden
        """
        self.socket.listen(self.request_queue_size)         # Устанавливается размер очереди, для клиентов

""" Сервер serve_forever """
# Логика основанная на событиях
    def serve_forever(self, poll_interval=0.5):
        """ Handle one request at a time intile shutdown 
        
        Polls for shutdown every poll_interval seconds. Ignires self.timeoit. If you need to do periodic tasks, do them in another thread        
        """
        self.__is_shut_down.clear()
        try:
            # XXX: Consider using another file descriptor or connecting to the // Рассмотрите возможность использования другого файлового дескриптора или подключения к сокету
            # socket to wake this up instead of polling. Polling reduces our   // чтобы разбудить его вместо опроса
            # responsiveness to a shutdown request and wastes cpu at all other times.   // Отзывчивость на запрос о завершении работы и трата ресурсов процессора в любое другое время.
            with _ServerSelector() as selector:                 # Как только приходит новый клиент, возникает событие, что новый клиент подключен и создается новый экземпляр класса EchoTCPHandler()
                selector.register(self, selectors.EVENT_READ)
            
            while not self.__shutdown_request:
                ready = selector.select(poll_interval)
                if ready:
                    self._handle_request_noblock()

                self.service_actions()

        finally:
            self.__shutdown_request = False
            self.__is_shut_down.set()

# Пример: Позволяет распаралелить вычисление или работу наших клиентов """
import socketserver

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):# Используем свой свобственный класс TCP сервера, который наследуется от основного класса TCPServer и ThreadingMixIn
    pass

class EchoTCPHandler(socketserver.BaseRequestHandler):      # Наследуемся от BaseRequestHandler и определяем EchoTCPHandler, который будет отправлять то же сообщение как бы эхоСервер

    def handle(self):                                       # Переходим в метод handle, мы использовали ThreadingMixIn - он распараллеливает обработку наших клиентов, тоесть при подключении нового клиента, который возвращается методом accept (с IP адресом), 
        data = self.request.recv(1024).strip()              # ThreadingMixIn - Когда к нам подключается один клиент, создается экземпляр класса EchoTCPHandler, и в отдельном потоке обрабатывается метод handle
        print('Address: {}'.format(self.client_address[0])) # Таким образом сервер может обрабатывать несколько клиентом, данный механизм используется в django run server
        print('Data: {}'.format(data.decode()))
        self.request.sendall(data)

if __name__ == '__main__':
    with ThreadingTCPServer(('', 8888), EchoTCPHandler) as server
        server.serve_forever()

""" Логика ThreadingMixIn """   # Распараллеливание вычислений

def process_request(self, request, client_address):
    """ Start a new thread to process the request """
    t = threading.Thread(target = self.process_request_thread, args = (request, client_address))
    t.daemon = self.daemon_threads
    if not t.daemon  and self._block_on_close:
        if self._threads is None:
            self.threads =  []
        self._threads.append(t)
    t.Start
# Создает thread (соединение) на каждого нового клиента и обрабатывает его в новом поток

