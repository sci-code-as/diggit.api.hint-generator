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

# Added a retry-strat. here, which will retry our requests if the server 
# does not respond or throws a connection error if we perform the requests 
# too fast. 
retry_strategy = Retry(total=3, backoff_factor=1) 


main_url = 'http://35.228.245.72:80' # home of the thing... 
api_loc = '{}/Exercise'.format(main_url)

connection_check = requests.post('{}/'.format(main_url)).status_code == 200

    
    
def get_exercise(part=0):
    """
    Request exercise by part. 
    Call this function with an integer 
    """
    params = {'part':part}
    exercise_text = eval(requests.get(api_loc, params = params).content.decode('utf-8')) 
    return exercise_text
    


        
def test_my_answer(part=0,filename='<enter-filename>.py'):
    """
    Provide us with an integer indicating how far you have gotten, and we can 
    test and provide hints towards correcting any mistakes you may have made. 
    """
    with open(filename) as f:
        answer = f.read()
        
    params = {'part':part,
              'answer': answer,
              'w_test':True}
    try:
        if filename[-3:] == '.py':
            exec('from %s import *'% filename[:-3])
        else: 
            exec('from %s import *'% filename)
            
    except SyntaxError:
        print(f'Your code has a syntax error that will not allow us to check it:\n{sys.exc_info()[1]}')
        return 
    
    except NameError:
        print(f'Your code stopped on an error due to undefined name:\n{sys.exc_info()[1]}')
    except: 
        print(f'Your code exited with the following error message:\n{sys.exc_info()[1]}')
        
    #session start here ?
    adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    
    response = eval(session.get(api_loc, params = params).content.decode('utf-8'))


    return response
    
    
    
    
def write_readme(content):
    with open('exercise_readme.md','w') as f: 
        for el in content: 
            f.write(el)
    
if __name__ == '__main__':
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

