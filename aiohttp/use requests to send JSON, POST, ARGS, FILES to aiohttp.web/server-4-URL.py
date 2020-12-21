
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

    return web.Response(text='Received...')

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
