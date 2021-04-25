from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.select import Select


chrome_path = '/Users/zhannak/PycharmProjects/webdriver/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.maximize_window()
driver.get('https://timetracker.techmahindra.com/mytime/Login.aspx#')
time.sleep(3)

email =
pas =

name = driver.find_element_by_css_selector("input[name='loginfmt']").send_keys(email)
submit =  driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
time.sleep(2)
password = driver.find_element_by_id('i0118').send_keys(pas)
passub = driver.find_element_by_id('idSIButton9').click()
time.sleep(20)
lan_id = driver.find_element_by_id("txtUser").send_keys('IY00617947')
lan_pass = driver.find_element_by_id('txtPwd').send_keys(pas)
lan_submit = driver.find_element_by_id('btnSubmit').click()

# Time tracker log in
acknowledge = driver.find_element_by_css_selector("input[id='ctl00_CPH_chkAcknow']").click()
time.sleep(2)
fil_timesheet = driver.find_element_by_id('ctl00_CPH_imgFill').click()

# In week
def monday():

    day = driver.find_element_by_css_selector('span[id="lblDay0"]')
    day.click()
    time.sleep(1)
    pay_code = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay0_ctl02_ddlPayCodeType']"))
    pay_code.select_by_visible_text("Regular Time")
    time.sleep(1)
    project_nonproject = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay0_ctl02_ddlPANPA']"))
    project_nonproject.select_by_visible_text('Project')
    time.sleep(1)
    project = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay0_ctl02_ddlProject']"))
    project.select_by_visible_text('Wearables')
    time.sleep(1)
    task = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay0_ctl02_ddlPayCode']"))
    task.select_by_visible_text('ATTENDANCE-Attendance')

    in_time = driver.find_element_by_css_selector("input[id='gvTimesheetDay0_ctl02_txtSignIn']")
    in_time.send_keys("0900")
    out_time = driver.find_element_by_xpath("//input[@id='gvTimesheetDay0_ctl02_txtSignOut']")
    out_time.send_keys("1700")
    meal_break = Select(driver.find_element_by_css_selector("select[id='ddlMealBreak0']"))
    meal_break.select_by_visible_text('I voluntarily did not avail meal break')
    submit_day = driver.find_element_by_css_selector("a[id='lnkSubmit0']")
    submit_day.click()

def tuesday():

    day = driver.find_element_by_css_selector('span[id="lblDay1"]')
    day.click()
    time.sleep(1)
    pay_code = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay1_ctl02_ddlPayCodeType']"))
    pay_code.select_by_visible_text("Regular Time")
    time.sleep(1)
    project_nonproject = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay1_ctl02_ddlPANPA']"))
    project_nonproject.select_by_visible_text('Project')
    time.sleep(1)
    project = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay1_ctl02_ddlProject']"))
    project.select_by_visible_text('Wearables')
    time.sleep(1)
    task = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay1_ctl02_ddlPayCode']"))
    task.select_by_visible_text('ATTENDANCE-Attendance')

    in_time = driver.find_element_by_css_selector("input[id='gvTimesheetDay1_ctl02_txtSignIn']")
    in_time.send_keys("0900")
    out_time = driver.find_element_by_xpath("//input[@id='gvTimesheetDay1_ctl02_txtSignOut']")
    out_time.send_keys("1700")
    time.sleep(1)
    meal_break = Select(driver.find_element_by_css_selector("select[id='ddlMealBreak1']"))
    meal_break.select_by_visible_text('I voluntarily did not avail meal break')
    submit_day = driver.find_element_by_css_selector("a[id='lnkSubmit0']")
    submit_day.click()
