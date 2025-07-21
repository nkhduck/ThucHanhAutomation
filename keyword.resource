*** Settings ***
Library    SeleniumLibrary
Library    Collections
Variables    locator.py

*** Variables ***
${Browser}    edge  
${url}    https://lamthaocosmetics.vn/

${fullname}     Nguyễn Kim Hoàng Đức
${email}        ducnguyen@gmail.com
${phone}        0323456789
${address}      16 Trần Kế Xương, Hải Châu, Đà Nẵng
*** Keywords ***
Open Home Page
    Open Browser    ${url}    ${Browser}
    Maximize Browser Window
    Set Selenium Speed    0.5s
Close Advertisement
    Wait Until Element Is Visible    ${close_advertisement}    timeout=10s
    Click Element    ${close_advertisement}
    
Open Product Category
    Click Element    ${product_category}    
Choose Pharmaceutical
    Click Element    ${pharmaceutical_cosmetics}
Add To Cart
    Mouse Over       ${product}
    Click Element    ${add_to_cart}
Shopping Cart
    Click Element    ${shopping_cart}
Add Quantity
    Wait Until Element Is Visible    ${add_quantity}    timeout=5s
    Click Element    ${add_quantity} 
    Sleep    1s
    Click Element    ${add_quantity}
Checkout
    Click Element    ${checkout_button}
Fill In Information
    [Arguments]    ${fullname}    ${email}    ${phone}    ${address}
    Input Text    ${input_fullname}    ${fullname}
    Input Text    ${input_email}    ${email}
    Input Text    ${input_phone}    ${phone}
    Input Text    ${input_address}    ${address}

    Click Element    ${select_province}
    Sleep    3s
    Click Element    ${select_district}
    Sleep    3s
    Click Element    ${select_ward}
    Click Element    ${next_button}
Close All Browsers Custom
    Close All Browsers










