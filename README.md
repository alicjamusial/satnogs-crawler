# SatNOGS crawler
SatNOGS database crawler - audio &amp; waterfall data download based on python [scrapy](https://github.com/scrapy/scrapy).

## Usage
Download the repo and run `scrapy crawl satnogs -a noradId=XXXXX` in main folder. 

## Result
- `/data` - JSON file generated with all observations meta for choosen satellite.
- `/files/audio` - *.ogg audio files
- `/files/waterfall` - *.png waterfall files

## Performance
Downloading all the data & files takes even several dozen minutes. But if something goes wrong and the script fails, you can run it again and it won't download the file if it already exists in the folder.

## Future?
Probably choosing start & end dates of downloaded files. More info soon.
