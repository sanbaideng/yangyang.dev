---
title: Laravel
date: 2021-11-09 18:26:55
background: bg-[#e44230]
label: PHP
теги:
    - web
    - фреймворк
    - php
категории:
    - Программирование
intro: |
    [Laravel](https://laravel.com/docs/8.x/) - это выразительный и прогрессивный фреймворк веб-приложений для PHP.
    Эта шпаргалка содержит справочник по общим командам и возможностям Laravel 8.
плагины:
    - copyCode
---


# Laravel
---------------

### Требования {.row-span-2}
- Версия PHP >= 7.3
- BCMath PHP Extension
- Ctype PHP Extension
- Fileinfo PHP Extension
- JSON PHP Extension
- Mbstring PHP Extension
- OpenSSL PHP Extension
- PDO PHP Extension
- Tokenizer PHP Extension
- XML PHP Extension

Убедитесь, что ваш веб-сервер направляет все запросы к файлу вашего приложения
`public/index.php` файл, См: [Развертывание](#deployment)


### Windows
- #### Установите [Docker Desktop](https://www.docker.com/products/docker-desktop)
- #### Установите и включите [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install)
- #### Убедитесь, что Docker Desktop [настроен на использование WSL2](https://docs.docker.com/desktop/windows/wsl/)
- #### В терминале WSL2:
    ``hell
    $ curl -s https://laravel.build/example-app | bash
    $ cd example-app
    $ ./vendor/bin/sail up
    ```
{.marker-timeline}

Доступ к приложению по `http://localhost`



### Mac
- #### Установите [Docker Desktop](https://www.docker.com/products/docker-desktop)
- #### В терминале:
    ``hell
    $ curl -s https://laravel.build/example-app | bash
    $ cd example-app
    $ ./vendor/bin/sail up
    ```
{.marker-timeline}

Доступ к приложению по `http://localhost`


### Linux
``hell
$ curl -s https://laravel.build/example-app | bash
$ cd example-app
$ ./vendor/bin/sail up
```
Установка через [Composer](https://getcomposer.org)
``bash
$ composer create-project laravel/laravel example-app
$ cd example-app
$ php artisan serve
```
Доступ к приложению через `http://localhost`




Конфигурация
---------------

### .env {.cols-2}
Получение значений из файла `.env`
``php
env('APP_DEBUG');

// со значением по умолчанию
env('APP_DEBUG', false);
```
Определяем текущее окружение
``php
использовать Illuminate\Support\Facades\App;

$environment = App::environment();
```
Доступ к значениям конфигурации с использованием синтаксиса "точка"
``php
// config/app.php --> ['timezone' => '']
$value = config('app.timezone');

// Получаем значение по умолчанию, если конфигурационное значение не существует...
$value = config('app.timezone', 'Asia/Seoul');
```
Установка значений конфигурации во время выполнения:
``php
config(['app.timezone' => 'America/Chicago']);
```

### Режим отладки
Включить (локальный dev):
```php
// .env файл
APP_ENV=local
APP_DEBUG=true
// ...
```
Выключение (production):
```php
// .env файл
APP_ENV=production
APP_DEBUG=false
// ...
```

### Режим обслуживания
Временное отключение приложения (код состояния 503)
```bash
php artisan down
```

#### Отключить режим обслуживания
``bash
php artisan up
```

#### Обход режима обслуживания
``bash
php artisan down --secret="1630542a-246b-4b66-afa1-dd72a4c43515"
```
Зайдите на URL-адрес вашего приложения `https://example.com/1630542a-246b-4b66-afa1-dd72a4c43515`, чтобы установить cookie и обойти экран обслуживания

Маршрутизация
---------------

### Маршрутизация HTTP-методов {.row-span-2}
``php
Route::get($uri, $callback);
Route::post($uri, $callback);
Route::put($uri, $callback);
Route::patch($uri, $callback);
Route::delete($uri, $callback);
Route::options($uri, $callback);
```
Несколько HTTP-методов
```php
Route::match(['get', 'post'], '/', function () {
    //
});

Route::any('/', function () {
    //
});
```

### Базовое определение {.row-span-2}
``php
использовать Illuminate\Support\Facades\Route;

// закрытие
Route::get('/greeting', function () {
    return 'Hello World';
});

// действие контроллера
Route::get(
    '/user/profile',
    [UserProfileController::class, 'show']
);
```

### Инъекция зависимостей
``php
использовать Illuminate\Http\Request;

Route::get('/users', function (Request $request) {
    // ...
});
```
Конкретные зависимости типа hint для автоинъекции


### Маршруты просмотра
``php
// Аргумент 1: URI, Аргумент 2: имя представления
Route::view('/welcome', 'welcome');

// с данными
Route::view('/welcome', 'welcome', ['name' => 'Taylor']);
```
Маршрут должен возвращать только представление.  



### Привязка модели маршрута {.row-span-4}
#### Неявное связывание
С закрытием
``php
использовать App\Models\User;

Route::get('/users/{user}', function (User $user) {
    return $user->email;
});

// /user/1 --> User::where('id', '=', 1);
```
С помощью действия контроллера
``php
use App\Http\Controllers\UserController;
использовать App\Models\User;

// Определение маршрута...
Route::get('/users/{user}', [UserController::class, 'show']);

// Определение метода контроллера...
public function show(User $user)
{
    return view('user.profile', ['user' => $user]);
}
```
С пользовательской колонкой разрешения
``php
использовать App\Models\Post;

Route::get('/posts/{post:slug}', function (Post $post) {
    return $post;
});

// /posts/my-post --> Post::where('slug', '=', 'my-post');
```
Всегда используйте другой столбец для разрешения
``php
// в App\Models\Post
public function getRouteKeyName()
{
    return 'slug';
}
```
Множественные модели - вторая является дочерней по отношению к первой
``php
использовать App\Models\Post;
использовать App\Models\User;

Route::get('/users/{user}/posts/{post:slug}', function (User $user, Post $post) {
    return $post;
});
```
Удобный способ автоматической инъекции экземпляров модели непосредственно в маршруты




### Параметры маршрута {.row-span-2}
Захват сегментов URI внутри маршрута
#### Необходимые параметры
``php
Route::get('/user/{id}', function ($id) {
    return 'User '.$id;
});
```
С инъекцией зависимостей
``php
использовать Illuminate\Http\Request;

Route::get('/user/{id}', function (Request $request, $id) {
    return 'User '.$id;
});
```
#### Необязательные параметры
``php
Route::get('/user/{name?}', function ($name = null) {
    return $name;
});

Route::get('/user/{name?}', function ($name = 'John') {
    { return $name;
});
```



### Маршруты перенаправления
Статус HTTP `302`
``php
Route::redirect('/here', '/there');
```
Установка кода статуса
``php
Route::redirect('/here', '/there', 301);
```
Постоянный `301` редирект
``php
Route::permanentRedirect('/here', '/there');
```


### Ограничения регулярных выражений {.cols-2}
``php
Route::get('/user/{name}', function ($name) {
    //
})->where('name', '[A-Za-z]+');

Route::get('/user/{id}', function ($id) {
    //
})->where('id', '[0-9]+');

Route::get('/user/{id}/{name}', function ($id, $name) {
    //
})->where(['id' => '[0-9]+', 'name' => '[a-z]+']]);
```
См. также: [Regex Cheatsheet](/regex)

### Именованные маршруты
Имена маршрутов всегда должны быть уникальными
``php
Route::get('/user/profile', function () {
    //
})->name('profile');
```
См: [Справочники](#helpers-cols-3)


### Обратные маршруты
``php
Route::fallback(function () {
    //
});
```
Выполняется, когда ни один другой маршрут не подходит

### Группы маршрутов
#### Middleware
``php
Route::middleware(['first', 'second'])->group(function () {
    Route::get('/', function () {
        // Используется первое и второе промежуточное ПО...
    });

    Route::get('/user/profile', function () {
        // Используется первое и второе промежуточное ПО...
    });
});
```
#### Префиксы URI
``php
Route::prefix('admin')->group(function () {
    Route::get('/users', function () {
        // Совпадает с URL "/admin/users"
    });
});
```
#### Префикс имени
``php
Route::name('admin.')->group(function () {
    Route::get('/users', function () {
        // Маршруту присваивается имя "admin.users"...
    })->name('users');
});
```
Совместное использование атрибутов в маршрутах


### Доступ к текущему маршруту
``php
использовать Illuminate\Support\Facades\Route;

// Illuminate\Routing\Route
$route = Route::current();

// строка
$name = Route::currentRouteName();

// строка
$action = Route::currentRouteAction();
```


Помощники
---------------

### маршруты {.row-span-2}
#### Именованный маршрут
``php
$url = route('profile');
```
С параметрами
``php
// Route::get('/user/{id}/profile', /*...*/ )->name('profile);

$url = route('profile', ['id' => 1]);

// /user/1/profile/
```
Со строкой запроса
``php
// Route::get('/user/{id}/profile', /*...*/ )->name('profile);

$url = route('profile', ['id' => 1, 'photos'=>'yes']);

// /user/1/profile?photos=yes
```

#### Перенаправления
``php
// Генерация перенаправлений...
return redirect()->route('profile');
```

#### Модели Eloquent
``php
echo route('post.show', ['post' => $post]);
```
Помощник маршрута автоматически извлекает ключ маршрута модели.
См. раздел [Маршрутизация](#routing-cols-4)

### Генерация URL
Генерируйте произвольные URL-адреса для вашего приложения, которые будут
автоматически использовать схему (HTTP или HTTPS) и хост
из текущего запроса
``php
$post = App\Models\Post::find(1);

echo url("/posts/{$post->id}");

// http://example.com/posts/1
```
#### Текущий URL
``php
// Получение текущего URL без строки запроса...
echo url()->current();

// Получение текущего URL с учетом строки запроса...
echo url()->full();

// Получение полного URL для предыдущего запроса...
echo url()->previous();
```
### URL именованного маршрута
```php
$url = route('profile');
```
См. [Именованный маршрут](#named-route)

### Обработка ошибок
``php
public function isValid($value)
{
    try {
        // Валидация значения...
    } catch (Throwable $e) {
        report($e);

        return false;
    }
}
```
Сообщить об исключении, но продолжить обработку текущего запроса

 ### HTTP-исключения
 ``php
 // страница не найдена
 abort(404);
 ```
Формирование ответа на исключение HTTP с использованием кода состояния


Контроллеры
---------------

### Базовый
``php
пространство имен App\Http\Controllers;

use App\Http\Controllers\Controller;
использовать App\Models\User;

class UserController extends Controller
{
    public function show($id)
    {
        return view('user.profile', [
            'user' => User::findOrFail($id)
        ]);
    }
}
```
Определяем маршрут для этого метода контроллера:
``php
использовать App\Http\Controllers\UserController;

Route::get('/user/{id}', [UserController::class, 'show']);
```

Запросы
---------------

### Защита от CSRF
Laravel автоматически генерирует "токен" CSRF для каждой активной сессии пользователя.  
Этот маркер используется для проверки того, что аутентифицированный пользователь является тем, кто действительно выполняет запросы.

Получение маркера текущей сессии:
``php
Route::get('/token', function (Request $request) {
    $token = $request->session()->token();

    $token = csrf_token();

    // ...
});
```
Формы `POST`, `PUT`, `PATCH` или `DELETE` должны содержать скрытое поле CSRF `_token`.
в форме для проверки запроса.
``html
<form method="POST" action="/profile">
    @csrf

    <!-- Эквивалентно... -->
    <input type="hidden" name="_token" value="{{ csrf_token() }}" />
</form>
```
См. [Forms](#forms-cols-3)

### Доступ к запросу
Получение экземпляра текущего запроса с помощью подсказки типа
действия контроллера или закрытия маршрута
``php
// действие контроллера
class UserController extends Controller
{
    public function store(Request $request)
    {
        $name = $request->input('name');
    }
}

// закрытие
Route::get('/', function (Request $request) {
    //
});
```
[См. Маршрутизация](#routing)

### Path
Информация о пути запроса
``php
$uri = $request->path();

// https://example.com/foo/bar --> foo/bar
```
#### Соответствие пути шаблону
Проверка соответствия пути входящего запроса заданному шаблону
``php
// * - подстановочный знак
if ($request->is('admin/*')) {
    //
}
```
Определите, соответствует ли входящий запрос именованному маршруту
``php
if ($request->routeIs('admin.*')) {
    //
}
```

### URL
Полный URL-адрес входящего запроса
``php
// URL без строки запроса
$url = $request->url();

// URL с учетом строки запроса
$urlWithQueryString = $request->fullUrl();

// добавление данных в строку запроса
$request->fullUrlWithQuery(['type' => 'phone']);
```

### Метод запроса
```php
$method = $request->method();

// проверка соответствия HTTP-глагола заданной строке
if ($request->isMethod('post')) {
    //
}
```

### IP-адрес клиента
```php
$ipAddress = $request->ip();
```


### Заголовки
``php
$value = $request->header('X-Header-Name');

$value = $request->header('X-Header-Name', 'значение по умолчанию');

// определяем, содержит ли запрос заданный заголовок
if ($request->hasHeader('X-Header-Name')) {
    //
}

// Получение токена носителя из заголовка авторизации
$token = $request->bearerToken();
```

### Тип содержимого
Возвращает массив, содержащий все типы контента, принимаемые запросом
``php
$contentTypes = $request->getAcceptableContentTypes();
```
Булева проверка на то, что типы контента приняты запросом
``php
if ($request->accepts(['text/html', 'application/json'])) {
    // ...
}
```


### Входные данные {.row-span-4}
Получение всех входных данных входящего запроса в виде массива
``php
$input = $request->all();
```
Получить все входные данные входящего запроса в виде коллекции
``php
$input = $request->collect();

// Получаем подмножество в виде коллекции
$request->collect('users')->each(function ($user) {
    // ...
});
```
См. раздел [Справочники](#helpers-cols-3)

Получение пользовательского ввода (также получает значения из строки запроса)
``php
$name = $request->input('name');

// со значением по умолчанию, если его нет
$name = $request->input('name', 'Sally');
```

Доступ к массиву входных данных
``php
$name = $request->input('products.0.name');

$names = $request->input('products.*.name');
```

Получение всех входных значений в виде ассоциативного массива:
``php
$input = $request->input();
```

Получать значения только из строки запроса:
``php
$name = $request->query('name');

// со значением по умолчанию
$name = $request->query('name', 'Helen');
```

Получение всех значений строки запроса в виде ассоциативного массива:
``php
$query = $request->query();
```

#### Булевые входные значения
Пригодится для ввода флажков или других булевых значений.
Возвращает `true` для `1`, `"1"`, `true`, `"true"`, `"on"` и `"yes"`.   
Все остальные значения будут возвращать `false`.
``php
$archived = $request->boolean('archived');
```

### Динамические свойства
Доступ к входным данным через свойства.  
Если вход не найден, проверяются параметры маршрута.
``php
$name = $request->name;
```

### Получение частичного ввода
``php
$input = $request->only(['username', 'password']);

$input = $request->only('username', 'password');

$input = $request->except(['credit_card']);

$input = $request->except('credit_card');
```

### Проверка существования
Определить наличие значения (значений)
``php
if ($request->has('name')) {
    //
}

// проверка наличия ВСЕХ значений
if ($request->has(['name', 'email'])) {
    //
}

// если присутствуют какие-либо значения
if ($request->hasAny(['name', 'email'])) {
    //
}
```

### Старый ввод
Получение входных данных из предыдущего запроса
``php
$username = $request->old('username');
```
Или воспользуйтесь помощником ``old()``
``php
<input type="text" name="username" value="{{ old('username') }}">
```
См: [Хелперы](#helpers-cols-3)
См: [Формы](#forms-cols-3)

### Загруженные файлы
Получение загруженного файла из запроса
``php
$file = $request->file('photo');

$file = $request->photo;
```

Получение пути или расширения файла
``php
$path = $request->photo->path();

$extension = $request->photo->extension();
```

Сохраняем загруженный файл со случайно сгенерированным именем
``php
// путь, по которому должен быть сохранен файл относительно
// настроенного корневого каталога файловой системы
$path = $request->photo->store('images');

// необязательный 2-й параметр для указания диска файловой системы
$path = $request->photo->store('images', 's3');
```
Сохраняем загруженный файл и указываем его имя
``php
$path = $request->photo->storeAs('images', 'filename.jpg');

$path = $request->photo->storeAs('images', 'filename.jpg', 's3');
```
См. подробнее: [Файловое хранилище Laravel](https://laravel.com/docs/8.x/filesystem)


Просмотры
---------------
### Intro
- [Laravel Docs - Views](https://laravel.com/docs/8.x/views)
 
``html
<!-- Вид хранится в файле resources/views/greeting.blade.php -->

<html>
    <body>
        <h1>Здравствуйте, <?php echo $name; ?></h1>
    </body>
</html>
```
Создайте представление, поместив файл с расширением `.blade.php`
в каталоге `resources/views`.


### Передача данных в представления
#### В виде массива
``php
return view('greetings', ['name' => 'Victoria']);
```
#### Использование функции with()
``php
return view('greeting')
            ->with('name', 'Victoria')
            ->with('occupation', 'Astronaut');
```

Доступ к каждому значению с помощью ключей данных
``html
<html>
    <body>
        <h1>Здравствуйте, {{ $name }}</h1>
        <!-- Или -->
        <h1>Здравствуйте, <?php echo $name; ?></h1>
    </body>
</html>
```


### помощник view
Возврат представления из маршрута с помощью помощника ``view()``
``php
Route::get('/', function () {
    return view('greeting', ['name' => 'James']);
});
```
См: [View Routes](#view-routes) и [Helpers](#helpers)


### Подкаталоги
``php
// resources/views/admin.profile.blade.php
return view('admin.profile');
```


Шаблоны лезвий
---------------

### Intro
- [Laravel Docs - Blade Templates](https://laravel.com/docs/8.x/blade)

Blade - это шаблонизатор, входящий в состав Laravel
который также позволяет использовать обычный PHP.

### Представления
Представления Blade возвращаются с помощью помощника `view()`.
``php
Route::get('/', function () {
    return view('welcome', ['name' => 'Samantha']);
});
```
См: [Views](#view-helper)

### Комментарии
``html
{{-- Этот комментарий не будет присутствовать в отрисованном HTML --}}
```


### Директивы {.row-span-3}
#### if Statements
```php
@if (count($records) === 1)
    У меня есть одна запись!
@elseif (count($records) > 1)
    У меня несколько записей!
@else
    У меня нет ни одной записи!
@endif
```
#### isset & empty
``php
@isset($records)
    // $records определен и не является null...
@endisset

@empty($records)
    // $records "пуст"...
@endempty
```
#### Аутентификация
``php
@auth
    // Пользователь аутентифицирован...
@endauth

@guest
    // Пользователь не аутентифицирован...
@endguest
```
#### Циклы
``html
@for ($i = 0; $i < 10; $i++)
    Текущее значение {{ $i }}
@endfor

@foreach ($users as $user)
    <p>Это пользователь {{ $user->id }}</p>
@endforeach

@forelse ($users as $user)
    <li>{{ $user->name }}</li>
@empty
    <p>Нет пользователей</p>
@endforelse

@while (true)
    <p>Я зацикливаюсь до бесконечности.</p>
@endwhile
```
Итерация цикла:
``php
@foreach ($users as $user)
    @if ($loop->first)
        Это первая итерация.
    @endif

    @if ($loop->last)
        Это последняя итерация.
    @endif

    <p>Это пользователь {{ $user->id }}</p>.
@endforeach
```
См. подробнее: [Laravel Loop Variable](https://laravel.com/docs/8.x/blade#the-loop-variable)


### Отображение данных
В Blade эхо-операторы `{{ }}` автоматически передаются через функцию
функция PHP `htmlspecialchars` для предотвращения XSS-атак.

Отображение содержимого переменной name:
``html
Здравствуйте, {{ $name }}.
```
Вывести результаты работы функции PHP:
``html
Текущая временная метка UNIX равна {{ time() }}.
```
Отображение данных без экранирования с помощью `htmlspecialchars`
``html
Здравствуйте, {!!! $name !!!}.
```

### Включение вложенных представлений
Включение представления Blade из другого представления.  
Все переменные, доступные родительскому представлению, будут доступны и включенному представлению
``html
<div>
    <!-- resources/views/shared/errors/blade.php -->
    @include('shared.errors')

    <form>
        <!-- Содержание формы -->
    </form>
</div>
```

### Необработанный PHP
Выполнение блока обычного PHP
``php
@php
    $counter = 1;
@endphp
```

### Стеки
Blade позволяет выполнять push в именованные стеки, которые могут быть отображены в другом представлении или макете.  
Полезно для библиотек javascript, необходимых дочерним представлениям
``html
<!-- Добавить в стек -->
@push('scripts')
    <script src="/example.js"></script>
@endpush
```
Рендеринг стека
``html
<head>
    <!-- Содержание заголовка -->

    @stack('scripts')
</head>
```
Добавление в начало стека
``php
@push('scripts')
    Это будет второй...
@endpush

// Позже...

@prepend('scripts')
    Это будет первым...
@endprepend
```


Формы
---------------
### Intro
- [Laravel Docs - Forms](https://laravel.com/docs/8.x/blade#forms)

### Поле CSRF
Включите скрытое поле CSRF-токена для проверки запроса
``html
<form method="POST" action="/profile">
    @csrf
    
    ...
</form>
```
См: [CSRF Protection](#csrf-protection)

### Поле метода
Поскольку HTML-формы не могут выполнять запросы `PUT`, `PATCH` или `DELETE`, вам необходимо добавить скрытое поле `_method` для подмены этих глаголов HTTP.
необходимо добавить скрытое поле `_method` для подмены этих HTTP-глаголов:
``html
<form action="/post/my-post" method="POST">
    @method('PUT')

    ...
</form>
```

### Ошибки валидации
``html
<!-- /resources/views/post/create.blade.php -->

<label for="title">Название поста</label>

<input id="title" type="text" class="@error('title') is-invalid @enderror">

@error('title')
    <div class="alert alert-danger">{{ $message }}</div>
@enderror
```
См: [Validation](#validation-cols-3)

### Перезаполнение форм
При перенаправлении из-за ошибки валидации ввод запроса передается в сессию.  
Получите входные данные из предыдущего запроса с помощью метода ``old``.
``php
$title = $request->old('title');
```
Или с помощью помощника `old()`
``html
<input type="text" name="title" value="{{ old('title') }}">
```

Валидация
---------------
### Intro
- [Laravel Docs - Validation](https://laravel.com/docs/8.x/validation)

В случае неудачи проверки будет сгенерирован ответ с перенаправлением на предыдущий URL.  
Если входящий запрос является XHR-запросом, то будет возвращен JSON-ответ с сообщениями об ошибках
сообщения об ошибках валидации.

### Логика
``php
// в файле routes/web.php
Route::get('/post/create', [App\Http\Controllers\PostController::class, 'create']);
Route::post('/post', [App\Http\Controllers\PostController::class, 'store']);

// в app/Http/Controllers/PostController...
public function store(Request $request)
{
    $validated = $request->validate([
        // input name => правила валидации
        'title' => 'required|unique:posts|max:255',
        'body' => 'required',
    ]);

    // Запись в блоге валидна...
}
```

### Правила {.row-span-5}
Может также передаваться в виде массива
``php
$validatedData = $request->validate([
    'title' => ['required', 'unique:posts', 'max:255'],
    'body' => ['required'],
]);
```
#### after:date
Поле должно быть значением после заданной даты.
``php
'start_date' => 'required|date|after:tomorrow'
```
Вместо строки даты можно указать другое поле для сравнения с датой
``php
'finish_date' => 'required|date|after:start_date'
```
См. [before:date](#beforedate)
#### after_or_equal:date
Поле должно быть значением после или равным заданной дате.  
См. [after:date](#afterdate)
#### before:date
Поле должно быть значением, предшествующим заданной дате.  
В качестве значения `date` может быть указано имя другого поля.  
См. [after:date](#afterdate)
#### alpha_num
Поле должно состоять исключительно из буквенно-цифровых символов
#### boolean
Поле должно быть способно быть приведено к виду `boolean`.  
Принимаются следующие значения: `true`, `false`, `1`, `0`, `"1"` и `"0"`.
#### подтверждено
Поле должно иметь соответствующее поле `{поле}_confirmation`.  
Например, если поле является паролем, то должно присутствовать соответствующее поле `password_confirmation`.
#### current_password
Поле должно соответствовать паролю аутентифицированного пользователя.
#### дата
Поле должно представлять собой правильную, неотносительную дату в соответствии с PHP-функцией `strtotime`.
#### email
Поле должно быть оформлено как адрес электронной почты.
#### файл
Поле должно представлять собой успешно загруженный файл.  
См: [Загруженные файлы](#uploaded-files)
#### max:value
Поле должно быть меньше или равно максимальному значению.  
Строки, числа, массивы и файлы оцениваются аналогично правилу [size](#sizevalue).
#### min:value
Поле должно иметь минимальное значение.  
Строки, числа, массивы и файлы оцениваются как правило [size](#sizevalue).
#### mimetypes:text/plain,...
Файл должен соответствовать одному из заданных MIME-типов:
``php
'video' => 'mimetypes:video/avi,video/mpeg,video/quicktime'
````
Содержимое файла будет прочитано, и фреймворк попытается угадать MIME-тип
MIME-тип, независимо от MIME-типа, указанного клиентом.
#### mimes:foo,bar,...
Поле должно иметь MIME-тип, соответствующий одному из перечисленных расширений.
``php
'photo' => 'mimes:jpg,bmp,png'
````
Содержимое файла будет прочитано, и фреймворк попытается угадать MIME-тип
MIME-типа, независимо от MIME-типа, указанного клиентом.
 
[Полный список MIME-типов и расширений](https://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types)
#### nullable
Поле может быть нулевым.
#### numeric
Поле должно быть числовым.
#### password
Поле должно соответствовать паролю аутентифицированного пользователя.
#### запрещено
Поле должно быть пустым или отсутствовать.
#### prohibited_if:anotherfield,value,...
Поле должно быть пустым или отсутствовать, если поле
поле _anotherfield_ равно любому значению.
#### prohibited_unless:anotherfield,value,...
Поле должно быть пустым или отсутствовать, если поле
поле _anotherfield_ равно любому значению.
#### required
Поле должно присутствовать во входных данных и не быть пустым.  
Поле считается "пустым", если верно одно из следующих условий:
- Значение равно `null`.
- Значение является пустой строкой.
- Значение является пустым массивом или пустым объектом `Countable`.
- Значение представляет собой загруженный файл без пути.
#### required_with:foo,bar,...
Поле должно присутствовать и быть непустым, только если любое из других
указанных полей присутствует и не пуст.
#### size:value
Поле должно иметь размер, соответствующий заданному значению.
- Для строк: количество символов
- Для числовых данных: целое значение (должно также выполняться правило `numeric` или `integer`).
- Для массивов: счетчик массива
- Для файлов: размер файла в килобайтах
``php
// Проверяем, что длина строки составляет ровно 12 символов...
'title' => 'size:12';
// Проверяем, что заданное целое число равно 10...
'seats' => 'integer|size:10';
// Удостовериться, что массив содержит ровно 5 элементов...
'tags' => 'array|size:5';
// Удостовериться, что загружаемый файл имеет размер ровно 512 килобайт...
'image' => 'file|size:512';
```
#### unique:table,column
Поле не должно существовать в данной таблице базы данных
#### url
Поле должно быть корректным URL

[Смотрите все доступные правила](https://laravel.com/docs/8.x/validation#available-validation-rules)

### Проверка паролей
Убедитесь, что пароли имеют достаточный уровень сложности
``php
$validatedData = $request->validate([
    'password' => ['required', 'confirmed', Password::min(8)]
]);
```
Объект правила ``Password`` позволяет легко настраивать требования к сложности пароля
``php
// Требуется не менее 8 символов...
Password::min(8)

// Требуется не менее одной буквы...
Password::min(8)->letters()

// Требуется хотя бы одна прописная и одна строчная буква...
Password::min(8)->mixedCase()

// Требуется хотя бы одна цифра...
Password::min(8)->numbers()

// Требуется хотя бы один символ...
Password::min(8)->symbols()
```
Убедиться, что пароль не был скомпрометирован в результате публичной утечки данных о паролях
``php
Password::min(8)->uncompromised()
```
> _Использует модель [k-анонимности](https://en.wikipedia.org/wiki/K-anonymity) через сервис [haveibeenpwned.com](https://haveibeenpwned.com) без ущерба для конфиденциальности и безопасности пользователя_.

Методы могут быть соединены в цепочку
``php
Password::min(8)
    ->letters()
    ->mixedCase()
    ->numbers()
    ->символы()
    ->uncompromised()
```
### Отображение ошибок валидации
``php
<!-- /resources/views/post/create.blade.php -->

<h1>Создать пост</h1>

@if ($errors->any())
    <div class="alert alert-danger">
        <ul>
            @foreach ($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif

<!-- Создание почтовой формы -->
```
См: [Ошибки валидации](#validation-errors)

### Необязательные поля
Часто необходимо помечать "необязательные" поля запроса как `nullable`.
если вы не хотите, чтобы валидатор считал значения `null` недопустимыми
``php
// Поле publish_at может быть либо null, либо корректным представлением даты
$request->validate([
    'title' => 'required|unique:posts|max:255',
    'body' => 'required',
    'publish_at' => 'nullable|date',
]);
```

### Валидированный вход
Получение данных запроса, прошедших валидацию
``php
$validated = $request->validated();
```
Или с помощью `safe()`, которая возвращает экземпляр `Illuminate\Support\ValidatedInput`.
``php
$validated = $request->safe()->only(['name', 'email']);

$validated = $request->safe()->except(['name', 'email']);

$validated = $request->safe()->all();
```
#### Итерация
``php
foreach ($request->safe() as $key => $value) {
    //
}
```
#### Доступ как массив
``php
$validated = $request->safe();

$email = $validated['email'];
```


Сессия
---------------
### Intro
- [Laravel Docs - Session](https://laravel.com/docs/8.x/session)

Laravel поставляется с различными бэкендами сессий, доступ к которым осуществляется через
унифицированный API. Поддерживаются Memcached, Redis и базы данных.

#### Конфигурация
Конфигурация сессий находится в файле `config/session.php`.   
По умолчанию Laravel настроен на использование драйвера файловой сессии



### Проверка Isset / Exists
Возвращает `true`, если элемент присутствует и не является `null`:
``php
if ($request->session()->has('users')) {
    //
}
```
Возвращает `true`, если присутствует, даже если он `null`:
``php
if ($request->session()->exists('users')) {
    //
}
```
Возвращает `true`, если элемент `null` или не существует:
``php
if ($request->session()->missing('users')) {
    //
}
```


### Получение данных {.row-span-2}
#### Через запрос
``php
// ...
class UserController extends Controller
{
    public function show(Request $request, $id)
    {
        $value = $request->session()->get('key');

        //
    }
}
```
Передаем значение по умолчанию в качестве второго аргумента для использования
если ключ не существует
``php
$value = $request->session()->get('key', 'default');

// закрытие может быть передано и выполнено по умолчанию
$value = $request->session()->get('key', function () {
    return 'default';
});
```
#### Через помощник сессии
```php
Route::get('/home', function () {
    // Получаем часть данных из сессии...
    $value = session('key');

    // Указание значения по умолчанию...
    $value = session('key', 'default');

    // Сохраняем часть данных в сессии...
    session(['key' => 'value']);
});
```
См: [Session Helper]()

#### Все данные сессии
``php
$data = $request->session()->all();
```
#### Извлечение и удаление
Получение и удаление элемента из сессии
``php
$value = $request->session()->pull('key', 'default');
```

### Хранение данных
Через экземпляр запроса
``php
$request->session()->put('key', 'value');
```
Через глобальный помощник "сессия"
``php
session(['key' => 'value']);
```
Вставка нового значения в значение сессии, являющееся массивом
``php
// массив имен команд
$request->session()->push('user.teams', 'developers');
```


Ведение журнала
---------------

### Конфигурация
Параметры конфигурации поведения журнала находятся в файле `config/logging.php`.  
По умолчанию Laravel при записи сообщений в журнал будет использовать канал стека, который объединяет несколько каналов журнала в один канал.

### Уровни {.row-span-2}
Доступны все уровни логирования, определенные в спецификации [RFC 5424](https://tools.ietf.org/html/rfc5424):
- emergency
- предупреждение
- критический
- ошибка
- предупреждение
- уведомление
- информация
- отладка

### Фасад журнала {.row-span-2}
``php
использовать Illuminate\Support\Facades\Log;

Log::emergency($message);
Log::alert($message);
Log::critical($message);
Log::error($message);
Log::warning($message);
Log::notice($message);
Log::info($message);
Log::debug($message);
```

### Контекстная информация
``php
использовать Illuminate\Support\Facades\Log;

Log::info('Пользователю не удалось войти в систему.', ['id' => $user->id]);
```


Развертывание
---------------
### Intro
- [Laravel Docs - Deployment](https://laravel.com/docs/8.x/deployment)
 
Убедитесь, что ваш веб-сервер направляет все запросы к файлу `public/index.php` вашего приложения

### Оптимизация
#### Карта автозагрузки Composer'а.
``bash
composer install --optimize-autoloader --no-dev
```
#### Загрузка конфигурации
Убедитесь, что вы вызываете функцию `env` только из своих конфигурационных файлов.   
После кэширования конфигурации файл `.env` не будет загружаться, а все вызовы функции `env` для
функции `env` для переменных `.env` будут возвращать `null`.
``bash
php artisan config:cache
```
#### Загрузка маршрутов
``bash
php artisan route:cache
```
#### Загрузка представления
``bash
php artisan view:cache
```

### Режим отладки
Опция debug в файле `config/app.php` определяет, сколько информации
об ошибке, отображаемой пользователю.  
По умолчанию эта опция устанавливается в значение переменной окружения `APP_DEBUG` в файле `.env`.
в файле `.env`.
В производственной среде это значение всегда должно быть `false`.   
Если переменная `APP_DEBUG` будет установлена в значение `true` в производственной среде, вы рискуете открыть конечным пользователям конфиденциальные значения конфигурации.



Также см.
-------
- [Laravel Docs](https://laravel.com/docs/8.x)
- [Laracasts](https://laracasts.com/)
- [Laravel API](https://laravel.com/api/8.x/)
