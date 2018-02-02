# Simple scrapy project

The first project I did while learning the scrapy framework. It simply parses rating of students of ITMO University from ITMO DE system.

## Getting Started

Firstly clone this repository

```
git clone https://github.com/alexpulich/scrapy-de-ifmo-rating.git
cd scrapy-de-ifmo-rating
```

Install all the dependencies from requirements.txt using pip.

```
pip install -r requirements.txt
```

## Running

To scrap the data to json file execute following instructions

```
cd de_ifmo_rating
scrapy crawl rating -o <filename>.json
```