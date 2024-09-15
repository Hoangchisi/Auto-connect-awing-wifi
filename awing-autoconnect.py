# Import the puppeteer library
import asyncio
import time
from pyppeteer import launch

## PUPPETEER LESSON #1:
## when specify selector for elements, always put their class behind their selector
## like this button below with the selector #acceptconnection
## you have to .<class> behind the selector too, in this case it's accept-connection.wa-button.wa-button-logo

## The whole thing look like this, for example.
## <button id="acceptconnection" class="accept-connection wa-button wa-button-logo" 
##      onclick="onclickBtnConnect()" style="justify-content: center; 
##          background-color: rgb(80, 184, 72); color: rgb(255, 255, 255);">
##            TIẾP TỤC ĐỂ KẾT NỐI INTERNET
##  </button>

async def main():
    # Launch a browser instance
    browser = await launch(
        headless=False, 
        slowMo=25,
        executablePath='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    )
    # Create a new page
    page = await browser.newPage()
    # Go to the website
    await page.goto('http://v1.awingconnect.vn/login?serial=CC:2D:E0:1C:00:11&client_mac=C0:B5:D7:0C:0A:83&client_ip=186.186.14.223&userurl=http://www.msftconnecttest.com/redirect&login_url=http://rescue.wi-mesh.vn/login', ignoreHTTPSErrors=True)

    # Wait for the first button to load
    #await page.waitForSelector('#logo_button.btn.btn-primary.connect-button.w-75')
    # Click the first button
    await page.click('#logo_button.btn.btn-primary.connect-button.w-75')

    # Wait for the second webpage to load (there is no second webpage but i'll leave it here for educational purpose i think)
    # await page.waitForNavigation()

    time.sleep(3)
    # Wait for the second button to load (the second button is on the same page as the first one, just different layer)
    await page.waitForSelector('#connectToInternet.btn.btn-primary.mt-2.connect-button')
    # Click the second button
    await page.click('#connectToInternet.btn.btn-primary.mt-2.connect-button')

    # Close the browser
    await browser.close()

# Run the async function
asyncio.get_event_loop().run_until_complete(main())
