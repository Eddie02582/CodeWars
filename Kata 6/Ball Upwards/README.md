# Ball Upwards

<a href="https://www.codewars.com/kata/ball-upwards/python">原文</a>


You throw a ball vertically upwards with an initial speed v (in km per hour). The height h of the ball at each time t is given by h = v*t - 0.5*g*t*t where g is Earth's gravity (g ~ 9.81 m/s**2). A device is recording at every tenth of second the height of the ball. For example with v = 15 km/h the device gets something of the following form: (0, 0.0), (1, 0.367...), (2, 0.637...), (3, 0.808...), (4, 0.881..) ... where the first number is the time in tenth of second and the second number the height in meter.</br>

## Task

Write a function max_ball with parameter v (in km per hour) that returns the time in tenth of second of the maximum height recorded by the device.

## Example

```
max_ball(15) should return 4
```

```
max_ball(25) should return 7
```

Given a number, *Find if it is Jumping or not .*

Notes
<ul>
    <li>Remember to convert the velocity from km/h to m/s or from m/s in km/h when necessary</li>
    <li>The maximum height recorded by the device is not necessarily the maximum height reached by the ball.</li>   
</ul>


## Solution


sol: 簡單來說 v=vo+at,t=(v-vo)/a,至高點v=0,a=-g=-9.81,t=vo/g,題目有說returns the time in tenth of second ,回傳10*t

``` python
def max_ball(v0):
    v0=v0*1000/3600
    t=v0/9.81
    return round(t*10)
```












