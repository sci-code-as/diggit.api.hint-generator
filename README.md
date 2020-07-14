# Introduction: 

Welcome to the practice problem part where you will be presented two entry-level tasks in making python-program. 

## Requirements: 

#### 1) Code editor:
1. If you have a code editor - use the one you have.
2. If you don’t - download & setup Visual Studio Code via: [code.visualstudio.com/download](https://code.visualstudio.com/download) 

#### 2) Python 3:
1. If you already have Python installed - Congrats! You do not need to go thought the next step. 
2. If you don’t, please follow the following:  

- For Mac:  [opensource.com](https://opensource.com/article/19/5/python-3-default-mac) (Navigate to “What we should do” section).
- For Windows:  [howtogeek.com](https://www.howtogeek.com/197947/how-to-install-python-on-windows/) (Navigate to “How to Install Python 3” section)

3.You may need to install the `requests`-package to run the request script, which 
can be done by executing `pip install requests`. ( or visit this [pypi.org/project/requests](https://pypi.org/project/requests/))

 
#### 3) Loom:
1. Download & setup Loom application for desktop: [loom.com/desktop](https://www.loom.com/desktop) 
2. Test video recording with the correct the following settings:
- No sound & no face camera
- Select Window to be recorded 
- Select App - Visual Studio (or the code editor that you use)

## Usage of `req_script`  (put this info when it is needed): 

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
This will create the file `exercise.md` which you can view with any markdown-viewer, 
e.g. in VS-Code using the "preview". 
 
## Getting Hints: 
If you need a hint, or feel you've reached the solution you should run 
```
$> python3 req_script.py test 0 <your_file>
```

After this the `exercise.md` will be updated with feedback on your current 
program, and give you some hints as to what you should do further. 

There's two portions (0 and 1) to this exercise, where portion 1 is 
about writing the evaluation portion of the code. 


# VS-Code using Preview-function (demo): 
VSCode open in repo-directory for this demo: 
<p align="center">
  <img src="./.github/VS_code.gif" alt="Contribution Guide">
</p>


## Other notes: 
- currently the feedback is aiming you towards a specific way of doing this, 
and will not be running unit-tests on you. 
- check back here in a bit to see an updated version 
