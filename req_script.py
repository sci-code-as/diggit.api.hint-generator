#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
"""
Request Support: 
    
Script to perform request to a server, and print what comes back. 
"""
import requests, json 
import sys
from requests.packages.urllib3.util.retry import Retry
from functools import reduce
import time
# Added a retry-strat. here, which will retry our requests if the server 
# does not respond or throws a connection error if we perform the requests 
# too fast. 
retry_strategy = Retry(total=3, backoff_factor=1) 


main_url = 'http://0.0.0.0:80'#'https://hint-service-ccoonwiv5q-lz.a.run.app' # home of the thing... 
api_loc = '{}/chosen_exercise'.format(main_url)

connection_check = requests.post('{}/'.format(main_url)).status_code == 200

    
    
def get_exercise(name:str=''):
    """
    Request exercise by part. 
    Call this function with an integer 
    """
    params = {'name':name}
    print(f'params:{params}')
    exercise_text = eval(requests.get(api_loc, params = params).content.decode('utf-8')) 
    return exercise_text
    
def get_exercises():
    """
    Retrieve available exercises as list. 
    """
    ex_list = eval(requests.get(main_url+'/').content.decode('utf-8'))['available']
    return ex_list
    


        
def test_my_answer(filename=None):
    """
    Provide us with an integer indicating how far you have gotten, and we can 
    test and provide hints towards correcting any mistakes you may have made. 
    """
    if not filename: 
        print("... something wrong with the filename...")
        raise NameError
    with open(filename) as f:
        answer = f.read()
        
    params = {'name':filename,
              'answer': answer,
              'w_test':True}
    """
    try:
        if filename[-3:] == '.py':
            exec('from %s import *'% filename[:-3])
        else: 
            exec('from %s import *'% filename)
            
    except SyntaxError:
        print(f'Your code has a syntax error that will not allow us to check it:\n{sys.exc_info()[1]}')
    
    except NameError:
        print(f'Your code stopped on an error due to undefined name:\n{sys.exc_info()[1]}')
    except: 
        print(f'Your code exited with the following error message:\n{sys.exc_info()[1]}')
     """   
    #session start here ?

    adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    
    response = eval(session.get(api_loc, params = params).content.decode('utf-8'))

    return response
    
    
    
    
def write_readme(content):
    with open('exercise.md','w') as f: 
        for el in content: 
            f.write(el)
            
            
            
#%% Experimental Repl. 
from time import sleep
class REPL(): 
    """
    start up a repl for navigation etc. etc. 
    """
    #TODO: 1. load, and display, available exercises. 
    #TODO: 2. pretty print (ish). 
    #TODO: 3. include printout to indicate basic howto. 
    #TODO: 4. hint requests 
    def __init__(self): 
        
        self.width = 80
        # exercises need to load, via method.
                        # [['1','first exercise <name_of_file_1>'], 
                        #  ['2','second exercise <name_of_file_2>']]
        
        exercise_list = get_exercises()
        self.exercises = [[i,ex] for i,ex in zip(range(len(exercise_list)),exercise_list)]
        print(self.exercises)
        # then we can set up what's current (this should be done dynamically maybe?)
        self.current = self.splash_home()
        
        self.run()
        
    def run(self):
        # Run commands. 
        self.running = True
        while self.running: 
            for line in self.current: 
                sys.stdout.write(line +'\n')
            sys.stdout.flush()
            new_command = self.prompt()
            try: 
                #print('trying to execute via setattr:',f'setattr(self,{self.commands[new_command]})' )
                try: 
                    new_command = int(new_command)
                except: 
                    pass
                if isinstance(new_command, int): 
                    print(f'Chosen exercise {new_command}')
                    self.current= self.exercise_splash(new_command)
                print(f"Executing command '{self.commands[new_command][1]}'")
                eval(f'{self.commands[new_command][0]}')
                
            except TypeError: 
                print('some type error...')
                print(f'running plain...{self.commands[new_command].split(",")[1]}')
                eval(self.commands[new_command].split(',')[1])
            except KeyError: 
                print(f'command not recognized, please use {self.commands.keys()}')
                continue
            except NameError: 
                print("Command Failed, exiting....")
                self.running = False
                continue
            except IndexError:
                print('Exercise Index out of range, check list of available exercises.')
            
    
            
            
    def splash_home(self):
        # Get size of cl ? or default to [100]... 
        self.commands= {'q': ["setattr(self,'running', False)","quit CLI"],
                        'number': ["self.exercise_splash(number)","chosen exercise"],
                        'h': ["setattr('current',self.splash_home())","return to [h]ome"]}
        width = self.width# 100 # or change this. 
        line = '-'*width 
        d_line = '='*width

        title= 'Welcome to the Sci-Code Hint system! '
        content= "Please select an exercise from the list below:"
        command_request = "Available commands:"
        _exercises = [str(ex[0])+' - '+ex[1] for ex in self.exercises]
        _ex_out = reduce(lambda x,y: x + '\n' + y, _exercises)
        _commands = [str(key) + ' - ' + val[1] for key,val in self.commands.items()]
        _com_out = reduce(lambda x,y: x + '\n' + y, _commands)
        build_order = [line, title, line, content, line, _ex_out, d_line, command_request, _com_out]
        return build_order
        
    def exercise_splash(self,exercise_no):
        #self.current = self.exercise_splash()
        name_ = self.exercises[exercise_no][1]
        
        width = self.width# 100 # or change this. 
        line = '-'*width 
        d_line = '='*width
        self.commands= {'q': ["setattr(self,'running', False)","quit CLI"],
                        'hint': [f"self.get_hint('{name_}')","get hints."],
                        'h': ["setattr(self,'current',self.splash_home())","return to home"]}
        command_request = "Available commands:"
        _commands = [str(key) + ' - ' + val[1] for key,val in self.commands.items()]
        _com_out = reduce(lambda x,y: x + '\n' + y, _commands)
        write_readme(get_exercise(name_))
        self.exercise_prompt = f"The exercise-text for '{name_}' has been written/updated to the 'exercise.md'- file, check your progress from there."
        return [line, f"Exercise {name_}:\nStart by creating the file '{name_}'\n", line, self.exercise_prompt, d_line, command_request, _com_out]
        
    def get_hint(self,target_file):
        try: 
            write_readme(test_my_answer(target_file))
        except FileNotFoundError: 
            print(f'\nERROR:\nYou first need to create the file {target_file} to start requesting hints for this exercise')
        
        
    def load_conf(self): 
        
        pass
    
    def save_conf(self): 
        pass
    
    #def percentage_completed(self, exercise_no): 
    #    default = '['+ 20*' '+ ']'
    
    
        
    def prompt(self): 
        _user_input = input('$ > ')
        if _user_input=='':
            sys.stdout.write('\r no command written')
            sleep(0.5)
            return self.prompt()
        return _user_input
        
        
#%%     
    
if __name__ == '__main__':
    
    test = REPL()
    run_mode = sys.argv
    
    i = 0
    test_flag = 'test' in run_mode
    get_next = 'get' in run_mode
    
    if get_next: 
        ind = run_mode.index('get')
        i = int(run_mode[ind+1])
        write_readme(get_exercise(i))
    elif test_flag: 
        ind = run_mode.index('test')
        i = int(run_mode[ind+1])
        target_file = run_mode[ind+2]
        if 'target_file' in locals():
            write_readme(test_my_answer(i, target_file))
        else:
            write_readme(test_my_answer(i,target_file))

