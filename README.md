# SatNOGS crawler
SatNOGS database crawler - audio &amp; waterfall data download.

## Usage
Download the repo and run `scrapy crawl satnogs -a noradId=XXXXX` in main folder. 

## Result
- `/data` folder - JSON file generated with all observations meta for choosen satellite.
- `/files/audio` - *.ogg audio files
- `/files/waterfall` - *.png waterfall files

More options soon.
