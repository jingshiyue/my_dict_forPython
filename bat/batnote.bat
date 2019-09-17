@echo off
REM if exist D:\workfile\zhongkeyuan_workspace\README0.md (
	REM echo yes
REM ) else (
	REM echo not
REM )


REM if exist D:\workfile\zhongkeyuan_workspace\README0.md (
	REM echo yes
REM ) else if 1==2 (
	REM echo 1==2
REM ) else (
	REM echo end
REM )


REM ***********************************************************************************************
REM /r recursion 
REM /d directory
REM *正则批配任意字符  ?批配一个字符
REM /d遍历目录
REM /r 递归遍历文件
REM /l 迭代数值范围
REM /f 文件内容


REM 在cmd窗口中：for %I in (command1) do command2 
REM 在批处理文件中：for %%I in (command1) do command2
REM in和do之间的command1表示的字符串或变量可以是一个，也可以是多个，每一个字符串或变量，我们称之为一个元素，每个元素之间，用空格键、跳格键、逗号、分号或等号分隔；
REM type /?
REM pause

REM @echo off
REM for  %%I in (A,B,C) do (
REM echo %%I
REM )


REM @echo off
REM for %%i in (*.txt) do echo "%%i"
REM pause
REM echo afterpause
REM pause
REM echo afterpausepause
REM pause
REM echo afterpause


REM for /d /r %%i in (test*) do echo "%%i"

REM 下面三种是递归遍历目录下的文件
REM for /r  D:\workfile\zhongkeyuan_workspace %%i in (*) do echo "%%i"
REM for /r  ./ %%i in (*) do echo "%%i"
REM for /r  .\ %%i in (*) do echo "%%i"

REM 递归遍历目录，目录名有test
REM for /d /r %%i in (test*) do echo "%%i"

REM 相当于range(0,5,10)
REM >> 重定向 追加
REM > 重定向 覆盖
REM for /l %%i in (0,5,100000000000) do (
    REM @echo %%i >>log.log
	REM pause
REM )

REM %%i %%j %%k %%m 字母连续
REM for /f "tokens=2,4,8,11 delims= " %%i in (log.log) do echo %%i %%j %%k %%m

REM ***********************************************************************************************







