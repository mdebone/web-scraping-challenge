from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_all():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_item, news_date, news_title, news_blurb = scrape_mars_news(browser)
    image_title, full_url = scrape_mars_image(browser)
    mars_html_table, combo_html_table = scrape_mars_facts()
    hemispheres_table = scrape_mars_hemispheres(browser)

# Create Mars dictionary that is to be imported into Mongo
    mars_info_scrape = {
        'news_item': news_item,
        'news_date': news_date,
        'news_title': news_title,
        'news_blurb': news_blurb,
        'image_title': image_title,
        'full_url': full_url,
        'combo_html_table': combo_html_table(),
        'mars_html_table': mars_html_table(),
        'hemispheres_table': hemispheres_table()
    }

    # browser.quit()
    
    return mars_info_scrape

# Mars News
def scrape_mars_news(browser):

    # initalize browser
    # browser = init_browser()

    # go to Mars News site in splinter
    mars_news_url = 'https://redplanetscience.com/'
    browser.visit(mars_news_url)

    time.sleep(1)

    # HTML object
    news_html = browser.html
    
    # Parse HTML with Beautiful Soup
    soup = bs(news_html, 'html.parser')

    # retrieve the most recent news item
    news_item = soup.select_one('div', class_='list_text')

    # Retrieve the most recent news item content, date, title, blurb
    news_date = soup.find('div', class_='list_date').get_text()
    news_title = soup.find('div', class_='content_title').get_text()
    news_blurb = soup.find('div', class_='article_teaser_body').get_text()

    # browser.quit()

    return news_item, news_date, news_title, news_blurb

# Get the JPL Mars Image of the Day
def scrape_mars_image(browser): 

     # initalize browser
    # browser = init_browser()

    # JPL Mars Space Images - Featured Image in splinter
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    time.sleep(1)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    # Use Beautiful Soup's find() method to navigate and retrieve attributes
    image_title = soup.find('h1', class_='media_feature_title').get_text() 
    featured_image_url = soup.find('img', class_="headerimage")['src']

    # Get full url
    full_url = url+featured_image_url

    # browser.quit()

    return image_title, full_url

# Get Mars Facts 
def scrape_mars_facts():

     # initalize browser
    # browser = init_browser()

    # Visit Mars facts url
    mars_facts_url = "https://galaxyfacts-mars.com/"
    # browser.visit(mars_facts_url)

    time.sleep(1)

    # Use Pandas to parse the url
    table = pd.read_html(mars_facts_url)

    mars_df = table[1]

    # Create DataFrame
    mars_df.columns = ["Description", "Value", ]

    # Set index to Description
    mars_df.set_index("Description", inplace=True)

    # Save Mars html code to folder Assets
    mars_html_table = mars_df.to_html(classes= "table table-striped")

    # Now get the combo df
    combo_df = table[0]

    # Create a DataFrame
    combo_df.columns = ["Mars - Earth Comparison", "Mars", "Earth",]

    # Set index to Description
    combo_df.set_index("Mars - Earth Comparison", inplace=True)

    # Drop index first row
    combo_df = combo_df.drop(['Mars - Earth Comparison'])

    # Save Combo html code to folder Assets
    combo_html_table = combo_df.to_html(classes= "table table-striped")

    # browser.quit()

    return mars_html_table, combo_html_table

# Mars Hemispheres
def scrape_mars_hemispheres(browser):

        # initalize browser
        # browser = init_browser()

        # Use splinter to visit the Mars Hemispheres website
        hemisphere_url = "https://marshemispheres.com/"
        browser.visit(hemisphere_url)

        # HTML object
        hemisphere_html = browser.html

        # Parse HTML with Beautiful Soup
        soup = bs(hemisphere_html, 'html.parser')

        # Scrape all items that contain mars hemispheres information
        hemispheres = soup.find_all("div", class_="item")

        # Create empty list for hemisphere url
        hemispheres_table = []

        # Loop thru the Hemispheres
        for titles in hemispheres:
            title = titles.find("h3").text
            hemisphere_img = titles.find("a", class_="itemLink product-item")["href"]
        
            # Visit Link
            browser.visit(hemisphere_url + hemisphere_img)
        
            # HTML Object
            image_html = browser.html
            soup = bs(image_html, "html.parser")
        
            # Create full image url
            img_url = hemisphere_url + soup.find("img", class_="wide-image")["src"]
        
            # Append the retrieved information into a list of dictionaries
            hemispheres_table.append({"title" : title, "img_url" : img_url})

        # browser.quit()

        # Return mars_data dictionary
        return hemispheres_table

if __name__ == "__main__":
    print(scrape_all)