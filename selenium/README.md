
See also

- [beautifulsoup](../beautifulsoup)
- [requests](../requests)
- [scrapy](../scrapy)
- [selenium](../selenium)
- [`__scraping__`](../__scraping__)

---

Wait:

- [selenium-python.readthedocs.io/waits](http://selenium-python.readthedocs.io/waits.html)

Resize:

- [How do I resize the window in Chrome and Firefox when testing with Selenium?](https://stackoverflow.com/a/29600557/1832058)

    # Chrome

    chrome_options.add_argument("--window-size=1920x1080")

    # all browsers


    driver.set_window_size(1920, 1080)

    # or

    driver.maximize_window()

    # or with javascript (doesn't work for me

    driver.execute_script("window.resizeTo(1920,1080)")


Scroll:

- [How can I scroll a web page using selenium webdriver in python?](https://stackoverflow.com/questions/29600093/how-do-i-resize-the-window-in-chrome-and-firefox-when-testing-with-selenium)


    driver.execute_script("window.scrollTo(0, Y)")

    # ---
    
    while driver.find_element_by_tag_name('div'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        divs = driver.find_element_by_tag_name('div').text
        if 'End of Results' in Divs:
            print 'end'
            break

    # ---
    
    element = find_element_by_xpath("xpath of the li you are trying to access")

    element.location_once_scrolled_into_view

    # ---
    
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
            
        last_height = new_height    
        
    # ---
    
    page.driver.browser.mouse.move_to( find("element").native,100,100)

    # ---
    
    Actions actions = new Actions(driver);
    actions.sendKeys(Keys.BACK_SPACE).perform();    

    # ---
    
    WebDriver driver = new FirefoxDriver();
    JavascriptExecutor js = (JavascriptExecutor)driver;
    js.executeScript("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));");
    
