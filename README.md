# 我要干啥来着 what-was-i-doing

## 介绍

有时候我们可能会开启多线程模式，经常可能突然来了一个消息或者想到一个东西去查查，结果突然就开始想“诶，我刚才是要干啥来着？”。

为了防止这种情况的出现，写了一个小窗口，可以随时记录自己刚刚准备要干什么，以防自己忘了自己在干什么。

听起来有点憨批，但其实也挺有用的。

## 注意

windows 缓存会保存在：`C:\Users\你的用户名\AppData\Local\LiRen\what-was-i-doing` 这里

## 开发

打包

```commandline
pyinstaller --onefile --windowed --icon=./assets/favicon.ico main.py -n what-was-i-doing
```

踩坑：必须把pyinstaller安装在虚拟环境里，然后打包前激活虚拟环境再输入上面的指令。







