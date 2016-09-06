

mkdir -p data
rm -f data/street_names.json
rm -f data/street_names.csv

scrapy crawl nyc -o data/street_names.json
in2csv data/street_names.json > data/street_names.csv

