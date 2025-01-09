from playwright.async_api import async_playwright

async def fetch_url(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_selector('div#exchange-rates table.with-border tbody')

        # Get fullpage screenshot for reference
        screenshot = await page.screenshot(full_page=True)

        # get html content of page also for reference
        html_content = await page.content()
        
        table_body = await page.query_selector('div#exchange-rates table.with-border tbody')
        rows = await table_body.query_selector_all('tr')
        
        data = []
        for row in rows:
            cells = await row.query_selector_all('th, td')
            row_data = [await cell.inner_text() for cell in cells]
            data.append(row_data)
        
        await browser.close()
        
    return data, html_content, screenshot


