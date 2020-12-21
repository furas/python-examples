
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2020.12.21
# https://docs.aiohttp.org/en/stable/index.html
# https://stackoverflow.com/questions/65371754/aiohttp-web-post-method-get-params/

from aiohttp import web

routes = web.RouteTableDef()

@routes.post('/test')
async def test(request):
    print('\n--- request ---\n')

    # ----------------------------------------------------------------------

    print('ARGS string:', request.query_string)  # arguments in URL as string
    print('ARGS       :', request.query)         # arguments in URL as dictionary

    # ----------------------------------------------------------------------

    # >> it can't use at the same time: `content.read()`, `text()`, `post()`, `json()`, `multiparts()` 
    # >> because they all read from the same stream (not get from variable) 
    # >> and after first read this stream is empty

    # ----------------------------------------------------------------------

    #print('BODY bytes :', await request.content.read())  # body as bytes  (post data as bytes, json as bytes)
    #print('BODY string:', await request.text())          # body as string (post data as string, json as string)

    # ----------------------------------------------------------------------

    #print('POST       :', await request.post())         # POST data

    # ----------------------------------------------------------------------

    #try:
    #    print('JSON:', await request.json())  # json data as dictionary/list
    #except Exception as ex:
    #    print('JSON: ERROR:', ex)

    # ----------------------------------------------------------------------

    try:
        #print('MULTIPART:', await request.multipart())  # files and forms
        reader = await request.multipart()
        print('MULTIPART:', reader)
        while True:
            part = await reader.next()
            if part is None: 
                break
            print('filename:', part.filename)
            print('>>> start <<<')
            print(await part.text())
            print('>>> end <<<')
    except Exception as ex:
        print('MULTIPART: ERROR:', ex)

    # ----------------------------------------------------------------------

    return web.Response(text='Received...')

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
