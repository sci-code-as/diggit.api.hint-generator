# Introduction: 

Welcome to this short exercise in making a python-program. 

We'll make something pretty basic here, but it's a good exercise to try. 
## Requirements: 
You'll need to have Python 3.X installed and be able to run programs from the 
terminal/command prompt. 
 
This is tested on linux, but should work on a windows-command prompt as well. 

You may need to install the `requests`-package to run the request script, which 
can be done by executing `pip install requests`. ( or visit this [site](https://pypi.org/project/requests/))

## Usage of `req_script` : 

You'll be pulling the `req_script.py` from this repo, which is going to 
pull and create a file called `exercise.md` for you. This file you can view in 
preview (on VS-code) and this will be the medium for the exercise text as well 
as the feedback generated based on your program. 
 
## Getting started: 
To get started make a directory, put the script in there and execute 
```
$> python3 req_script.py get 0
```
The script should then pull the first (0'th) portion of the exercise for you. 
If you need a hint, or feel you've reached the solution you should run 
```
$> python3 req_script.py test 0 <your_file>
```

After this the `exercise.md` will be updated with feedback on your current 
program, and give you some hints as to what you should do further. 

There's two portions (0 and 1) to this exercise, where portion 1 is 
about writing the evaluation portion of the code. 

## Other notes: 
- currently the feedback is aiming you towards a specific way of doing this, 
and will not be running unit-tests on you. 
- check back here in a bit to see an updated version 