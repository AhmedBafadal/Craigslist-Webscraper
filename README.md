# Craigslist Web Scraper

## Description
A web scraping application extracting 200+ job posts from Craigslist related to engineering in New York City, US. 

Link: https://newyork.craigslist.org/search/egr

Multiple data points can be extracted from each post that are listed in paginated search results, and is saved in a json file (items.json), containing the job title, job description, URL, compensation, address and employment type (e.g. full-time).


## Installation
```
pip install scrapy

scrapy crawl jobs -o items.json
```