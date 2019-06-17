from splinter import Browser
from bs4 import BeautifulSoup 
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit Nasa Website
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Scrape Content Title from Nasa Mars Website 
    list_item = news_soup.select_one('ul.item_list li.slide')
    news_title = list_item.find("div", class_="content_title")

    # Text from Nasa Mars Website 
    title = news_title.get_text()

    # Scrape Paragraph Text from Nasa Mars Website 
    news_para = list_item.find("div", class_="article_teaser_body")

    # Paragraph Text from Nasa Mars Website 
    paragraph = news_para.get_text()

    return title, paragraph

def scrape_img():
    browser = init_browser()

    # Path to JPL Featured Space Image URL
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_image_url)

                # Scrape Full Size JPL Featured Space Image

    # Splinter Click to click 'full image' on website 
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Delay splinter click to allow website to load in order to submit another click command
    browser.is_element_present_by_text('more info', wait_time=1)

    # Splinter Click to click 'more info' on website
    more_info = browser.find_link_by_partial_text('more info')
    more_info.click()

    # Beautiful Soup command
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')

    # Scrape main image and save as variable called "featured_mars_image"
    mars_image = image_soup.find("img", class_="main_image")
    source = mars_image.get("src")
    featured_mars_image = f'https://www.jpl.nasa.gov{source}'

    # Image from Nasa Website 
    # mars_img = featured_mars_image

    return featured_mars_image

def scrape_twit():
    browser = init_browser()

    # Path to Mars Twitter Feed
    featured_twit_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(featured_twit_url)

    # Beautiful Soup command
    html = browser.html
    twit_soup = BeautifulSoup(html, 'html.parser')

    # Scrape weather from Mars Twitter Acct.
    mars_twit = twit_soup.find("div", class_="js-tweet-text-container")

    # Text from Mars Twitter
    twitter = mars_twit.get_text()

    return twitter

def scrape_facts():
    # browser = init_browser()

    # Scrape mars facts from mars facts website provided
    mars_facts = "https://space-facts.com/mars/#facts"

    # Convert to PDataFrame
    facts_table = pd.read_html(mars_facts)
    facts_table[0]

    # Clean PDataFrame
    mars_facts_df = facts_table[0]
    mars_facts_df.columns = ["Parameter", "Values"]
    mars_facts_df.set_index(["Parameter"], inplace=True)

    # Convert PDataFrame to HTML
    mars_html_table = mars_facts_df.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    html = mars_html_table

    return html 



def scrape_hemis():
    browser = init_browser()

    # Visit hemispheres website through splinter module 
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    # Store the main_ul 
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored
    for i in items: 
     # Store title
        title = i.find('h3').text
    
        # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
        # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + partial_img_url)
            
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
            
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')
            
        # Retrieve full image source 
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
        # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
            
        # Display hemisphere_image_urls
        hemis = hemisphere_image_urls

    return hemis


def scrape_all():
    title, paragraph = scrape_info()    
    data = {

        "title": title,
        "paragraph": paragraph,
        "mars_image": scrape_img(),
        "twitter": scrape_twit(),
        "mars_html": scrape_facts(),
        "mars_hemi_images": scrape_hemis()

    }

    return data





    










   