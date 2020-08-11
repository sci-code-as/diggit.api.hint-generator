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
from contextlib import redirect_stderr #for testing 
import unittest
from unittest.mock import patch
from io import StringIO
import importlib #for reload of imports...


# Added a retry-strat. here, which will retry our requests if the server 
# does not respond or throws a connection error if we perform the requests 
# too fast. 
retry_strategy = Retry(total=3, backoff_factor=1) 


main_url = 'https://hint-service-ccoonwiv5q-lz.a.run.app' # home of the thing... local-alt:#'http://0.0.0.0:80'#
api_loc = '{}/chosen_exercise'.format(main_url)

connection_check = requests.post('{}/'.format(main_url)).status_code == 200

#print('connected?',connection_check)
    
def get_exercise(name:str=''):
    """
    Request exercise by part. 
    Call this function with an integer 
    """
    params = {'name':name}
    print(f'params:{params}')
    
    response = requests.get(api_loc, params = params).json()#('utf-8'))
    #print('returns...',type(response),response)
    exercise_text = response['content']
    unit_test = response['unit_test']
    print(exercise_text)
    return exercise_text,unit_test
    
def get_exercises():
    """
    Retrieve available exercises as list. 
    """
    ex_list = eval(requests.get(main_url+'/').content.decode('utf-8'))['available']
    return ex_list
    


        
def test_my_answer(filename=None,tests = ''):
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
    error = False
    try:
        print('\n::: Running Your Code :::\nPro-tip: if your code seems stuck in an infinite loop use ctrl+c to cancel it.\n\n' )
        #only works once ? - can't get reload(module/function) to work elegantly
        
        
        #print('::: Running unit-tests on code :::')
        
        
        
        #exec(f'{tests}') #adds the test(s)
        #print(answer + '\n' + tests)
        
        try:
            #exec(f'{tests}')
            exec(answer + tests, locals())
            suite = unittest.TestSuite()
            
            suite.addTests(unittest.makeSuite(eval('Exercise_Test')))
            #print('locals.',locals().keys())
            #print('globals',globals().keys())
            dummy_io = StringIO() #captures log from io so that it does not print to user.
            with redirect_stderr(dummy_io):
                runner = unittest.TextTestRunner(verbosity=0)
            result = runner.run(suite)
            
            passed_tests = result.wasSuccessful()
            
        except NameError: 
            print('Check the names...' )
            passed_tests= False
        except: 
            passed_tests = False
    except SyntaxError:
        print(f'Your code has a syntax error that will not allow us to check it:\n{sys.exc_info()[1]}') 
        error = True
    except NameError:
        print(f'Your code stopped on an error due to undefined name:\n{sys.exc_info()[1]}')
        error = True
    except: 
        print(f'Your code exited with the following error message:\n{sys.exc_info()[1]}')
        error = True
       
    #session start here ?
    if passed_tests or error: 
        params['w_test'] = False
        adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()  
        response = session.get(api_loc, params = params).json()
        text = response['content'] + '\n\n### Your code has successfully passed all unit tests, Congratulations!' if passed_tests else ''
    else: 
        adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()  
        response = session.get(api_loc, params = params).json()
        text = response['content']       
    return text
    
    
    
    
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
        self.test = '' # will be part of eval. 
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
            self.running=False
            
            
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
        
        content, test = get_exercise(name_)
        write_readme(content)
        self.test = test
        
        self.exercise_prompt = f"The exercise-text for '{name_}' has been written/updated to the 'exercise.md'- file, check your progress from there."
        return [line, f"Exercise {name_}:\nStart by creating the file '{name_}'\n", line, self.exercise_prompt, d_line, command_request, _com_out]
        
    def get_hint(self,target_file):
        # First run the tests. 
        try: 
            write_readme(test_my_answer(target_file, self.test))
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
    
    

