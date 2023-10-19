---
Название: Перейти
дата: 2020-12-17 21:51:44
фон: bg-[#4ba4cc]
теги:
    - Go
категории:
    - Программирование
intro: |
    В этой шпаргалке представлены базовый синтаксис и методы, которые помогут вам в использовании [Go](https://go.dev/).
плагины:
    - copyCode
---


Начало работы
--------



### hello.go
``go
пакет main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
}
```
Запуск непосредственно
``Основной сценарий
$ go run hello.go
Привет, мир!
```
Или попробуйте это сделать в [Go repl](https://repl.it/languages/go)



### Переменные
``go
var s1 string
s1 = "Learn Go!"

// Объявление нескольких переменных одновременно
var b, c int = 1, 2
var d = true
```
Краткое объявление
``go
s1 := "Learn Go!"        // string
b, c := 1, 2 // int
d := true // bool
```

См: [Базовые типы](#go-basic-types)



### Функции
``go
пакет main

import "fmt"

// Точка входа программ
func main() {
    fmt.Println("Hello world!")
    say("Hello Go!")
}

func say(message string) {
    fmt.Println("Вы сказали: ", message)
}
```
См: [Функции](#go-functions)



### Комментарии
``go
// Однострочный комментарий

/* Многострочный
 многострочный комментарий */
```



### Утверждение If
``go
if true {
    fmt.Println("Да!")
}
```
См: [Управление потоком](#go-flow-control)



Типы Go Basic
--------

### Строки

``go
s1 := "Hello" + "World"

s2 := ``Сырой`` строковый литерал
может включать разрывы строк.

// Выходные данные: 10
fmt.Println(len(s1))

// Выходные данные: Hello
fmt.Println(string(s1[0:5]))
```
Строки имеют тип `string`.


### Числа

``go
num := 3 // int
num := 3.        // float64
num := 3 + 4i // complex128
num := byte('a') // byte (псевдоним: uint8)

var u uint = 7 // uint (unsigned)
var p float32 = 22.7 // 32-битный float
```
Операторы ####
``go
x := 5
x++
fmt.Println("x + 4 =", x + 4)
fmt.Println("x * 4 =", x * 4)
```
См: [Больше операторов](#go-operators-and-punctuation)




### Булевы

``go
isTrue := true
isFalse := false
```

#### Операторы
``go
fmt.Println(true && true) // true
fmt.Println(true && false) // false
fmt.Println(true || true) // true
fmt.Println(true || false) // true
fmt.Println(!true) // false
```
См: [Больше операторов](#go-operators-and-punctuation)




### Массивы {.row-span-2}
``go
┌────┬────┬────┬────┬─────┬─────┐
| 2 | 3 | 5 | 7 | 11 | 13 |
└────┴────┴────┴────┴─────┴─────┘
  0 1 2 3 4 5
```

---

``го
primes := [...]int{2, 3, 5, 7, 11, 13}
fmt.Println(len(primes)) // => 6

// Выходные данные: [2 3 5 7 11 13]
fmt.Println(primes)

// То же, что и [:3], Выходные данные: [2 3 5]
fmt.Println(primes[0:3])
```
---
``go
var a [2]string
a[0] = "Hello"
a[1] = "World"

fmt.Println(a[0], a[1]) //=> Hello World
fmt.Println(a) // => [Hello World]
```
#### 2d массив
``go
var TwoDimension [2][3]int
for i := 0; i < 2; i++ {
    for j := 0; j < 3; j++ {
        twoDimension[i][j] = i + j
    }
}
// => 2d:  [[0 1 2] [1 2 3]]
fmt.Println("2d: ", twoDimension)
```



### Указатели

``go
func main () {
  b := *getPointer()
  fmt.Println("Значение равно", b)
}
```


``go
func getPointer () (myPointer *int) {
  a := 234
  return &a
}
```


``go
a := new(int)
*a = 234
```

См: [Указатели](https://tour.go.dev/moretypes/1)


### Ломтики

``go
s := make([]string, 3)
s[0] = "a"
s[1] = "b"
s = append(s, "d")
s = append(s, "e", "f")

fmt.Println(s)
fmt.Println(s[1])
fmt.Println(len(s))
fmt.Println(s[1:3])

slice := []int{2, 3, 4}
```

См. также: [Пример с ломтиками](https://gobyexample.com/slices)






### Константы
``go
const s string = "константа"
const Phi = 1,618
const n = 500000000
const d = 3e20 / n
fmt.Println(d)
```




### Преобразования типов

``go
i := 90
f := float64(i)
u := uint(i)

// Будет равно символу Z
s := string(i)
```

#### Как получить строку int?

``go
i := 90

// необходимо импортировать "strconv"
s := strconv.Itoa(i)
fmt.Println(s) // Выходные данные: 90
```




Строки Go
--------

### Функция строк
``go
пакет main

импорт (
	"fmt"
	s "strings"
)

func main() {
    /* Необходимо импортировать strings как s */
	fmt.Println(s.Contains("test", "e"))

    /* Встраивание */
    fmt.Println(len("hello"))  // => 5
    // Выходные данные: 101
	fmt.Println("hello"[1])
    // Выходные данные: e
	fmt.Println(string("hello"[1]))

}
```



### fmt.Printf {.row-span-2 .col-span-2}
``go
пакет main

import (
	"fmt"
	"os"
)

тип точка struct {
	x, y int
}

func main() {
	p := точка{1, 2}
	fmt.Printf("%v\n", p) // => {1 2}
	fmt.Printf("%+v\n", p) // => {x:1 y:2}
	fmt.Printf("%#v\n", p) // => main.point{x:1, y:2}
	fmt.Printf("%T\n", p) // => main.point
	fmt.Printf("%t\n", true) // => TRUE
	fmt.Printf("%d\n", 123) // => 123
	fmt.Printf("%b\n", 14) // => 1110
	fmt.Printf("%c\n", 33) // => !
	fmt.Printf("%x\n", 456) // => 1c8
	fmt.Printf("%f\n", 78.9) // => 78.9
	fmt.Printf("%e\n", 123400000.0) // => 1.23E+08
	fmt.Printf("%E\n", 123400000.0) // => 1.23E+08
	fmt.Printf("%s\n", "\"string\") // => "string"
	fmt.Printf("%q\n", "\"string\") // => "\"string\"
	fmt.Printf("%x\n", "hex this") // => 6.86578E+15
	fmt.Printf("%p\n", &p) // => 0xc00002c040
	fmt.Printf("|%6d|%6d|\n", 12, 345) // => | 12| 345|
	fmt.Printf("|%6.2f|%6.2f|\n", 1.2, 3.45) // => | 1.20| 3.45|
	fmt.Printf("|%-6.2f|%-6.2f|\n", 1.2, 3.45) // => |1.20 |3.45 |
	fmt.Printf("|%6s|%6s|\n", "foo", "b") // => | foo| b|
	fmt.Printf("|%-6s|%-6s|\n", "foo", "b") // => |foo |b |

	s := fmt.Sprintf("a %s", "string")
	fmt.Println(s)

	fmt.Fprintf(os.Stderr, "an %s\n", "error")
}

```
См. также: [fmt](https://go.dev/pkg/fmt/)




### Примеры функций
| Пример | Результат |
|-------------------------------|-------------|
| Contains("test", "es") | true |
| Count("test", "t") | 2 |
| HasPrefix("test", "te") | true |
| HasSuffix("test", "st") | true |
| Index("test", "e") | 1 | |
| Join([]string{"a", "b"}, "-") | a-b |
| Repeat("a", 5) | aaaaa |
| Replace("foo", "o", "0", -1) | f00 |
| Replace("foo", "o", "0", 1) | f0o |
| Split("a-b-c-d-e", "-") | [a b c d e] | |
| ToLower("TEST") | test |
| ToUpper("test") | TEST |



Перейти к управлению потоком
--------

### Условный

``go

a := 10

if a > 20 {
    fmt.Println(">")
} else if a < 20 {
    fmt.Println("<")
} else {
    fmt.Println("=")
}
```

### Выражения в if

``go
x := "hello go!"

if count := len(x); count > 0 {
    fmt.Println("Yes")
}

```
---
``go

if _, err := doThing(); err != nil {
    fmt.Println("О-о-о")
}
```

### Переключатель
```go {.wrap}
x := 42.0
switch x {
case 0:
case 1, 2:
    fmt.Println("Несколько совпадений")
case 42:   // Не "провалиться".
    fmt.Println("достигнуто")
case 43:
    fmt.Println("Не достигнуто")
default:
    fmt.Println("Необязательно")
}
```

См: [Switch](https://github.com/golang/go/wiki/Switch)

### Цикл For

``go
for i := 0; i <= 10; i++ {
  fmt.Println("i: ", i)
}
```

### Цикл For-Range

```go {.wrap}
nums := []int{2, 3, 4}
sum := 0
for _, num := range nums {
    sum += num
}
fmt.Println("sum:", sum)
```

### Цикл While

```go
i := 1
for i <= 3 {
    fmt.Println(i)
    i++
}
```

### Продолжение ключевого слова
```go
for i := 0; i <= 5; i++ {
    if i % 2 == 0 {
        продолжить
    }
    fmt.Println(i)
}
```
### Ключевое слово Break
```go
for {
    fmt.Println("цикл")
    break
}
```



Структуры и карты Go
--------

### Определение {.row-span-2}

``go
пакет main

import (
	"fmt"
)

тип Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v.X, v.Y) // => 4 2
}
```

См: [Structs](https://tour.go.dev/moretypes/2)

### Литералы

``go
v := Vertex{X: 1, Y: 2}
// Имена полей могут быть опущены
v := Vertex{1, 2}
// Y является неявным
v := Vertex{X: 1}
```

Можно также поместить имена полей.


### Карты {.row-span-2}
``go
m := make(map[string]int)
m["k1"] = 7
m["k2"] = 13
fmt.Println(m) // => map[k1:7 k2:13]

v1 := m["k1"]
fmt.Println(v1) // => 7
fmt.Println(len(m)) // => 2

delete(m, "k2")
fmt.Println(m) // => map[k1:7]

_, prs := m["k2"]
fmt.Println(prs) // => false

n := map[string]int{"foo": 1, "bar": 2}
fmt.Println(n) // => map[bar:2 foo:1]
```


### Указатели на структуры

``go
v := &Vertex{1, 2}
v.X = 2
```

Выполнение операции `v.X` аналогично выполнению операции `(*v).X`, когда `v` является указателем.





Перейти к функциям
--------


### Множественные аргументы
``go
func plus(a int, b int) int {
    return a + b
}
func plusPlus(a, b, c int) int {
    return a + b + c
}
fmt.Println(plus(1, 2))
fmt.Println(plusPlus(1, 2, 3))
```

### Множественный возврат

``go
func vals() (int, int) {
    return 3, 7
}

a, b := vals()
fmt.Println(a) // => 3
fmt.Println(b) // => 7
```

### Литералы функций

``go
r1, r2 := func() (string, string) {
    x := []string{"hello", "cheatsheets.zip"}
    return x[0], x[1]
}()

// => hello cheatsheets.zip
fmt.Println(r1, r2)
```

### Голый возврат

``go
func split(sum int) (x, y int) {
  x = sum * 4 / 9
  y = sum - x
  return
}

x, y := split(17)
fmt.Println(x) // => 7
fmt.Println(y) // => 10
```

Заметим, что использование голых возвратов ухудшает читаемость.

### Вариативные функции
``go
func sum(nums ...int) {
    fmt.Print(nums, " ")
    total := 0
    for _, num := range nums {
        total += num
    }
    fmt.Println(total)
}
sum(1, 2) //=> [1 2] 3
sum(1, 2, 3) // => [1 2 3] 6

nums := []int{1, 2, 3, 4}
sum(nums...) // => [1 2 3 4] 10
```


### функция инициализации
```go
import --> const --> var --> init()
```
---
``go
var num = setNumber()

func setNumber() int {
    return 42
}
func init() {
    num = 0
}
func main() {
    fmt.Println(num) // => 0
}
```


### Функции как значения
``go
func main() {
    // присваиваем функции имя
    add := func(a, b int) int {
        return a + b
    }
    // используем имя для вызова функции
    fmt.Println(add(3, 4)) // => 7
}
```

### Закрытия 1
``go
func scope() func() int{
    outer_var := 2
    foo := func() int {return outer_var}
    return foo
}

// Outpus: 2
fmt.Println(scope()())
```

### Закрытия 2
``go
func outer() (func() int, int) {
    outer_var := 2
    inner := func() int {
        outer_var += 99
        return outer_var
    }
    inner()
    return inner, outer_var
}
inner, val := outer()
fmt.Println(inner()) // => 200
fmt.Println(val) // => 101
```


Пакеты Go
--------


### Импортирование {.row-span-2}

``go
import "fmt"
import "math/rand"
```
#### То же самое, что
``go
импорт (
  "fmt" // дает fmt.Println
  "math/rand" // дает rand.Intn
)
```

См: [Импортирование](https://tour.go.dev/basics/1)




### Псевдонимы {.row-span-2}

``go
import r "math/rand"
```
---
``go
импорт (
    "fmt"
    r "math/rand"
)
```
---
``go
r.Intn()
```


### Пакеты

``go
пакет main

// Внутренний пакет может быть импортирован только другим пакетом
// который находится внутри дерева, укорененного в родителе внутреннего каталога
пакет internal
```

См: [Внутренние пакеты](https://go.dev/doc/go1.4#internalpackages)

### Экспорт имен

``go
// Начинаются с заглавной буквы
func Hello () {
  ---
}
```

См: [Экспортированные имена](https://tour.go.dev/basics/3)



Go Concurrency
--------

### Goroutines {.row-span-2}

``go
пакет main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {
	f("direct")
	go f("goroutine")

	go func(msg string) {
		fmt.Println(msg)
	}("go")

	time.Sleep(time.Second)
	fmt.Println("done")
}
```


См: [Goroutines](https://tour.go.dev/concurrency/1), [Channels](https://tour.go.dev/concurrency/2)




### WaitGroup {.row-span-2}

``go
пакет main

import (
	"fmt"
	"sync"
	"time"
)

func w(id int, wg *sync.WaitGroup) {
	отложить wg.Done()
	fmt.Printf("%d starting\n", id)

	time.Sleep(time.Second)
	fmt.Printf("%d done\n", id)
}

func main() {
	var wg sync.WaitGroup
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go w(i, &wg)
	}
	wg.Wait()
}
```
См: [WaitGroup](https://go.dev/pkg/sync/#WaitGroup)




### Закрытие каналов

``go
ch <- 1
ch <- 2
ch <- 3
close(ch) // Закрытие канала
```
---
``go
// Итерация канала до закрытия
for i := range ch {
  ---
}
```
---
``go
// Закрыто, если `ok == false`
v, ok := <- ch
```

См: [Range and close](https://tour.go.dev/concurrency/4)



### Буферизованные каналы

``go
ch := make(chan int, 2)
ch <- 1
ch <- 2
ch <- 3
// фатальная ошибка:
// все горутины спят - тупик
```

См: [Буферизованные каналы](https://tour.go.dev/concurrency/3)





Перейти к контролю ошибок
--------

### Отложенные функции

``go
func main() {
  defer func() {
    fmt.Println("Выполнено")
  }()
  fmt.Println("Работает...")
}
```


### Лямбда defer

``go
func main() {
  var d = int64(0)
  defer func(d *int64) {
    fmt.Printf("& %v Unix Sec\n", *d)
  }(&d)
  fmt.Print("Выполнено ")
  d = time.Now().Unix()
}
```

Функция defer использует текущее значение d, если только мы не используем указатель для получения конечного значения в конце main.




### Defer

``go
func main() {
  defer fmt.Println("Готово")
  fmt.Println("Работает...")
}
```

См: [Отсрочка, паника и восстановление](https://blog.go.dev/defer-panic-and-recover)



Перейти к методам {.cols-2}
--------

### Приемники

``go
type Vertex struct {
  X, Y float64
}
```

``go
func (v Vertex) Abs() float64 {
  return math.Sqrt(v.X * v.X + v.Y * v.Y)
}
```


``go
v := Vertex{1, 2}
v.Abs()
```

См: [Методы](https://tour.go.dev/methods/1)

### Мутация

``go
func (v *Vertex) Scale(f float64) {
  v.X = v.X * f
  v.Y = v.Y * f
}
```


``go
v := Vertex{6, 12}
v.Scale(0.5)
// `v` обновляется
```

См: [Приемники указателей](https://tour.go.dev/methods/4)

Интерфейсы Go {.cols-2}
--------

### Базовый интерфейс

``go
type Shape interface {
  Площадь() float64
  Периметр() float64
}
```

### Структура

``go
type Rectangle struct {
  Длина, Ширина float64
}
```

Структура `Rectangle` неявно реализует интерфейс `Shape`, реализуя все его методы.

### Методы

``go
func (r Rectangle) Area() float64 {
  return r.Length * r.Width
}

func (r Rectangle) Perimeter() float64 {
  return 2 * (r.Length + r.Width)
}
```

Методы, определенные в `Shape`, реализованы в `Rectangle`.

### Пример интерфейса

``go {.wrap}
func main() {
  var r Shape = Rectangle{Length: 3, Width: 4}
  fmt.Printf("Тип r: %T, Площадь: %v, Периметр: %v.", r, r.Area(), r.Perimeter())
}
```

Разное
-------------

### Ключевые слова
- перерыв
- по умолчанию
- func
- интерфейс
- выбор
- случай
- отложить
- идти
- карта
- структура
- чан
- else
- перейти
- пакет
- переключатель
- const
- провал
- если
- диапазон
- тип
- продолжать
- для
- импорт
- возврат
- var
{.cols-3 .marker-none}

### Операторы и пунктуация
| | | | | | | | | |
|---|----|-----|-----|------|----|-----|---|---|
| + | & | += | &= | && | == | != | ( | ) |
| - | \| | -= | \|= | \|\| | < | <= | [ | ] |
| * | ^ | *= | ^= | <- | > | >= | { | } |
| / | << | /= | <<= | ++ | = | := | , | ; |
| % | >> | %= | >>= | -- | !  | ... | . | : |
| | &^ | &^= | | | | | | |



Также см. {.cols-1}
--------
- [Devhints](https://devhints.io/go) _(devhints.io)_
- [A tour of Go](https://tour.go.dev/welcome/1) _(tour.go.dev)_
- [Go wiki](https://github.com/golang/go/wiki/) _(github.com)_
- [Эффективный Go](https://go.dev/doc/effective_go) _(go.dev)_
- [Go by Example](https://gobyexample.com/) _(gobyexample.com)_
- [Awesome Go](https://awesome-go.com/) _(awesome-go.com)_
- [JustForFunc Youtube](https://www.youtube.com/channel/UC_BzFbxG2za3bp5NRRRXJSw) _(youtube.com)_
- [Руководство по стилю](https://github.com/golang/go/wiki/CodeReviewComments) _(github.com)_




