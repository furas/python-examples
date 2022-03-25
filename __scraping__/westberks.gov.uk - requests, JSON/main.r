# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.11
# [r - How to correctly identify html node - Stack Overflow](https://stackoverflow.com/questions/71425295/how-to-correctly-identify-html-node/71426345#71426345)

> install.packages("rvest")
> install.packages("jsonlite")  

> library(rvest)    # it adds also `%>%`
> library(jsonlite)  

> data <- "https://www.surfdeal.ch/produkt/2019-aqua-marina-fusion-orange/" %>%
  read_html() %>%
  html_nodes('form.variations_form.cart') %>%
  html_attr('data-product_variations') %>%
  fromJSON
  
> data$display_price

[1] 479 375 439 479 479

> data$display_regular_price    

[1] 699 549 629 699 699

> data$image$title

[1] "aqua marina fusion bamboo padddel"   
[2] "aqua marina fusion aluminium padddel"
[3] "aqua marina fusion carbon padddel"   
[4] "aqua marina fusion hibi padddel"     
[5] "aqua marina fusion silver padddel"  

>  colnames(data)

 [1] "attributes"            "availability_html"     "backorders_allowed"   
 [4] "dimensions"            "dimensions_html"       "display_price"        
 [7] "display_regular_price" "image"                 "image_id"             
[10] "is_downloadable"       "is_in_stock"           "is_purchasable"       
[13] "is_sold_individually"  "is_virtual"            "max_qty"              
[16] "min_qty"               "price_html"            "sku"                  
[19] "variation_description" "variation_id"          "variation_is_active"  
[22] "variation_is_visible"  "weight"                "weight_html"          
[25] "is_bookable"           "number_of_dates"       "your_discount"        
[28] "gtin" 
