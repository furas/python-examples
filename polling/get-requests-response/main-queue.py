import requests
import polling
import queue

def test(response):
    return response.status_code == 200

my_queue = queue.Queue()

result = polling.poll(lambda: requests.get('http://google.com'), 
                      step=60, 
                      poll_forever=True, 
                      check_success=test,
                      collect_value=my_queue)

if my_queue.empty():
    print('empty')
else:
    while not my_queue.empty():
        print(my_queue.get())
    
#print(result.text)
    
