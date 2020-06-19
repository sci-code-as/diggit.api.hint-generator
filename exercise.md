
# Day Of Week - function

Write a Python-function to find day of the week for a given date. 

In this exercise you should write a function that takes in a date and 
returns a day of the week. 
## Starting hints:
You will likely want to use the libraries `datetime` and `calendar` so 
you should import these. 
 
## Style-tips: 
### Structuring your program: 
    - imports 
    - constants and global values (if any)
    - functions 
    - function-calls, dependent variables etc. as needed.

So it should look something like: 
```python
import foo
bar = 0
def foobar(baz):
    # A function that does something, and a comment that describes it.
    return baz
    
print(foobar(bar))
```
### General on style:
Readability counts, so use meaningful names for variables. For 
variables we use lower-case, and if combining we use underscore to bind words. 
e.g. `example_variable`.
 

Functions follow the same conventions as variables, unless there's a good 
reason to break these (e.g. you're working in a codebase which uses a different
convention). So we would prefer here to use the name `find_day` as our function
name. 
 
If you want to look deeper into writing ideomatic python see the PEP-8 documentation, 
(or write `import this` on the top of your code for a little easter egg.)




---
  

Feedback Part 1: 

Missing, or incomplete elements:
- you should start using the method `strptime` from your import `datetime`: try calling it like this
`datetime.datetime.strptime()`
- `strptime` stands for something like: string parse time, meaning it takes a string, and 
parses this into a datetime from a format that you'll have to specify. 
 
Give this a shot!

```python 
datetime.datetime.strptime('31 12 2020', '%d %m %Y')
```

where:  
- `%m` is the month (1-12)
- `%d` is the day (1-31)
- `%Y` is the 4 digit year like 2020 our current year!
    

![](https://media.giphy.com/media/cOERGffHCIay7yS3ME/giphy.gif)

