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


*** Test Cases ***
Success Login
    open page
    Success Login

Failed Login invalid username
    open page
    Failed Login invalid username

Failed Login invalid password
    open page
    Failed Login invalid password

Failed Login invalid username and password
    open page
    Failed Login invalid username and password


*** Keywords ***
open page
    Open Browser    ${Url}    Chrome

Success Login
    Input Text    id=user-name    ${name}
    Input Text    id=password    ${pass}
    Click Element    id=login-button
    Close Browser

Failed Login invalid username
    Input Text    id=user-name    ${invalid_name}
    Input Text    id=password    ${pass}
    Click Element    id=login-button
    Close Browser

Failed Login invalid password
    Input Text    id=user-name    ${name}
    Input Text    id=password    ${invalid_pass}
    Click Element    id=login-button
    Close Browser

Failed Login invalid username and password
    Input Text    id=user-name    ${invalid_name}
    Input Text    id=password    ${invalid_pass}
    Click Element    id=login-button
    Close Browser
