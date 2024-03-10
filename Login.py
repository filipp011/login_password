from selene import browser,have

browser.open('https://school.qa.guru/')
browser.element('.login-form [name=email]').type("fil.nis61@gmail.com")
browser.element('.login-form [name=password]').type("558852558852RND").press_enter()
browser.element('.page-header').should(have.text('Список тренингов'))






