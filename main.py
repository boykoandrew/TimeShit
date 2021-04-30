from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

chrome_path = '/Users/zhannak/PycharmProjects/webdriver/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.maximize_window()
driver.get('https://timetracker.techmahindra.com/mytime/Login.aspx#')
wait = WebDriverWait(driver, 10)



# login Microsoftonline.com
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Sign in']")))
name = driver.find_element_by_css_selector("input[name='loginfmt']").send_keys(email)
submit =  driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a[id='idA_PWD_ForgotPassword']")))
password = driver.find_element_by_id('i0118').send_keys(pas)

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']")))
time.sleep(1)
passub = driver.find_element_by_css_selector("input[type='submit']").click()
time.sleep(20)
lan_id = driver.find_element_by_id("txtUser").send_keys('IY00617947')
lan_pass = driver.find_element_by_id('txtPwd').send_keys(pas)
lan_submit = driver.find_element_by_id('btnSubmit').click()

# Time tracker log in
acknowledge = driver.find_element_by_css_selector("input[id='ctl00_CPH_chkAcknow']").click()
wait.until(expected_conditions.presence_of_element_located((By.ID, "ctl00_CPH_imgFill")))
fil_timesheet = driver.find_element_by_id('ctl00_CPH_imgFill').click()


# In week
def monday():


    day = driver.find_element_by_css_selector('span[id="lblDay0"]')
    day.click()
    time.sleep(1)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//select[@id='gvTimesheetDay0_ctl02_ddlPANPA']")))
    pay_code = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay0_ctl02_ddlPayCodeType']"))
    pay_code.select_by_visible_text("Regular Time")
    time.sleep(1)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//select[@id='gvTimesheetDay0_ctl02_ddlPANPA']")))
    project_nonproject = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay0_ctl02_ddlPANPA']"))
    project_nonproject.select_by_visible_text('Project')
    time.sleep(1)

    project = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay0_ctl02_ddlProject']"))
    project.select_by_visible_text('Wearables')
    time.sleep(1)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "select[id='gvTimesheetDay0_ctl02_ddlPayCode']")))
    task = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay0_ctl02_ddlPayCode']"))
    task.select_by_visible_text('ATTENDANCE-Attendance')

    in_time = driver.find_element_by_css_selector("input[id='gvTimesheetDay0_ctl02_txtSignIn']")
    in_time.send_keys("0900")
    out_time = driver.find_element_by_xpath("//input[@id='gvTimesheetDay0_ctl02_txtSignOut']")
    out_time.send_keys("1700")
    time.sleep(1)

    meal_break = Select(driver.find_element_by_css_selector("select[id='ddlMealBreak0']"))
    meal_break.select_by_visible_text('I voluntarily did not avail meal break')
    time.sleep(3)
    submit_day = driver.find_element_by_css_selector("a[id='lnkSubmit0']").click()
    time.sleep(3)

    l = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[id='lblMsgDay0']")))
    saved = driver.find_element_by_css_selector("span[id='lblMsgDay0']").text
    print(saved)



def tuesday():

    day = driver.find_element_by_css_selector('span[id="lblDay1"]')
    day.click()
    time.sleep(2)
    pay_code = Select(driver.find_element_by_css_selector("select[id='gvTimesheetDay1_ctl02_ddlPayCodeType']"))
    pay_code.select_by_visible_text("Regular Time")
    time.sleep(2)
    project_nonproject = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay1_ctl02_ddlPANPA']"))
    project_nonproject.select_by_visible_text('Project')
    time.sleep(2)
    project = Select(driver.find_element_by_xpath("//select[@id='gvTimesheetDay1_ctl02_ddlProject']"))
    project.select_by_visible_text('Wearables')
    time.sleep(2)
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
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[id='lblMsgDay1']")))
    saved = driver.find_element_by_css_selector("span[id='lblMsgDay1']").text
    print(saved)

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
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "span[id='lblMsgDay2']")))
    saved = driver.find_element_by_css_selector("span[id='lblMsgDay2']").text
    print(saved)

def thursday():

    day = driver.find_element_by_css_selector('span[id="lblDay3"]')
    day.click()
    time.sleep(1)
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
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[id='lblMsgDay3']")))
    saved = driver.find_element_by_css_selector("span[id='lblMsgDay3']").text
    print(saved)

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
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[id='lblMsgDay4']")))
    saved = driver.find_element_by_css_selector("span[id='lblMsgDay4']").text
    print(saved)


def previous_week():
    driver.find_element_by_xpath("//a[@id='lnkPrevWeek']").click()


previous_week()
monday()
tuesday()
# wednesday()
# thursday()
# friday()

# driver.quit()





