# Ras-Rain-Detector

肝度:[![wakatime](https://wakatime.com/badge/user/b2ca97db-bce2-4b9b-8588-23c0de16890a/project/4abdce95-6975-4e73-ac71-6ba798d263ca.svg)](https://wakatime.com/badge/user/b2ca97db-bce2-4b9b-8588-23c0de16890a/project/4abdce95-6975-4e73-ac71-6ba798d263ca)

USTB Raspberry Development homework

----

## 功能

`Ras-Rain-Detector`是一款可以实时监测天气并提醒用户及时关窗的程序, 基于树莓派平台实现

### 实时气温检测

启动程序后会在控制台持续显示`当前气温` `降水情况` `关窗情况`等, 待机指示灯绿色常量

````
Ras-Rain-Detector
Temp: 26.9C
Raining: False
Window: Opened
````

### 下雨关窗提醒

当检测到下雨且用户窗户打开时, 会提醒用户关窗, 此时指示灯变为红色, 窗户关闭后重新变绿

```
Ras-Rain-Detector
Temp: 21.9C
Raining: True
Window: Opened
!!!Close the window!!!
```



> 以下是开发文档

##  端口规范

### PCM8591

`AIN0`雨滴

`AIN1`湿度

### 树莓派

#### LED

```
makerobo_R = 11 (17)
makerobo_G = 12 (18)
makerobo_B = 13 (27)
```

#### 触摸

```
makerobo_TouchPin = 16 (36)
```

#### U型光电

```
U_photo_PIPin  = 40
```

## 设计

### 触摸开关模块

`touch.py`

封装函数`is_touch`, 检测到触摸返回`True`, 否则返回`False`

### LED模块

`LED.py`

待机状态指示灯绿色常亮

函数`change_LED`, 被调用时改变当前指示灯颜色, 红变绿, 绿变红

函数`clear_LED`, 被调用时关闭LED灯并释放`GPIO`接口


### 模拟温度传感模块

`thermistor.py`

函数`thm_loop`连续读取当前温度

### 雨滴传感模块

`rain.py`

函数`rain_mainloop`持续读取当前是否下雨

### 光电门传感模块

`U_photo.py`

初始化函数`init`负责设置`GPIO`时间监听器

函数`loop`在输入变化时显示当前状态

----

