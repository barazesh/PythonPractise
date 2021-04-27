import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS


def main():
    starttime = time.time()
    # desiredDate = date(2013, 11, 8)
    # getDay(desiredDate)

    getYear(1392)
    print(f'Execution time in seconds: {time.time()-starttime}')


def getYear(year):
    driver = webdriver.Firefox()
    driver.get("http://www.time.ir/fa/eventyear")
    year_selector = driver.find_element_by_id(
        'ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_txtYear')
    year_selector.clear()
    year_selector.send_keys(str(year))
    driver.find_element_by_id(
        'ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_btnGo').click()
    page = driver.page_source
    soup=BS(page,'lxml')
    months = soup.select('#ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_pnlYearCalendar .panel.panel-body')
    monthCounter = 0
    for m in months:
        monthCounter += 1
        print('************')
        print(f'month: {monthCounter}')
        days = m.select('.eventCalendar .mainCalendar .dayList > div')
        print('###')
        for d in days:
            isDisabled='disabled' in d.attrs['class']
            if 'disabled' not in d.attrs['class']:
                if d.select('.holiday'):
                    print('*Holiday*')
                jalali=d.select('.jalali')[0].string
                miladi=d.select('.miladi')[0].string
                qamari=d.select('.qamari')[0].string
                print(f'Jalali: {jalali} -- Miladi: {miladi} -- Qamari: {qamari}')
                print('-----------------')


def getDay(inputDate):
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("http://www.time.ir")
    convert = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_ddlSelectConvertType"))
    ))
    convert.select_by_value("0")
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.dateConvertFirstDate > h5'), "میلادی:"))

    select_day = Select(driver.find_element_by_id(
        'ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_ddlDay'))
    select_day.select_by_value(str(inputDate.day))
    select_month = Select(driver.find_element_by_id(
        'ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_ddlMonth'))
    select_month.select_by_value(str(inputDate.month))
    select_year = driver.find_element_by_id(
        'ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_txtYear')
    select_year.clear()
    select_year.send_keys(str(inputDate.year))
    driver.find_element_by_id(
        'ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_btnConvert').click()

    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
        (By.ID, 'ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_lblFirstDateNumeral'), inputDate.isoformat()))
    miladi = driver.find_element_by_id(
        'ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_lblFirstDateNumeral').text
    shamsi = driver.find_element_by_id(
        'ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_lblSecondDateNumeral').text
    qamary = driver.find_element_by_id(
        'ctl00_cphMiddle_Sampa_Web_View_TimeUI_DateConvert00cphMiddle_3733_lblThirdDateNumeral').text
    print(miladi)
    print(shamsi)
    print(qamary)


if __name__ == '__main__':
    main()
