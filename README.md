# SAMARA iGEM Research Assistant

A comprehensive tool to parse through the software and modelling pages of various iGEM teams. The project serves as a Django-based front-end deployment of the initial [iGEMScraper](https://github.com/iGEMCalgary/iGEMScraper) module. This project is heavily inspired by iGEM Calgary's 2018 project [SARA](https://github.com/iGEMCalgary/research-assistant). The project aims to expand upon SARA by fully automating the scraper-to-deployment pipeline while also increasing the scope of the project by including modelling pages.

The information is extracted using the scraper, summarized using the [DistilBART CNN 12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) model, and then passed to a Django database using the [scrapy-djangoitem](https://github.com/scrapy-plugins/scrapy-djangoitem) plugin. From there, it is deployed using standard Django features onto the [site here]().

## Installation

1. Download the files from the repository
2. Create a virtual environment and run the following commands from inside the virtual environment to install the required packages:    
`pip install torch --extra-index-url https://download.pytorch.org/whl/cu113`    
`pip install -r requirements.txt`  
  
A brief overview of the major packages installed and their usage in the program are listed below:

| Library/Module | Usage |
| -------------- | ----- |
| Scrapy | Creates the CrawlSpider used to parse and scrape iGEM wiki pages. |
| RegEx | Allows for string processing and the usage of wildcard text patterns. |
| lxml | Allows for HTML processing and cleaning to help sanitize scraping outcomes. |
| parsel | Adds CSS selectors to extract text from the html page body. |
| Django | Creates a python-based deployment of the scraped pages. |
| scrapy-djangoitem | Allows for Scrapy to interface with and output Django model items. |
| nltk | Tokenizes the sentances for use with the DistilBART CNN 12-6 model. |
| transformers | Provides access to the DistilBART CNN 12-6 model. |
| PyTorch | Requirement to use the DistilBART CNN 12-6 model. Also allows access to CUDA-based summarization. |

## Usage

The program is run through the terminal. In order to do so, we must first navigate to the first netscrape_nav folder. If inside the project folder, the command to do so is as follows:
  
`cd ./netscrape_nav`  
  
We can then run the scraper itself using the following command:  
  
`scrapy crawl tomholland`  

This command can be somewhat modified to suit your needs and documentation to do so is available on the [Scrapy docs](https://docs.scrapy.org/en/latest/index.html). By default, the project will output to a file named samara.jl, located in the first netscrape_nav folder. This is to allow for the scraped items to be used seperately from the Django deployment. The project will also save each scraped object to the db.sqlite3 file inside the SAMARADeployment folder, allowing Django to access the information.

## Modification

### Page Selection
  
As a default, the program scrapes any page that contains Software or Mode* in the URL. To change the pages scraped, you must first create a Link Extractor rule (in iGEMScraper.py) to parse the URL for certain keywords. Certain pages are standardized amongst iGEM teams and thus, are simpler to create rules for. Regular Expressions may be used to create wildcard rules to help increase the scope of the scraper for more inconsistant page namings (see rule #2 and the [RegularExpressions documentation](https://docs.python.org/3/library/re.html) for more information and examples of their usage). 

### Item Processing

Item processing begins in the items.py file, with the defining of a DjangoItem WikiPage object for each Django "model" item. Each item in the file should correspond to a Django app model, as defined in each app's model.py file. A scrapy-djangoitem DjangoItem object functions near identically to a standard scrapy Item object; both are dictionary-like objects that allow for information to remain organized and catagorized. Each existing WikiPage Item *should* be sufficent for scraping iGEM wiki pages, but if necessary, it can be easily modified to accept different parameters. The process to add a scraper parameter is as follows:

1. Create a new Django app for the page type you wish to scrape.
2. Create a models.py file inside of the new app folder and define the model. The existing models.py files inside of the "software" and "model" folders may serve as good examples for model definitions.
3. Define the items in the netscrape_nav/netscrape_nav/items.py file. Make sure to import the created models and to define each DjangoItem as terms of one (using the django_model variable).
4. Create a scrapy rule (in netscrape_nav/netscrape_nav/spiders/iGEMScraper.py) to select pages that meet a criteria and define a function to call when an item is found.
5. Create an Item instance inside of the function and pass to it the appropriate parameters.

The second step involves post processing in the pipelines.py file. While some preliminary processing is done before creating a WikiPage Item (in netscrape_nav/netscrape_nav/items.py), we further process it here to remove unwanted characteristics from the scraped text. This file contains the summarizer model, processing the pagetext into a (relatively) short, useful summary. This step can be easily expanded on, with additional processing steps being a few lines of code away.
  
This step also includes the removal of default or unpopulated wiki pages, pages that do not follow standard iGEM convention, and other broken or otherwise unusable pages. 

### Exporting
  
Exporting is also done through the pipelines.py file. By default, the scraper will use the JsonLinesItemExporter provided by Scrapy. This will export the pages as a .jl file. If changing the export format is desired or if the existing functionality is simply not enough, one may use the Scrapy [Item Exporters](https://docs.scrapy.org/en/latest/topics/exporters.html) and the [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html) docs to customize the functionality of the exporter. As part of the Djagno integration, the project also exports the files as an sqlite3 file. Functionality for using these files is built into Django, though you may use any SQL tool to process the data within it.

The code is able to automatically construct 
  
## License
The code is provided under the MIT license.
