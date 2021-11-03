
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.03
#
# title: How to get data with websocket in a class and instantiate variable
# url: https://stackoverflow.com/questions/69817003/how-to-get-data-with-websocket-in-a-class-and-instantiate-variable/69824728#69824728

# [How to get data with websocket in a class and instantiate variable](https://stackoverflow.com/questions/69817003/how-to-get-data-with-websocket-in-a-class-and-instantiate-variable/69824728#69824728)

import websocket
import json

class WS:

    def __init__(self):
        self.socket = 'wss://ftx.com/ws/'
        self.close = None # default value at start

    def stream(self):
        self.ws = websocket.WebSocketApp(
                    self.socket,
                    on_message=self.on_message,
                    on_error=self.on_error,
                    on_close=self.on_close,
                    on_open=self.on_open
                  )

        print('run forever')
        self.ws.run_forever()
        
    def on_open(self, ws):
        print('on_open:', ws)

        data = {'op': 'subscribe', 'channel': 'ticker', 'market': 'ETH-PERP'}
        
        self.ws.send(json.dumps(data))

    def on_close(self, ws):
        print('on_close:', ws)

    def on_message(self, ws, message):
        print('on_message:', ws, message)
        
        data = json.loads(message)

        if data['type'] == 'update':
            self.close = data['data']['last']

    def get_data_out(self):
        return self.close
   
    def on_error(self, ws, error):
        print('on_error:', ws, error)
        
# --- main ---

websocket.enableTrace(True)  # if you want to see more information  
                             # but code works also without this line

WS().stream()


