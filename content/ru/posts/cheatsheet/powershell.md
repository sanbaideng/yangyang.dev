---
название: Powershell
дата: 2020-11-25 18:28:43
фон: bg-[#397fe4]
теги:
    - скрипт
    - окна
категории:
    - Программирование
    - Операционная система
intro: Это краткая шпаргалка по началу работы с Powershell-сценариями.
плагины:
    - copyCode
---

Основные команды
---------------

### Вспомогательные команды

***Powershell использует формат "глагол-существительное" для своих команд.***

Некоторые распространенные глаголы:
| Verb | Description |
|----------|--------------------------------------------------|
Получить | Get | Используется для получения информации.                   |
| Установить | Используется для настройки или изменения параметров.           |
| | New | Используется для создания новых экземпляров объектов.        |
| | Remove | Используется для удаления или удаления объектов.                 |
| | Invoke | Используется для выполнения определенного действия или операции. |
| Start | Используется для запуска процесса или операции.        |
| Stop | Приостановить или завершить процесс или операцию.|
| Enable | Используется для активации или включения функции.           |
| Отключить | Используется для деактивации или отключения функции.        |
| Test | Используется для выполнения тестов или проверок.                |
| Обновить | Используется для обновления данных или конфигураций.|


Список доступных модулей
``powershell
Get-Module --ListAvailable
```
Перечисляет доступные команды и функции.
``powershell
Get-Command -Module ActiveDirectory
```
Получает справку
``powershell
Get-Help <cmd>
Get-Help <cmd> -Examples
Get-Help -Name Get-Process -Parameter Id
```

Перечисляет псевдонимы и соответствующие им имена команд.
``powershell
Get-Alias | Select-Object Name, Definition
```

**Get-Member:** Отображает свойства и методы объектов.
``powershell
Get-Process | Get-Member
```

### Манипулирование объектами {.col-span-2}

**Select-Object:** Выбирает определенные свойства объектов или настраивает их отображение.
``powershell
Get-Process | Select-Object Name, CPU
```

**Where-Object:** Фильтрует объекты на основе заданных условий.
``powershell
Get-Service | Where-Object { $PSItem.Status -eq 'Running' }
#OR
Get-Service | ? { $_.Status -eq 'Running' }
```

**Measure-Object:** Вычисляет статистику, такую как сумма, среднее и количество, для свойств объекта.
``powershell
Get-Process | Measure-Object -Property WorkingSet -Sum
```

**ForEach-Object:** Выполняет операцию над каждым объектом в коллекции. (ОСТОРОЖНО: нижеприведенная команда создаст префикс файлов/папок в текущем каталоге)
``powershell
Get-ChildItem | ForEach-Object { Rename-Item $_ -NewName "Prefix_$_" }
```

**Sort-Object:** Сортировка объектов по заданным свойствам.
``powershell
Get-ChildItem | Sort-Object Length -Descending
```

**Format-Table:** Форматирует вывод в виде таблицы с указанными столбцами.
```powershell
Get-Service | Format-Table -AutoSize # ft alias
```

**Format-List:** Форматирует вывод в виде списка свойств и значений.
``powershell
Get-Process | Format-List -Property Name, CPU # fl alias
```

### FileSystem {.col-span-2}

``powershell
New-Item -path file.txt -type 'file' -value 'contents'
New-Item -path file.txt -type 'dir'
Copy-Item <src> -destination <dest>
Move-Item -path <src> -destination <dest>
Remove-Item <file>
Test-Path <путь>
Rename-Item -path <path> -newname <newname>

# использование библиотеки базовых классов .NET
[System.IO.File]::WriteAllText('test.txt', '')
[System.IO.File]::Delete('test.txt')

Get-Content -Path "test.txt"
Get-Process | Out-File -FilePath "processes.txt "# Вывод в файл
Get-Process | Export-Csv -Path "processes.csv" # Вывод в csv
$data = Import-Csv -Path "data.csv" # Импорт из csv
```

Управление системой
---------------

### Windows Management Instrumentation {.col-span-2}
``powershell
# Получение информации о BIOS
Get-CimInstance -ClassName Win32_BIOS
# Получение информации о локально подключенных физических дисковых устройствах
Get-CimInstance -ClassName Win32_DiskDrive
# Получение информации об установленной физической памяти (RAM)
Get-CimInstance -ClassName Win32_PhysicalMemory
# Получение информации об установленных сетевых адаптерах (физических + виртуальных)
Get-CimInstance -ClassName Win32_NetworkAdapter
# Получение информации об установленной графической / видеокарте (GPU)
Get-CimInstance -ClassName Win32_VideoController

# Перечислить все имена классов
Get-CimClass | Select-Object -ExpandProperty CimClassName
# Исследовать различные WMI-классы, доступные в пространстве имен root\cimv2
Get-CimClass -Namespace root\cimv2
# Исследование дочерних пространств имен WMI, расположенных под пространством имен root\cimv2
Get-CimInstance -Namespace root -ClassName __NAMESPACE


```

### Управление сетью

``powershell
# Тестирование сетевого подключения к удаленному узлу
Test-Connection -ComputerName google.com

# Получить информацию о сетевом адаптере
Get-NetAdapter

# Получение информации об IP-адресе
Get-NetIPAddress

# Получение информации о таблице маршрутизации
Get-NetRoute

# Проверить, открыт ли порт на удаленном хосте
Test-NetConnection google.com -Port 80

```

### Управление пользователями и группами {.col-span-2}
``powershell
# Получение информации об учетной записи локального пользователя
Get-LocalUser

# Создать новую учетную запись локального пользователя
New-LocalUser -Name NewUser -Password (ConvertTo-SecureString "Password123" -AsPlainText -Force)

# Удалить учетную запись локального пользователя
Remove-LocalUser -Name UserToRemove

# Получить информацию о локальной группе
Get-LocalGroup

# Добавить члена в локальную группу
Add-LocalGroupMember -Group Administrators -Member UserToAdd
```

### Безопасность и разрешения
``powershell
# Получение списков контроля доступа для файла/директории
Get-Acl C:\Path\To\File.txt

# Установить списки контроля доступа для файла/директории
Set-Acl -Path C:\Path\To\File.txt -AclObject $aclObject
```

### Управление реестром {.col-span-2}
``powershell
# Получение значений ключей реестра
Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*" | Select DisplayName, DisplayVersion

# Установить значения ключей реестра
Set-ItemProperty -Path "HKLM:\Software\MyApp" -Name "SettingName" -Value "NewValue"

# Создать новое значение ключа реестра
New-ItemProperty -Path "HKCU:\Software\MyApp" -Name "NewSetting" -Value "NewValue" -PropertyType String

# Удалить значение ключа реестра
Remove-ItemProperty -Path "HKCU:\Software\MyApp" -Name "SettingToRemove"

# Проверить, существует ли ключ реестра
Test-Path "HKLM:\Software\MyApp"
```
Сценарии
---------------

### Переменные {.col-span-2}
Инициализация переменной с/без заданного типа:
``powershell
$var = 0
[int] $var = 'Trevor' # (выбрасывает исключение)
[string] $var = 'Trevor' # (не выбрасывает исключение)
$var.GetType()

# Множественное присваивание
$a,$b,$c = 'a','b','c'

# Создание массива
$arrayvar = @('va1','va2')

# Создать дикту
$dict = @{k1 = 'test'; k2 = 'best'}
```
Команды переменных
``Powershell
New-Variable -Name FirstName -Value Trevor
New-Variable FirstName -Value Trevor -Option <ReadOnly/Constant>

Get-Variable
Get-Variable | ? { $PSItem.Options -contains 'constant' }
Get-Variable | ? { $PSItem.Options -contains 'readonly' }

Remove-Variable -Name firstname
# Удаляет переменную, доступную только для чтения
Remove-Variable -Name firstname -Force
```
Типы переменных
int32, int64, string, bool
### Операторы


``powershell
# операторы
# (a <op> b)

= , += / -= , ++ / --
-eq / -ne , -lt / -gt , -le / -ge

$FirstName = 'Trevor'
$FirstName -like 'T*'
$true; $false #bool true/false

# тернарный оператор
$FoodToEat = $BaconIsYummy ? 'бекон' : 'свекла'

# -notin или -in
'Сельдерей' -in @('Бекон', 'Колбаса', 'Стейк')

# output: True
5 -is [int32]

# совпадение с регексом, можно использовать массив
'Trevor' -match '^T\w*'

# Поиск множественных совпадений.
$regex = [regex]'(\w*)'
$regex.Matches('this is test').Value

```
### Структура
#### Операция ввода-вывода
```powershell
"Выводится строка"

Write-Host "color" -ForegroundColor Red

$age = Read-host "Введите возраст"

$pwd = Read-host "password" -asSecureString

Clear-Host
```
#### Flow Controls
``powershell
IF(<#Condition#>){
<#Команды#>}ELSEIF(){}ELSE{}

Switch($var){
	"val1"{<#Commands#>; break}
    "val2"{<#Commands#>; break}
}

For($ct=0;$ct -le 3;$ct++){}

ForEach($var in $arr){}

while($var -ne 0){}

Do{}While()

```
### Функция / Модули {.row-span-2}

#### Пример 1
``powershell
function funcname{
    
    [CmdletBinding()].
	param(
		[Parameter(Mandatory)]
		[String]$user
	)
	Write-Host "welcome " $user
    return "value"
}
$var = funcname -user pcb
```
#### Пример 2
``powershell
function Get-EvenNumbers {
    [CmdletBinding()].
    param (
        [Parameter(ValueFromPipeline = $true)]
        [int] $Number
    )
    begin {<#команда#>}
    процесс {
        if ($Number % 2 -eq 0) {
            Write-Output $Number
        }
    }
    end {<#команда#>}   
}
1..10 | Get-EvenNumbers

```
#### Модули
``powershell
# powershell ищет модуль по пути
$env:PSModulePath

# выводит список всех модулей, установленных в системе
Get-Module -ListAvailable
# модули, импортированные в текущую сессию
Get-Module

Import-Module <moduleName>
Remove-Module <moduleName>

Find-Module -Tag cloud
Find-Module -Name ps*

# Создать модуль PowerShell в памяти
New-Module -Name trevor -ScriptBlock {
  function Add($a,$b) { $a + $b } }


```

### Советы

- В большинстве языков управляющим символом является обратный слеш **\\\**, тогда как в powershell - обратный тик **`**.
``powershell

```

## Также смотрите {.cols-1}
* [Microsoft Powershell](https://learn.microsoft.com/en-us/powershell/scripting/samples/sample-scripts-for-administration?view=powershell-7.3) _(learn.microsoft.com)_.
