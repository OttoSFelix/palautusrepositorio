*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Go To Register Page
    Set Username  jokke
    Set Password  jokke123
    Set Password Confirmation  jokke123
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!


Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  jo
    Set Password  jokke123
    Set Password Confirmation  jokke123
    Click Button  Register
    Register Should Fail With Message  Username is too short
    

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  jokke123
    Set Password  jok
    Set Password Confirmation  jok
    Click Button  Register
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Go To Register Page
    Set Username  jokke123
    Set Password  jooooooo
    Set Password Confirmation  jooooooo
    Click Button  Register
    Register Should Fail With Message  Password is not good enough

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  jokke123
    Set Password  jooooooo123
    Set Password Confirmation  jooooooo124
    Click Button  Register
    Register Should Fail With Message  Password doesnt match confirmed password

Register With Username That Is Already In Use
    Go To Register Page
    Set Username  jokke
    Set Password  jooooooo123
    Set Password Confirmation  jooooooo123
    Click Button  Register
    Go To Register Page
    Set Username  jokke
    Set Password  jooooooo123
    Set Password Confirmation  jooooooo123
    Click Button  Register
    Register Should Fail With Message  Username already taken

*** Keywords ***

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
