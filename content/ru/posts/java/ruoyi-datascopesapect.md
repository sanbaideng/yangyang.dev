---
title: "Проснись и узнай о масштабах власти"
date: 2023-08-25T10:39:58+08:00
тэги: ["springboot", "ruoyi"]
---
# Если вы следуете фреймворку Permission Scope dataScope Overview

- TLDR; фасеты + аннотации + локаторы mybatis (соответствуют 4 файлам DataScopeAspect.java, SysUserServiceImpl.java, SysUserMapper.xml и свойству params.dataScope в BaseEntity.java) ps: Официальный сайт Ruoyi: https://ruoyi.vip/

## 0. Класс BaseEntity имеет свойство params, в котором может храниться инжектируемый sql.
```
    private Map<String, Object> params; ``...
```

## 1. DataScopeAspect определяет фасеты
Класс DataScopeAspect, определяющий пять диапазонов разрешений, соответствует тому, как назначаются разрешения на данные для роли
```
DATA_SCOPE_ALL = "1" // Все разрешения на работу с данными
DATA_SCOPE_CUSTOM = "2"; // Пользовательские привилегии на данные
DATA_SCOPE_DEPT = "3"; //Права на ведомственные данные
DATA_SCOPE_DEPT_AND_CHILD = "4"; //Права на данные от отдела и ниже
DATA_SCOPE_SELF = "5"; //Права только на персональные данные
``


```
//Если пользователь не является администратором
if (StringUtils.isNotNull(currentUser) && !currentUser.isAdmin())

//Выполняем метод фильтрации разрешений
dataScopeFilter(JoinPoint joinPoint, SysUser user, String deptAlias, String userAlias)

//В соответствии с ролями пользователя user (возможно использование нескольких ролей) находим тип области разрешения каждой роли, судим, а затем добавляем sql-оператор.
// цикл // наконец, получить необходимость добавления sqlString
for (SysRole role : user.getRoles())

// окончательное суждение, если sqlString не является null
if (StringUtils.isNotBlank(sqlString.toString())))))

//и аргументами метода являются типы/подтипы BaseEntity (если есть новые типы, добавьте их сюда)
if (StringUtils.isNotNull(params) && params instanceof BaseEntity)

// то присваиваем sqlString свойству params.dataScope класса params
baseEntity.getParams().put(DATA_SCOPE, " AND (" + sqlString.substring(4) + ")");

``

## 2. Метод SysUserServiceImpl selectUserList пишет аннотацию
```
    @Override
    @DataScope(deptAlias = "d", userAlias = "u")
    public List<SysUser> selectUserList(SysUser user)
    {
        return userMapper.selectUserList(user);
    }
``

## 3. В SysUserMapper.xml пропишите ${params.dataScope} в соответствующем месте в selectUserList.

- Что вы имеете в виду под соответствующим местом?
  Оператор вставки является условным оператором AND, поэтому он должен находиться между операторами where, order by и т.д., иначе sql будет выполняться с ошибкой.
```
<select id="selectUserList" parameterType="SysUser" resultMap="SysUserResult">
select u.* from sys_user u
left join sys_dept d on u.dept_id = d.dept_id
where u.del_flag = '0'
<if test="userId ! = null и userId ! = 0">
AND u.user_id = #{userId}
</if
<! -- Фильтрация области данных -->
${params.dataScope}
</select
``


Резюме:

- 1. в mybatis отметить место, которое необходимо добавить;
- 2. в аннотации метода отметить псевдонимы sys_dept, sys_user (для использования при сращивании sqlString в DataScopeAspect)