def wednesday():

    day = driver.find_element_by_css_selector('span[id="lblDay2"]')
    day.click()
    time.sleep(2)
    pay_code = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay2_ctl02_ddlPayCodeType']"))
    pay_code.select_by_visible_text("Regular Time")
    time.sleep(2)
    project_nonproject = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay2_ctl02_ddlPANPA']"))
    project_nonproject.select_by_visible_text('Project')
    time.sleep(2)
    project = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay2_ctl02_ddlProject']"))
    project.select_by_visible_text('Wearables')
    time.sleep(2)
    task = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay2_ctl02_ddlPayCode']"))
    task.select_by_visible_text('ATTENDANCE-Attendance')

    in_time = driver.find_element_by_css_selector("input[id='gvTimesheetDay2_ctl02_txtSignIn']")
    in_time.send_keys("0900")
    out_time = driver.find_element_by_xpath("//input[@id='gvTimesheetDay2_ctl02_txtSignOut']")
    out_time.send_keys("1700")
    time.sleep(1)
    meal_break = Select(driver.find_element_by_css_selector("select[id='ddlMealBreak2']"))
    meal_break.select_by_visible_text('I voluntarily did not avail meal break')
    submit_day = driver.find_element_by_css_selector("a[id='lnkSubmit0']")
    submit_day.click()

def thursday():

    day = driver.find_element_by_css_selector('span[id="lblDay3"]')
    day.click()
    time.sleep(2)
    pay_code = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay3_ctl02_ddlPayCodeType']"))
    pay_code.select_by_visible_text("Regular Time")
    time.sleep(2)
    project_nonproject = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay3_ctl02_ddlPANPA']"))
    project_nonproject.select_by_visible_text('Project')
    time.sleep(2)
    project = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay3_ctl02_ddlProject']"))
    project.select_by_visible_text('Wearables')
    time.sleep(2)
    task = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay3_ctl02_ddlPayCode']"))
    task.select_by_visible_text('ATTENDANCE-Attendance')

    in_time = driver.find_element_by_css_selector("input[id='gvTimesheetDay3_ctl02_txtSignIn']")
    in_time.send_keys("0900")
    out_time = driver.find_element_by_xpath("//input[@id='gvTimesheetDay3_ctl02_txtSignOut']")
    out_time.send_keys("1700")
    time.sleep(1)
    meal_break = Select(driver.find_element_by_css_selector("select[id='ddlMealBreak3']"))
    meal_break.select_by_visible_text('I voluntarily did not avail meal break')
    submit_day = driver.find_element_by_css_selector("a[id='lnkSubmit0']")
    submit_day.click()
def friday():

    day = driver.find_element_by_css_selector('span[id="lblDay4"]')
    day.click()
    time.sleep(2)
    pay_code = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay4_ctl02_ddlPayCodeType']"))
    pay_code.select_by_visible_text("Regular Time")
    time.sleep(2)
    project_nonproject = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay4_ctl02_ddlPANPA']"))
    project_nonproject.select_by_visible_text('Project')
    time.sleep(2)
    project = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay4_ctl02_ddlProject']"))
    project.select_by_visible_text('Wearables')
    time.sleep(2)
    task = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay4_ctl02_ddlPayCode']"))
    task.select_by_visible_text('ATTENDANCE-Attendance')

    in_time = driver.find_element_by_css_selector("input[id='gvTimesheetDay4_ctl02_txtSignIn']")
    in_time.send_keys("0900")
    out_time = driver.find_element_by_xpath("//input[@id='gvTimesheetDay4_ctl02_txtSignOut']")
    out_time.send_keys("1700")
    time.sleep(2)
    meal_break = Select(driver.find_element_by_css_selector("select[id='ddlMealBreak4']"))
    meal_break.select_by_visible_text('I voluntarily did not avail meal break')
    time.sleep(2)
    submit_day = driver.find_element_by_css_selector("a[id='lnkSubmit0']")
    submit_day.click()

def previous_week():
    driver.find_element_by_xpath("//a[@id='lnkPrevWeek']").click()

for _ in range(3):
    monday()
    tuesday()
    wednesday()
    thursday()
    friday()
    previous_week()

driver.quit()





