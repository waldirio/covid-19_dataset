# covid-19_dataset

The main idea of this project is to collect the data shared on the link below and create a single dataset, combining all the availables reports in different schemas.
```
https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
```

At the end, the schema is based on the latest version and the whole information will be available in a single file. Also, another great improvement, there is a single column `Report_Data` where this field will be responsible for keep the timeframe track. This is better because we can keep the current number of columns and add new information with no impact.

Here we can see a simple snippet
```
Report_Data,FIPS,Admin2,Province_State,Country_Region,Last_Update,Lat,Long_,Confirmed,Deaths,Recovered,Active,Combined_Key
01-22-2020,,,Anhui,Mainland China,1/22/2020 17:00,,,1,,,,
01-22-2020,,,Beijing,Mainland China,1/22/2020 17:00,,,14,,,,
01-22-2020,,,Chongqing,Mainland China,1/22/2020 17:00,,,6,,,,
...
03-24-2020,27011,Big Stone,Minnesota,US,2020-03-24 23:37:31,45.42712824,-96.41403739,1,0,0,0,"Big Stone, Minnesota, US"
03-24-2020,38007,Billings,North Dakota,US,2020-03-24 23:37:31,47.02366884,-103.3762965,0,0,0,0,"Billings, North Dakota, US"
03-24-2020,16011,Bingham,Idaho,US,2020-03-24 23:37:31,43.21672879999999,-112.3978437,2,0,0,0,"Bingham, Idaho, US"
...
03-29-2020,,,,West Bank and Gaza,2020-03-29 23:08:13,31.9522,35.2332,109,1,18,90,West Bank and Gaza
03-29-2020,,,,Zambia,2020-03-29 23:08:13,-13.133897,27.849332,29,0,0,29,Zambia
03-29-2020,,,,Zimbabwe,2020-03-29 23:08:13,-19.015438,29.154857,7,1,0,6,Zimbabwe
```

Ps.: The python version used was 3.7, however, you probably will be able to run on python 2.6 as well.

To run, just clone the code and execute as below
```
$ ./covid-19_dataset.py 
Link: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
01-22-2020.csv
01-23-2020.csv
01-24-2020.csv
01-25-2020.csv
01-26-2020.csv
...
03-27-2020.csv
03-28-2020.csv
03-29-2020.csv
Saving to file: covid_final_timeframe.csv
```

Hope you enjoy this dataset.

Be Safe
Waldirio