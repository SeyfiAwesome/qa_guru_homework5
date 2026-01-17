import os
import time
from selene import browser, have


def test_registration_form():
    browser.element('#firstName').type('Seyfi')
    browser.element('#lastName').type('Ismailov')
    time.sleep(1)

    browser.element('#userEmail').type('seyfiismailov@gmail.com')
    time.sleep(1)

    browser.element('label[for="gender-radio-1"]').click()
    time.sleep(1)

    browser.element('#userNumber').type('9219212121')
    time.sleep(1)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1993"]').click()
    browser.element('[aria-label="Choose Saturday, August 21st, 1993"]').click()
    time.sleep(1)

    browser.element('#subjectsInput').type('E')
    browser.element('#react-select-2-option-0').click()
    browser.element('#subjectsInput').type('A')
    browser.element('#react-select-2-option-2').click()
    time.sleep(1)

    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    time.sleep(1)

    browser.element('#uploadPicture').send_keys(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../attachments/test.png'
            )
        )
    )
    time.sleep(1)

    browser.element('#currentAddress').type("Saint-Petersburg, Aptekarskaya street, 5")
    time.sleep(1)

    browser.element('#state').click()
    browser.all('div[id^=react-select-3-option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('div[id^="react-select-4-option"]').element_by(have.exact_text("Delhi")).click()
    time.sleep(1)

    browser.element('#submit').click()
    time.sleep(1)

    browser.element('.table-responsive').should(have.text('Seyfi Ismailov'))
    browser.element('.table-responsive').should(have.text('seyfiismailov@gmail.com'))

    browser.element('#closeLargeModal').click()
    time.sleep(1)
