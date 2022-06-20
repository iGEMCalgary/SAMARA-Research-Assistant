# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
'''
SAMARA iGEM Research Assistant
pipelines.py

This file creates and defines a item pipeline to process and export the WikiPage scrapy items 
established in items.py

Doesn't run on it's own; is accessed from iGEMScraper.py when running the command
'''

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonLinesItemExporter
# import and initialize the tokenizer and model from the checkpoint
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
import re
# Optional parameter to allow for debugging while running from scrapy. Not necessary unless something has gone terribly wrong.
# import os
# # os.environ['CUDA_LAUNCH_BLOCKING'] = "1"
import torch


nltk.download('punkt')  # Downloads the Punkt tokenizer model
checkpoint = "sshleifer/distilbart-cnn-12-6"  # This is the path for the model used (in reference to transformers)
device = 'cuda:0' if torch.cuda.is_available() else 'cpu' # Checks if the device has a GPU present to speed up summarizer; if you don't, you just get slow CPU summarization. I would really, really, really recommend using GPU summarization.

tokenizer = AutoTokenizer.from_pretrained(checkpoint) 
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint).to(device)  # Sets the model and sends it to the GPU/CPU depending on the device parameter

def generate_summary(text):
  '''
    Summarizes the input text using PyTorch and the DistilBART CNN 12-6 pretrained model 
    provided by transformers.

    Arguments:
        text (str): the text content of the page you want summarized.

    Returns:
        compiled_summary (str): the summarized version of the page.
    '''

  sentences = nltk.tokenize.sent_tokenize(text) # Tokenize the text into sentences (list)
  # Initialize values/parameters
  length = 0
  chunk = ""
  chunks = []
  count = -1

  for sentence in sentences:
    count += 1
    combined_length = len(tokenizer.tokenize(sentence)) + length  # Add the number of sentence tokens to the length counter

    if combined_length  <= tokenizer.max_len_single_sentence: # If it doesn't exceed the maximum sentence length
      chunk += sentence + " "   # Add the sentence to the chunk
      length = combined_length  # Update the length counter

      # If it is the last sentence
      if count == len(sentences) - 1:
        chunks.append(chunk.strip())  # Save the chunk
      
    else: 
      chunks.append(chunk.strip())    # Save the chunk
      
      # Reset the parameters
      length = 0 
      chunk = ""

      # Take care of the overflow sentence
      chunk += sentence + " "
      length = len(tokenizer.tokenize(sentence))
  len(chunks)

  # Inputs to the model
  inputs = [tokenizer(chunk, return_tensors="pt", max_length=1024, truncation=True).to(device) for chunk in chunks]
  
  compiled_summary = ''
  
  # For every chunk of the tokenized text
  for input in inputs:
    # Generate the summary
    output = model.generate(**input)
    # Add each chunk of summary to a string
    compiled_summary = compiled_summary + tokenizer.decode(*output, skip_special_tokens=True)

  return compiled_summary   

class KeystoneXL:
    '''
    The primary item pipeline for the WikiPage objects. Conditionally extracts the scraped information
    into the file specified in the self.file variable.
    
    Must also be specified in the settings.py file under ITEM_PIPELINES in order to function.
    '''

    def open_spider(self, spider): # Runs when the spider starts
        self.file = open('samara.jl', 'wb') # Opens the file specified. wb is necessary for the JsonLinesItemExporter and will overwrite the file each run
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8')  # Uses the built in JsonLineItemExporter class to export the file
        self.exporter.start_exporting() # Starts the exporter and waits for an item

    
    def close_spider(self, spider): # Runs when the spider ends
        self.exporter.finish_exporting()    # Ends the exporter
        self.file.close()   # Closes the file
    
    def process_item(self, item, spider):   # Runs when an item is yielded in iGEMScraper.py
        
        scraped_data = ItemAdapter(item)    # Adapts the item into a dict-like ItemAdapter object to process
        strings_to_check_for = ['No Page Text', # A list of strings found in false-positive, empty pages
                            'The requested page title was invalid', 
                            'This page is used by the judges to evaluate your team',
                            'This is a template page',
                            'There is currently no text',
                            'In order to be considered for the',
                            ]
        
        if any(bad_string in scraped_data['pagetext'] for bad_string in strings_to_check_for) == True:  # Checks if any of the false positive strings exists
            raise DropItem('Invalid Page Removed!') # If any string exists, drop the item, stop processing, and do not export
        
        if len(scraped_data['pagetext']) < 100: # Checks to ensure the page has sufficient content
            raise DropItem('Page too short')    # If any pagetext too short, drop the item, stop processing, and do not export
        
        scraped_data['pagetext'] = re.sub(r'\$\$.+?\$\$', '', scraped_data['pagetext']) # Removes equations from the exported data
        scraped_data['pagetext'] = re.sub(r'\$.+?\$', '', scraped_data['pagetext']) # Removes equations from the exported data
        scraped_data['pagetext'] = generate_summary(scraped_data['pagetext'])
        #put summarizer here
        item.save() # Saves the item to the Django Database
        self.exporter.export_item(item) # Exports the item to the file specified
        return item 