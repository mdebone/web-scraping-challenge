from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# browser = init_browser()
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit redplanetscience.com
mars_news_url = "https://redplanetscience.com/"
# Parse HTML with Beautiful Soup
browser.visit(mars_news_url)

time.sleep(1)

# Scrape page into Soup
news_html = browser.html
soup = bs(news_html, "html.parser")

# retrieve the most recent news item
news_item = soup.select_one('div', class_='list_text')

# Retrieve the most recent news item content, date, title, blurb
news_date = soup.find('div', class_='list_date').get_text()
news_date

news_title = soup.find('div', class_='content_title').get_text()
news_title

news_blurb = soup.find('div', class_='article_teaser_body').get_text()
news_blurb

# Visit spaceimages-mars.com
mars_image_url = "https://spaceimages-mars.com/"
# Parse HTML with Beautiful Soup
browser.visit(mars_image_url)

time.sleep(1)

# Scrape page into Soup
image_html = browser.html
soup = bs(image_html, "html.parser")

# Use Beautiful Soup's find() method to navigate and retrieve attributes
image_title = soup.find('h1', class_='media_feature_title').get_text()
image_title

# Get the featured image
featured_image_url = soup.find('img', class_="headerimage")['src']

# Visit galaxyfacts-mars.com
mars_facts_url = "https://galaxyfacts-mars.com/"
# Parse HTML with Beautiful Soup
browser.visit(mars_facts_url)

time.sleep(1)

# Scrape page into Soup
facts_html = browser.html
soup = bs(facts_html, "html.parser")

# Use Beautiful Soup's find() method to navigate and retrieve attributes
facts_table = pd.read_html(facts_html)

# Get the dataframe
mars_df = facts_table[1]

# Create DataFrame
mars_df.columns = ["Description", "Value", ]

# Set index to Description
mars_df.set_index("Description", inplace=True)

# Save the Mars dataframe to html
mars_df.to_html("mars_facts_data.html")

# Print Data Frame
mars_df

# Save Mars html code to folder Assets
mars_html_table = mars_df.to_html(classes= "table table-striped")

# Get the other dataframe
combo_df = facts_table[0]

# Create a DataFrame
combo_df.columns = ["Mars - Earth Comparison", "Mars", "Earth",]

# Set index to Description
combo_df.set_index("Mars - Earth Comparison", inplace=True)

# Drop index first row
combo_df = combo_df.drop(['Mars - Earth Comparison'])

# Save html code
combo_df.to_html("earth_mars_facts_data.html")

# inspect combo dataframe
combo_df

# Save Combo html code to folder Assets
combo_html_table = combo_df.to_html(classes= "table table-striped")

# Visit marshemispheres.com
hemisphere_url = "https://marshemispheres.com/"
browser.visit(hemisphere_url)

time.sleep(1)

# HTML object
hemispher_html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(hemispher_html, 'html.parser')  
        
# Scrape all items that contain mars hemispheres information
hemispheres = soup.find_all("div", class_="item")

# Create empty list
hemispheres_table = []

# Loop thru the Hemispheres
for titles in hemispheres:
    hemisphere_title = titles.find("h3").text
    hemisphere_img = titles.find("a", class_="itemLink product-item")["href"]
        
    # Visit Link
    browser.visit(hemisphere_url + hemisphere_img)
        
    # HTML Object
    image_html = browser.html
    image_info = bs(image_html, "html.parser")
        
     # Create full image url
    img_url = hemisphere_url + image_info.find("img", class_="wide-image")["src"]
        
    # Append the retrieved information into a list of dictionaries
    hemispheres_table.append({"title" : hemisphere_title, "img_url" : img_url})

# Store data in a dictionary
# mars_data = {
#     "news_item": news_item,
#     "news_date": news_date,
#     "news_title": news_title,
#     "news_blurb": news_blurb,
#     "mage_title": image_title,
#     "featured_image_url": featured_image_url,
#     "facts_table": facts_table,
#     "hemisphere_img": hemisphere_img,
#     "hemisphere_title": hemisphere_title
# }

# Close the browser after scraping
browser.quit()



