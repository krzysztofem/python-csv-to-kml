# 🧭 CsvToKml

Generate kml file from csv.

## Requirements

- Python ... and ability to run scripts
- Google Sheets - https://sheets.google.com/create

## Installation

- Download or clone this repo,

- Install dependencies:

```bash
  pip install -r requirements.txt
```

## Preparation of data

Important, make copie of this document first:

https://docs.google.com/spreadsheets/d/1-PtO4JO_di4PHnSAwz-f_tFZVQGzbXbO06qucoagjRc/edit?usp=sharing

![App Screenshot](https://github.com/krzysztofem/python-csv-to-kml/blob/9f20ddd111aa7f892d832e8e1eb34455814f8b3d/screenshots/google-sheets-copy.png?raw=true)

Next, add Yours items.

Keep in mind:

- Cords like **GPS N** and **GPS E** must have a format `53.070985`. **Dot is important!**.
- Select the appropriate periods to color the points on the map.

If you already have the data ready then it's time to export it.

![App Screenshot](https://github.com/krzysztofem/python-csv-to-kml/blob/main/screenshots/google-sheets-export.png?raw=true)

## Creating a KML file

Go to the directory of the previously downloaded script.

https://docs.google.com/spreadsheets/d/1-PtO4JO_di4PHnSAwz-f_tFZVQGzbXbO06qucoagjRc/edit?usp=sharing

```bat
python main.py ~/PATH_TO_YOR_FILE/YOUR_EXPORTED_FILE.csv
```

The generated KML file will be copied to the directory `GENERATED_MAPS`, which is located in directory of the previously downloaded script.

## Google My Maps

Go to Google My Maps to create new map:
https://www.google.com/maps/d/?hl=pl

Create new map:

![App Screenshot](https://github.com/krzysztofem/python-csv-to-kml/blob/main/screenshots/google-maps-1.png?raw=true)

Import Your KML file end enjoy!

![App Screenshot](https://github.com/krzysztofem/python-csv-to-kml/blob/main/screenshots/google-maps-2.png?raw=true)
