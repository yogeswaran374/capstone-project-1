class Inputs:
    #url, username and password for login page
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    incorrect_password = "admin"

    #personnal details and new employee details
    firstname = "yoges1"
    middlename = "1"
    lastname = "0"

    otherid = "500"

    #editing the employee details
    updated_other_id = "12345"

class Selectors:
    #loginpage selectors
    textbox_username_xpath = '//input[@name="username"]'
    textbox_password_xpath = '//input[@name="password"]'
    button_login_xpath = '//button[@type="submit"]'
    profile_icon = "//p[@class='oxd-userdropdown-name']"
    logout = "Logout"

    #add new employee details & personnal details selectors
    PIM_icon_abs_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    Add_button_xpath = '//i[@class="oxd-icon bi-plus oxd-button-icon"]'
    text_box_firstname_xpath = '//input[@name="firstName"]'
    text_box_middlename_xpath = '//input[@name="middleName"]'
    text_box_lastname_xpath = '//input[@name="lastName"]'
    save_button_xpath = '//button[@type="submit"]'

    text_box_other_id_absxpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    gender_radio_button_absxpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    save_personal_details_button_abs_xpath = 'html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/form/div[4]/button'
    lable_element = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6'

    #edit personnal details in PIM module selectors
    textbox_emp_name_absxpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    search_button_absxpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    Edit_icon_absxpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i'
    update_otherid_save_button_absxpath = 'html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/form/div[4]/button'

    #delete personal details selectors
    delete_existing_emp_details_absxpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i'
    popup_yes_button_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'
    records = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'