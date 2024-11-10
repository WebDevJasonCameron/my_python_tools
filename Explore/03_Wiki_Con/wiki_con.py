import os
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import time

# <C> Wiki Parser
class WikiParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []
        self.assets = []

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            full_url = urljoin(self.base_url, value)
            parsed_url = urlparse(full_url)

            # Check for internal links
            if parsed_url.netloc == urlparse(self.base_url).netloc:
                if tag == 'a' and attr == 'href':
                    self.links.append(full_url)
                elif tag in ['img', 'script', 'link'] and attr in ['src', 'href']:
                    self.assets.append(full_url)

# <F> Download Page
def download_page(url, base_dir, auth_handler):
    try:
        # Open URL with authentication
        opener = urllib.request.build_opener(auth_handler)
        urllib.request.install_opener(opener)
        response = opener.open(url)
        
        # Add delay to ensure page load
        time.sleep(2)
        
        html_content = response.read().decode('utf-8')
        
        # Parse the page content for links and assets
        parser = WikiParser(url)
        parser.feed(html_content)

        # Save HTML to local file
        page_path = url_to_filename(url, base_dir)
        os.makedirs(os.path.dirname(page_path), exist_ok=True)
        
        # Download assets and update HTML content
        html_content = download_assets(parser.assets, url, base_dir, html_content)

        with open(page_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        print(f"Downloaded {url}, found links: {parser.links} and assets: {parser.assets}")
        
        # Return discovered internal links
        return parser.links
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return []

# <F> Download Assets
def download_assets(assets, base_url, base_dir, html_content):
    for asset_url in assets:
        try:
            asset_data = urllib.request.urlopen(asset_url).read()
            asset_filename = os.path.basename(urlparse(asset_url).path)
            asset_path = os.path.join(base_dir, "assets", asset_filename)
            os.makedirs(os.path.dirname(asset_path), exist_ok=True)
            
            # Save the asset locally
            with open(asset_path, 'wb') as asset_file:
                asset_file.write(asset_data)
            
            # Update HTML to use local asset path
            html_content = html_content.replace(asset_url, os.path.join("assets", asset_filename))
            print(f"Downloaded asset {asset_url} -> {asset_path}")
        except Exception as e:
            print(f"Failed to download asset {asset_url}: {e}")
    return html_content

# <F> URL to Filename
def url_to_filename(url, base_dir):
    parsed = urlparse(url)
    path = parsed.path.strip('/').replace('/', '_')
    if not path:
        path = 'index'
    return os.path.join(base_dir, f"{path}.html")

# Example setup with authentication
username = 'your_username'
password = 'your_password'
base_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
base_dir = "./test_scrape_archive"

# Setup authentication handler
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, base_url, username, password)
auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# Initialize crawl queue
links_to_crawl = [base_url]
crawled_links = set()

# Crawl loop
while links_to_crawl:
    # Get the next URL to process
    url = links_to_crawl.pop()
    
    # Skip if already crawled
    if url in crawled_links:
        continue

    # Mark as crawled
    crawled_links.add(url)
    
    # Download the page and get its links
    new_links = download_page(url, base_dir, auth_handler)
    
    # Add new links to the crawl queue if not yet crawled
    for link in new_links:
        if link not in crawled_links:
            links_to_crawl.append(link)
