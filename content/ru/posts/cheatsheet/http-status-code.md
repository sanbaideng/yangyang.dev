---
title: Код статуса HTTP
background: bg-[#3b7dc0]
date: 2020-12-26 16:09:09
теги:
    - ответ
    - сервер
категории:
    - Другое
intro: |
    Шпаргалка по кодам статуса http. краткая справка по каждому коду статуса HTTP.
плагины:
    - tooltip
---

Код статуса HTTP
-----------


### Средства

- [1xx: Informational](#1xx-information){data-tooltip="Это означает, что запрос был получен и процесс продолжается."}
- [2xx: Успех](#2xx-successful){data-tooltip="Это означает, что действие было успешно получено, понято и принято."}
- [3xx: Перенаправление](#3xx-redirection){data-tooltip="Это означает, что для завершения запроса необходимо выполнить дальнейшие действия."}
- [4xx: Ошибка клиента](#4xx-client-error){data-tooltip="Это означает, что запрос содержит неправильный синтаксис или не может быть выполнен."}
- [5xx: Server Error](#5xx-server-error){data-tooltip="Это означает, что сервер не смог выполнить явно корректный запрос."}



### 2xx. Успешно {.row-span-2}
* [200: OK](https://tools.ietf.org/html/rfc7231#section-6.3.1){data-tooltip="Запрос выполнен."}
* [201: Created](https://tools.ietf.org/html/rfc7231#section-6.3.2){data-tooltip="Запрос выполнен, и новый ресурс создан."}
* [202: Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3){data-tooltip="Запрос принят к обработке, но обработка не завершена."}
* [203: Non-Authoritative Information](https://tools.ietf.org/html/rfc7231#section-6.3.4){data-tooltip="Информация в заголовке сущности получена от локальной или сторонней копии, а не от оригинального сервера."}
* [204: No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5){data-tooltip="В ответе указан код состояния и заголовок, но тело сущности в ответе отсутствует."}
* [205: Reset Content](https://tools.ietf.org/html/rfc7231#section-6.3.6){data-tooltip="Браузер должен очистить форму, используемую для этой транзакции, для дополнительного ввода данных."}
* [206: Partial Content](https://tools.ietf.org/html/rfc7233#section-4.1){data-tooltip="Сервер возвращает частичные данные запрашиваемого размера. Используется в ответ на запрос с указанием заголовка Range. Сервер должен указать диапазон, включаемый в ответ с помощью заголовка Content-Range."}




### 4xx. Ошибка клиента {.row-span-3}
* [400: Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1){data-tooltip="Сервер не понял запрос."}
* [401: Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1){data-tooltip="Запрашиваемая страница требует ввода имени пользователя и пароля."}
* [402: Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2){data-tooltip="Вы пока не можете использовать этот код."}
* [403: Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3){data-tooltip="Доступ к запрашиваемой странице запрещен."}
* [404: Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4){data-tooltip="Сервер не может найти запрашиваемую страницу."}
* [405: Method Not Allowed](https://tools.ietf.org/html/rfc7231#section-6.5.5){data-tooltip="Метод, указанный в запросе, не разрешен."}
* [406: Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6){data-tooltip="Сервер может сгенерировать только тот ответ, который не принят клиентом."}
* [407: Proxy Authentication Required](https://tools.ietf.org/html/rfc7235#section-3.2){data-tooltip="Вы должны пройти аутентификацию на прокси-сервере, прежде чем этот запрос будет обслужен."}
* [408: Request Timeout](https://tools.ietf.org/html/rfc7231#section-6.5.7){data-tooltip="Запрос занял больше времени, чем сервер был готов ждать."}
* [409: Конфликт](https://tools.ietf.org/html/rfc7231#section-6.5.8){data-tooltip="Запрос не может быть завершен из-за конфликта."}
* [410: Gone](https://tools.ietf.org/html/rfc7231#section-6.5.9){data-tooltip="Запрашиваемая страница больше не доступна ."}
* [411: Length Required](https://tools.ietf.org/html/rfc7231#section-6.5.10){data-tooltip="Длина "Content-Length" не определена. Сервер не примет запрос без него."}
* [412: Precondition Failed](https://tools.ietf.org/html/rfc7232#section-4.2){data-tooltip="Предварительное условие, указанное в запросе, оценено сервером как false."}
* [413: Payload Too Large](https://tools.ietf.org/html/rfc7231#section-6.5.11){data-tooltip="Сервер не примет запрос, так как объект запроса слишком велик."}
* [414: URI Too Long](https://tools.ietf.org/html/rfc7231#section-6.5.12){data-tooltip="Сервер не примет запрос, так как url слишком длинный". Возникает при преобразовании запроса "post" в запрос "get" с длинной информацией запроса."}
* [415: Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13){data-tooltip="Сервер не принимает запрос, так как медиатип не поддерживается."}
* [416: Range Not Satisfiable](https://tools.ietf.org/html/rfc7233#section-4.4){data-tooltip="Запрошенный диапазон байт недоступен и выходит за пределы."}
* [417: Expectation Failed](https://tools.ietf.org/html/rfc7231#section-6.5.14){data-tooltip="Ожидание, заданное в поле заголовка запроса Expect, не может быть выполнено этим сервером."}
* [426: Upgrade Required](https://tools.ietf.org/html/rfc7231#section-6.5.15){data-tooltip="Сервер отказывается выполнять запрос по текущему протоколу, но может быть готов сделать это после перехода клиента на другой протокол."}
* [451: Unavailable For Legal Reasons](https://datatracker.ietf.org/doc/html/rfc7725#section-3){data-tooltip="Этот код состояния указывает на то, что сервер отказывает в доступе к ресурсу в связи с требованием закона."}





### 1xx. Информация
* [100: Continue](https://tools.ietf.org/html/rfc7231#section-6.2.1){data-tooltip="Сервером получена только часть запроса, но пока она не отклонена, клиент должен продолжить выполнение запроса."}
* [101: Переключение протоколов](https://tools.ietf.org/html/rfc7231#section-6.2.2){data-tooltip="Сервер переключает протокол."}
* [102: Обработка](https://tools.ietf.org/html/rfc2518#section-10.1){data-tooltip="Промежуточный ответ, используемый для информирования клиента о том, что сервер принял полный запрос, но еще не завершил его."}




### 3xx. Перенаправление
* [300: Multiple Choices](https://tools.ietf.org/html/rfc7231#section-6.4.1){data-tooltip="Список ссылок. Пользователь может выбрать ссылку и перейти к этому месту. Не более пяти адресов."}
* [301: Moved Permanently](https://tools.ietf.org/html/rfc7231#section-6.4.2){data-tooltip="Запрашиваемая страница переместилась на новый адрес ."}
* [302: Found](https://tools.ietf.org/html/rfc7231#section-6.4.3){data-tooltip="Запрашиваемая страница временно переместилась по новому адресу ."}
* [303: See Other](https://tools.ietf.org/html/rfc7231#section-6.4.4){data-tooltip="Запрашиваемая страница может быть найдена по другому url ."}
* [304: Not Modified](https://tools.ietf.org/html/rfc7232#section-4.1){data-tooltip="Это код ответа на заголовок If-Modified-Since или If-None-Match, в котором URL не был изменен с указанной даты."}
* [305: Use Proxy](https://tools.ietf.org/html/rfc7231#section-6.4.5){data-tooltip="Доступ к запрашиваемому URL должен осуществляться через прокси, указанный в заголовке Location."}
* [306: Unused](https://tools.ietf.org/html/rfc7231#section-6.4.6){data-tooltip="Этот код использовался в предыдущей версии. Он больше не используется, но код зарезервирован."}
* [307: Временное перенаправление](https://tools.ietf.org/html/rfc7231#section-6.4.7){data-tooltip="Запрашиваемая страница временно переместилась на новый url."}


### 5xx. Ошибка сервера
* [500: Внутренняя ошибка сервера](https://tools.ietf.org/html/rfc7231#section-6.6.1){data-tooltip="Запрос не был завершен. Сервер встретил непредвиденное условие."}
* [501: Not Implemented](https://tools.ietf.org/html/rfc7231#section-6.6.2){data-tooltip="Запрос не был выполнен. Сервер не поддерживает требуемую функциональность."}
* [502: Bad Gateway](https://tools.ietf.org/html/rfc7231#section-6.6.3){data-tooltip="Запрос не был выполнен. Сервер получил недопустимый ответ от вышестоящего сервера."}
* [503: Service Unavailable](https://tools.ietf.org/html/rfc7231#section-6.6.4){data-tooltip="Запрос не был выполнен. Сервер временно перегружен или не работает."}
* [504: Gateway Timeout](https://tools.ietf.org/html/rfc7231#section-6.6.5){data-tooltip="Шлюз отключился по таймеру."}
* [505: HTTP Version Not Supported](https://tools.ietf.org/html/rfc7231#section-6.6.6){data-tooltip="Сервер не поддерживает версию протокола "http"."}

