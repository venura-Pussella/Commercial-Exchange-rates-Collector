import asyncio
from playwright.async_api import async_playwright

url = "https://www.combank.lk/rates-tariff#exchange-rates"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:127.0) Gecko/20100101 Firefox/127.0"

async def fetch_url():
    async with async_playwright() as p:
        # Launch a new browser instance
        browser = await p.firefox.launch()
        
        # Create a new browser context with user-agent
        context = await browser.new_context(user_agent=user_agent)
        
        # Create a new page within this context
        page = await context.new_page()
        
        # Navigate to the URL
        await page.goto(url, timeout=15000)
        
        # Get the content of the page
        content = await page.content()
        
        # Close the browser
        await browser.close()
        
        return content
    

def write_to_html(content):

    with open('file.html', 'w', encoding='utf-8') as f:
        f.write(content)

    return content




# import pandas as pd
# from io import StringIO
# import os
# from datetime import datetime

# def process_html_content_to_dataframe(html_content):

#     # html_file_like = StringIO(html_content)
#     df = pd.read_html(html_content)

#     # df['Bank'] = 'Nations Trust'
#     # df['Date'] = datetime.now().strftime('%Y-%m-%d') #todays date 
#     # df['Time'] = datetime.now().strftime('%H:%M:%S') #todays time

#     # file_path = os.path.join(OUTPUT_CSV)
#     # df.to_csv(file_path, index=False)
     
#     return df

# Run the asynchronous function using asyncio.run()
if __name__ == "__main__":
    content=asyncio.run(fetch_url())
    html_file = write_to_html(content)

