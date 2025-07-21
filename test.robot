*** Settings ***
Library    SeleniumLibrary
Resource   keyword.resource
Variables    locator.py

Suite Setup       Open Home Page
Suite Teardown    Close All Browsers Custom

*** Variables ***
${url}    https://lamthaocosmetics.vn/
${Browser}        edge

${fullname}      Nguyễn Kim Hoàng Đức
${email}         ducnguyen@gmail.com
${phone}         0323456789
${address}       16 Trần Kế Xương, Hải Châu, Đà Nẵng
*** Test Cases ***
Test Checkout Process
    Open Home Page
    Close Advertisement
    Open Product Category
    Choose Pharmaceutical
    Add To Cart
    Shopping Cart
    Add Quantity
    Checkout
    Fill In Information    ${fullname}    ${email}    ${phone}    ${address}
    Close All Browsers Custom



*** Keywords ***

