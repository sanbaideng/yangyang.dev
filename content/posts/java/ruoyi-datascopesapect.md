---
title: "若依权限范围"
date: 2023-08-25T10:39:58+08:00
draft: false
tags: ["springboot","ruoyi"]
---

# 若依框架 权限范围dataScope概览

- TLDR;切面+注解+mybatis定位符(对应三个文件DataScopeAspect.java,SysUserServiceImpl.java,SysUserMapper.xml 、BaseEntity.java中的params.dataScope属性)

## 0.BaseEntity类中有属性params，里面可以放需要注入的sql
```
    private Map<String, Object> params;
```

## 1.DataScopeAspect定义切面
DataScopeAspect类，定义了五种权限范围，
```
DATA_SCOPE_ALL = "1"             //全部数据权限
DATA_SCOPE_CUSTOM = "2";         //自定数据权限
DATA_SCOPE_DEPT = "3";           //部门数据权限
DATA_SCOPE_DEPT_AND_CHILD = "4"; //部门及以下数据权限
DATA_SCOPE_SELF = "5";           //仅本人数据权限
```


```
//如果不是超级管理员
if (StringUtils.isNotNull(currentUser) && !currentUser.isAdmin())

//执行权限过滤方法
dataScopeFilter(JoinPoint joinPoint, SysUser user, String deptAlias, String userAlias)

//根据用户user的roles(可多个角色)，找到各角色的权限范围的类型，判断，然后追加sql语句
//循环 //最后得到需要追加的sqlString
for (SysRole role : user.getRoles())

//最后判断 如果sqlString不为空
if (StringUtils.isNotBlank(sqlString.toString()))

//而且方法的参数是BaseEntity类型/子类型 （如果有新类型，在这里添加）
if (StringUtils.isNotNull(params) && params instanceof BaseEntity)

//则在参数类的属性params.dataScope赋值sqlString
baseEntity.getParams().put(DATA_SCOPE, " AND (" + sqlString.substring(4) + ")");

```

## 2.SysUserServiceImpl注解
```
    @Override
    @DataScope(deptAlias = "d", userAlias = "u")
    public List<SysUser> selectUserList(SysUser user)
    {
        return userMapper.selectUserList(user);
    }
```

## 3.SysUserMapper.xml中在合适的位置写入 ${params.dataScope}

- 什么叫合适的位置
  插入的语句是and 条件语句，所以需要在where和order by等之间，不然sql运行会报错。
```
<select id="selectUserList" parameterType="SysUser" resultMap="SysUserResult">
		select u.* from sys_user u
		left join sys_dept d on u.dept_id = d.dept_id
		where u.del_flag = '0'
		<if test="userId != null and userId != 0">
			AND u.user_id = #{userId}
		</if>
		<!-- 数据范围过滤 -->
		${params.dataScope}
	</select>
```


总结：
关键点：
- 1.是mybatis中，标记好需要追加的位置；
- 2.在方法注解中 标明sys_dept,sys_user的别名(在DataScopeAspect中拼接sqlString时要用到)
