
# date: 2020.07.05
# https://stackoverflow.com/questions/62735837/simulating-http-post-request-using-requests-module-is-not-working

import requests

data = {
    'TERM': '202070',
    'TERM_DESC': 'Fall 2020',
    'sel_subj': ['dummy', '%'],
    'sel_day': 'dummy',
    'sel_schd': ['dummy', '%'],
    'sel_camp': ['dummy', '%'],
    'sel_ism': ['dummy', '%'],
    'sel_sess': ['dummy', '%'],
    'sel_instr': ['dummy', '%'],
    'sel_ptrm': ['dummy', '%'],
    'sel_attrib': ['dummy', '%'],
    
    'sel_crse': '',
    'sel_crn': '',
    'sel_title': '',
    
    'begin_hh': '5',
    'begin_mi': '0',
    'begin_ap': 'a',
    'end_hh': '11',
    'end_mi': '0',
    'end_ap': 'p',
    'aa': 'N',
    'bb': 'N',
    'ee': 'N',
}

URL = 'https://selfservice.pasadena.edu/prod/pw_psearch_sched.p_listthislist'
r = requests.post(URL, data=data)
print(r.request.body)
print(r.status_code)
#print(r.text)


