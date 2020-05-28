#!/usr/bin/env python3

# date: 2020.05.28
# 

from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# --- functions ---

def get_data(start_date, end_date, product):
    
    # select `Variation Report`
    driver.find_element_by_id('ctl00_MainContent_Rbl_Rpt_type_1').click()
    
    # select `Daily Variant`
    element_variation = driver.find_element_by_id ('ctl00_MainContent_Ddl_Rpt_Option1')
    drop_variation = Select(element_variation)
    drop_variation.select_by_visible_text('Daily Variation')

    # select `product` before `date` because `end_date` opens calendar which blocks `product` list
    element_commodity = driver.find_element_by_id ('ctl00_MainContent_Lst_Commodity')
    drop_commodity = Select(element_commodity)
    drop_commodity.select_by_visible_text(product)

    # select `start_date` and `end_date`    
    driver.find_element_by_id('ctl00_MainContent_Txt_FrmDate').send_keys(start_date)
    driver.find_element_by_id('ctl00_MainContent_Txt_ToDate').send_keys(end_date)
    
    # click button `Get Data`
    driver.find_element_by_id('ctl00_MainContent_btn_getdata1').click()

    time.sleep(3)  # sometimes it need to wait for loading page
    
    #second table is the one that we want    
    table = pd.read_html(driver.page_source)[2]

    print(len(table))
    print(table)
    
    # go back
    driver.find_element_by_id('btn_back').click()

    time.sleep(3)  # sometimes it need to wait for loading page

    return table

# --- main ---

driver = webdriver.Firefox()

driver.get('https://fcainfoweb.nic.in/Reports/Report_Menu_Web.aspx')

start_date = '01/05/2020'
end_date   = '27/05/2020'

for number, product in enumerate( ('Rice', 'Wheat', 'Tomato', 'Sugar') ):
    table = get_data(start_date, end_date, product)
    # for first product create file, for other products append to existing file
    if number == 0:
        mode = 'w'
    else:
        mode = 'a'
    # standard engine `xlsxwriter` can't append so I had to use `openpyxl`
    with pd.ExcelWriter('output.xlsx', engine='openpyxl', mode=mode) as writer:
        table.to_excel(writer, sheet_name=product, index=False)

