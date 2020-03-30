#!/usr/bin/env python
"""
Code created by Waldirio M Pinheiro <waldirio@gmail.com> to collect the 
multiple data and create a single file adding the new column "report_data".
This field will be responsible to present the graphic timeframe and trends.
"""

import csv
import re
import os
import requests
import urllib3

URL = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"
SITE_BASE = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"

final_list = []
stage = []


def save_to_file():
    """
    Function responsible to generate the csv file
    """
    print("Saving to file: covid_final_timeframe.csv")
    with open("covid_final_timeframe.csv", "w") as file_result:
        csv_file = csv.writer(file_result)
        for records in final_list:
            csv_file.writerow(records)


def website_query():
    """
    Function responsible for collect the reports on github page and
    work with. When a new file be created, this script will be able
    to figure out, download and create a new output file including
    the whole information.
    """
    http = urllib3.PoolManager()
    r = http.request('GET', URL)
    links = re.findall('[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9].csv', str(r.data))
    print("Link: {}".format(URL))
    links = list(set(links))
    links.sort()

    for file_name in links:
        print(file_name)

        file_structure_01 = False
        file_structure_02 = False
        file_structure_03 = False
        header = True

        each_csv = requests.get(SITE_BASE + file_name)

        # each_csv = requests.get(SITE_BASE + "03-22-2020.csv")
        # each_csv = requests.get(SITE_BASE + "03-23-2020.csv")
        #
        # each_csv = requests.get(SITE_BASE + "01-22-2020.csv")
        # each_csv = requests.get(SITE_BASE + "03-19-2020.csv")
        # each_csv = requests.get(SITE_BASE + "03-29-2020.csv")
        # print(each_csv.status)
        open('temp_file.csv', 'wb').write(each_csv.content)

        with open('temp_file.csv.aux', "w") as stage_file:
            for line in open('temp_file.csv'):
                line = line.rstrip()
                # print(line)
                stage_file.write(line + '\n')
            os.rename('temp_file.csv.aux', 'temp_file.csv')

        with open('temp_file.csv') as fp:
            ref_file = csv.reader(fp)
            for row in ref_file:
                # print(row)
                if (row[0] == "FIPS") or \
                   (row[0] == "\ufeffFIPS") and \
                   (row[1] == "Admin2") and \
                   (row[2] == "Province_State") and \
                   (row[3] == "Country_Region") and \
                   (row[4] == "Last_Update") and \
                   (row[5] == "Lat") and \
                   (row[6] == "Long_") and \
                   (row[7] == "Confirmed") and \
                   (row[8] == "Deaths") and \
                   (row[9] == "Recovered") and \
                   (row[10] == "Active") and \
                   (row[11] == "Combined_Key"):
                    file_structure_01 = True
                    header = True
                elif (row[0] == "\ufeffProvince/State") or \
                     (row[0] == "Province/State") and \
                     (row[1] == "Country/Region") and \
                     (row[2] == "Last Update") and \
                     (row[3] == "Confirmed") and \
                     (row[4] == "Deaths") and \
                     (row[5] == "Recovered"):
                    file_structure_02 = True
                    header = True
                elif (row[0] == "Province/State") and \
                     (row[1] == "Country/Region") and \
                     (row[2] == "Last Update") and \
                     (row[3] == "Confirmed") and \
                     (row[4] == "Deaths") and \
                     (row[5] == "Recovered") and \
                     (row[6] == "Latitude") and \
                     (row[7] == "Longitude"):
                    file_structure_03 = True
                    header = True
                else:
                    header = False
                    if file_structure_01 and not header:
                        row.insert(0, file_name.split(".")[0])
                        final_list.append(row)
                    elif file_structure_02 and not header:
                        row.insert(0, file_name.split(".")[0])
                        row.insert(1, "")
                        row.insert(1, "")
                        row.insert(6, "")
                        row.insert(6, "")
                        row.insert(11, "")
                        row.insert(11, "")
                        final_list.append(row)
                    elif file_structure_03 and not header:
                        aux = []
                        row.insert(0, file_name.split(".")[0])
                        row.insert(1, "")
                        row.insert(1, "")
                        row.insert(11, "")
                        row.insert(11, "")
                        aux.insert(0, row[0])
                        aux.insert(1, row[1])
                        aux.insert(2, row[2])
                        aux.insert(3, row[3])
                        aux.insert(4, row[4])
                        aux.insert(5, row[5])
                        aux.insert(6, row[9])
                        aux.insert(7, row[10])
                        aux.insert(8, row[6])
                        aux.insert(9, row[7])
                        aux.insert(10, row[8])
                        aux.insert(11, row[11])
                        aux.insert(12, row[12])
                        row = aux
                        final_list.append(row)
                    else:
                        print("CHECK NEW STRUCTURE {}".format(ref_file))


def main():
    """
    Main function.
    """

    final_list.append(['Report_Data',
                       'FIPS',
                       'Admin2',
                       'Province_State',
                       'Country_Region',
                       'Last_Update',
                       'Lat',
                       'Long_',
                       'Confirmed',
                       'Deaths',
                       'Recovered',
                       'Active',
                       'Combined_Key'])
    website_query()
    save_to_file()


if __name__ == "__main__":
    main()
