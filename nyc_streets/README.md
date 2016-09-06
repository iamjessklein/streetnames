
# Scraping NYC Street Data

## What?

A python based tool that uses [scrapy](https://scrapy.org/) to extract data from [nycstreets.info](http://nycstreets.info/) and converts it to csv using [CSVKit](https://github.com/wireservice/csvkit)

## Setup

This project has been tested using [miniconda](http://conda.pydata.org/miniconda.html). If you have miniconda already installed, a new environment for running this scraper could be setup using the following command:

```
conda create --name=scrapy python=2 scrapy

```

Which will create a new conda environment called `scrapy` and install the Scrapy python package in this environment.

To activate this environment, run:

```
source activate scrapy
```

Then CSVKit can be installed using pip:

```
pip install csvkit
```

## Run

To run, checkout the `run.sh` script.

Once the dependencies are installed, the scraper and conversion should runnable by just running `run.sh`

```
./run.sh
```

This will create `data/street_names.json` and `data/street_names.csv`.


