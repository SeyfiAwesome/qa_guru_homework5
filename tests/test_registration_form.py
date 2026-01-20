import os
from selene import browser, have


def remove_banners():
    browser.driver.execute_script("""
        const fixedBan = document.getElementById('fixedban');
        if (fixedBan) fixedBan.remove();

        const footer = document.querySelector('footer');
        if (footer) footer.remove();
    """)


def test_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')
    remove_banners()

    browser.element('#firstName').type('Seyfi')
    browser.element('#lastName').type('Ismailov')

    browser.element('#userEmail').type('seyfiismailov@gmail.com')

    browser.element('label[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('9219212121')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1993"]').click()
    browser.element('[aria-label="Choose Saturday, August 21st, 1993"]').click()

    browser.element('#subjectsInput').type('E')
    browser.element('#react-select-2-option-0').click()
    browser.element('#subjectsInput').type('A')
    browser.element('#react-select-2-option-2').click()

    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../attachments/test.png'
            )
        )
    )

    browser.element('#currentAddress').type("Saint-Petersburg, Aptekarskaya street, 5")

    browser.element('#state').click()
    browser.all('div[id^=react-select-3-option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('div[id^="react-select-4-option"]').element_by(have.exact_text("Delhi")).click()

    browser.element('#submit').click()

    results = browser.element('.table-responsive')
    results.should(have.text('Seyfi Ismailov'))
    results.should(have.text('seyfiismailov@gmail.com'))
    results.should(have.text('Male'))
    results.should(have.text('9219212121'))
    results.should(have.text('21 August,1993'))
    results.should(have.text('English, Arts'))
    results.should(have.text('Sports, Reading, Music'))
    results.should(have.text('test.png'))
    results.should(have.text('Saint-Petersburg, Aptekarskaya street, 5'))
    results.should(have.text('NCR Delhi'))

    browser.element('#closeLargeModal').click()
