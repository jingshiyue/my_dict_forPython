@echo off
REM ******************set /p /a语法*****************************************************************************
REM set /p POP=请输入ping的次数：/P 命令行开关允许将变量数值设成用户输入的一行输入。读取输入行之前，显示指定的 promptString。promptString 可以是空的。
REM set /p t=input:
REM echo %t%

REM set /a a=%a%+1
REM if %a%==255 exit
REM ******************set /p /a语法*****************************************************************************

REM pushd 切换工作路径
REM set current_dir=.\Export\build\FaceSDKTest
REM pushd %current_dir%  
%path% 系统路径，环境变量

1>nul 意思是不显示命令运行的正确提示
2>nul 是不显示错误提示
一起就是 正确错误的都不显示
>是重定向符号
nul是空设备的意思
把提示输入到空设备就不显示了

for /l %%i in (0,1,9) do ( 
    set/p= *<nul  set/p声明变量的用法，将变量名省略，而<nul得意思是输入回车但不换行。这个作用类似于echo，但echo会换行。
    )
for /f "delims=" %%i in ('echo please enter your choice: ') do set /p=%%i<nul  显示提示信息
REM ********************if 语法***************************************************************************
REM if exist D:\workfile\zhongkeyuan_workspace\README0.md (
	REM echo yes
REM ) else (
	REM echo not
REM )

REM ****************************************
REM if exist D:\workfile\zhongkeyuan_workspace\README0.md (
	REM echo yes
REM ) else if 1==2 (
	REM echo 1==2
REM ) else (
	REM echo end
REM )

REM @echo off
REM set /p t=input:
REM echo %t%
REM if %t%==a (
	REM goto labe_a
REM ) else if %t% == b (
	REM goto labe_b
REM ) else (
	REM goto end
REM )

REM :labe_a
REM echo in labe_a
REM pause
REM exit

REM :labe_b
REM echo in labe_b
REM pause
REM exit

REM :end
REM echo in end
REM pause
REM exit
REM ****************************************

REM ********************if 语法***************************************************************************


REM **************************for 语法*********************************************************************
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

REM **************************for 语法*********************************************************************









