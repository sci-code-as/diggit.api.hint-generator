# Introduction: 

Welcome to this short exercise in making a python-program. 

We'll make something pretty basic here, but it's a good exercise to try. 
## Requirements: 
You'll need to have Python 3.X installed and be able to run programs from the 
terminal/command prompt. 
 
This is tested on linux, but should work from a mac- or windows-command prompt as well. 

You may need to install the `requests`-package to run the request script, which 
can be done by executing `pip install requests`. ( or visit this [site](https://pypi.org/project/requests/))

## Usage of `req_script` : 

You'll be pulling the `req_script.py` from this repo, which is going to 
pull and create a file called `exercise.md` for you. This file you can view in 
preview (on VS-code) and this will be the medium for the exercise text as well 
as the feedback generated based on your program. 
 
## Getting started: 
To get started make a directory, clone this repo, or put the script in there and execute 
```
$> python3 req_script.py
```
You will then be taken to an overview of available exercises, with integer values for each available exercise. 
Pick the exercise you wish to do. This will create the file `exercise.md` which you can view with any markdown-viewer, 
e.g. in VS-Code using the "preview". 

Following the `exercise.md` text you'll see the name of the exercise, and the filename you should give it, along with the description of the exercise.
 
In the bottom of the exercise-text you should see a Run-Sample, which is an example of what executing the code should look like. 

## Getting Hints: 
If you need a hint, or feel you've reached the solution you can now go to the open interface with the hint-system (or if the file is closed re-run the `python3 req_script.py` and navigate to the exercise you're working on). 

In the interface you should see a list of 'Available commands', and one of these is `hint`, just enter `hint` and the script will do two things; 
- It will run your code, with whatever outputs comes from it (print-statements etc.)
- Then it will run a bundle of unit tests against your code, and if it finds your code is not quite there to pass the tests it will provide you with hints as to what you can try to do next. 

After the hints have run, the script will stop and any feedback or hints will be written in the bottom of the `exercise.md` file, underneath the Run-Sample. (So you'll always be referring back to this file.) 

# VS-Code using Preview-function (demo): 
VSCode open in repo-directory for this demo: 
<p align="center">
  <img src="./.github/VS_code.gif" alt="Contribution Guide">
</p>


## Other notes: 
- The naming of functions is specific, so make sure you follow the exercise-instructions when naming your file and your function-name (if applicable)