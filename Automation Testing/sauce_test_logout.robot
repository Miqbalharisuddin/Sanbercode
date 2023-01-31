*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${Browser}          Chrome
${Url}              https://www.saucedemo.com/
${name}             standard_user
${invalid_name}     yanto
${pass}             secret_sauce
${invalid_pass}     yanto123
${error}            Epic sadface: Username and password do not match any user in this service


*** Test Cases ***
Logout
    open page
    Logout


*** Keywords ***
open page
    Open Browser    ${Url}    Chrome

Logout
    Input Text    id=user-name    ${name}
    Input Text    id=password    ${pass}
    Click Element    id=login-button
    Click Element    id=react-burger-menu-btn
    Click Element    id=logout_sidebar_link
    Title Should Be    Swag Labs
    Close Browser
