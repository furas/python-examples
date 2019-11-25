#!/usr/bin/env python3 

# date: 2019.11.24

import selenium.webdriver

driver = selenium.webdriver.Firefox()

html_content = """
    <div class=div1>
        <ul>
            <li>
                <a href='path/to/div1stuff/1'>Generic string 1</a>
                <a href='path/to/div1stuff/2'>Generic string 2</a>
                <a href='path/to/div1stuff/3'>Generic string 3</a>
            </li>
        </ul>            
    </div>

    <div class=div2>
        <ul>
            <li>
                <a href='path/to/div2stuff/1'>Generic string 1</a>
                <a href='path/to/div2stuff/2'>Generic string 2</a>
                <a href='path/to/div2stuff/3'>Generic string 3</a>
            </li>
        </ul>            
    </div>
"""

driver.get("data:text/html;charset=utf-8," + html_content)

elements = driver.find_elements_by_css_selector("div.div2 a")
for x in elements:
    print(x.get_attribute('href'))
    
item = driver.find_element_by_xpath("//div[@class='div2']//a[contains(text(),'Generic string 2')]")
print(item.get_attribute('href'))
item.click()
    
