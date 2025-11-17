*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Register Username  joonas
    Set Register Password  salasana123
    Set Register Password Confirmation  salasana123
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Register Username  a
    Set Register Password  salasana123
    Set Register Password Confirmation  salasana123
    Click Button  Register
    Register Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Register Username  joonas
    Set Register Password  lyhyt1
    Set Register Password Confirmation  lyhyt1
    Click Button  Register
    Register Should Fail With Message  Password must be at least 8 characters

Register With Valid Username And Invalid Password
    Set Register Username  joonas
    Set Register Password  salasana
    Set Register Password Confirmation  salasana
    Click Button  Register
    Register Should Fail With Message  Password must contain characters other than letters

Register With Nonmatching Password And Password Confirmation
    Set Register Username  joonas
    Set Register Password  salasana123
    Set Register Password Confirmation  salasana234
    Click Button  Register
    Register Should Fail With Message  Password and confirmation are different

Register With Username That Is Already In Use
    Set Register Username  kalle
    Set Register Password  salasana123
    Set Register Password Confirmation  salasana123
    Click Button  Register
    Register Should Fail With Message  Username already exists

*** Keywords ***
Register Page Should Be Open
    Title Should Be  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Register Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Register Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Register Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}
