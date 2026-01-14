import time
from selene import browser, have


def test_registration_form():
    browser.config.timeout = 10

    # Fill "First name" and "Last name"
    browser.element('#firstName').type('Seyfi')
    browser.element('#lastName').type('Ismailov')

    # Fill "email" field
    browser.element('#userEmail').type('seyfiismailov@gmail.com')

    # Check "Gender" radiobttn
    browser.element('label[for="gender-radio-1"]').click()

    # Fill "Number" field
    browser.element('#userNumber').type('9219212121')

    # Fill "Date of birth"
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1993"]').click()
    browser.element('[aria-label="Choose Saturday, August 21st, 1993"]').click()

    # Choose "Subjects" options (English + Arts)
    browser.element('#subjectsInput').type('E')
    browser.element('#react-select-2-option-0').click()
    browser.element('#subjectsInput').type('A')
    browser.element('#react-select-2-option-2').click()

    # Choose all check-box for "Hobbies" block
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()

    # Uploading the file to the "Picture" block
    browser.element('#uploadPicture').send_keys('attachments/test.png')

    # Fill the "Current Address" field
    browser.element('#currentAddress').type("Saint-Petersburg, Aptekarskaya street, 5")

    # Selecting State and City
    browser.element('#state').click()
    browser.all('div[id^=react-select-3-option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('div[id^="react-select-4-option"]').element_by(have.exact_text("Delhi")).click()
    time.sleep(5)

    # Click on Submit bttn
    browser.element('#submit').click()
    time.sleep(2)

    # Close the pop-up
    browser.element('#closeLargeModal').click()
    time.sleep(5)
