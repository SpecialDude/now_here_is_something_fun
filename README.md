# now here is something fun

>## [Read story on medium](https://medium.com/@warithadetayo.awa/now-here-is-something-fun-346ac202e5f0)

```py
>>> def sum_digits(num):
...     if num / 10 < 1:
...         return num
...     return (num % 10) + sum_digits(num // 10)
... 
>>> list(map(lambda x : sum_digits(x * 9), range(1, 10)))
[9, 9, 9, 9, 9, 9, 9, 9, 9]
>>>
```

![Radix-Minus in all Base Systems](number_base.gif)
