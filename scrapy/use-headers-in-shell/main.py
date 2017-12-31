
url = 'http://www.ikea.com/ae/en/catalog/categories/departments/childrens_ikea/31772/'

fetch(request.url, headers={'User-Agent': 'Mozilla/5.0'})

view(response)

response.css('div.productTitle.floatLeft')
