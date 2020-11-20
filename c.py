import csv
from datetime import datetime, timezone

with open('Yangon_HO.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    def aqiFromPM(PM25):
        if PM25 is None:
            return "-"
        if PM25 < 0:
            return PM25
        if PM25 > 1000:
            return "-"
        if PM25 > 350.5:
            return calcAQI(PM25, 500, 401, 500, 350.5)
        elif PM25 > 250.5:
            return calcAQI(PM25, 400, 301, 350.4, 250.5)
        elif PM25 > 150.5:
            return calcAQI(PM25, 300, 201, 250.4, 150.5)
        elif PM25 > 55.5:
            return calcAQI(PM25, 200, 151, 150.4, 55.5)
        elif PM25 > 35.5:
            return calcAQI(PM25, 150, 101, 55.4, 35.5)
        elif PM25 > 12.1:
            return calcAQI(PM25, 100, 51, 35.4, 12.1)
        elif PM25 > 0:
            return calcAQI(PM25, 50, 0, 12, 0)
        else:
            return "-"

    def getAQImessage(aqi):
        if aqi is None:
            return "-"
        elif aqi == "-":
            return "-"
        elif aqi >= 301:
            return 'Hazardous'
        elif aqi >= 201:
            return 'Very Unhealthy'
        elif aqi >= 151:
            return 'Unhealthy'
        elif aqi >= 101:
            return 'Unhealthy for Sensitive Groups'
        elif aqi >= 51:
            return 'Moderate'
        elif aqi >= 0:
            return 'Good'
        else:
            return
    
    

    def getRiskFactor(aqi):
        if aqi is None:
            return "-"
        elif aqi == "-":
            return "-"
        elif aqi >= 301:
            return '5'
        elif aqi >= 201:
            return '4'
        elif aqi >= 151:
            return '3'
        elif aqi >= 101:
            return '2'
        elif aqi >= 51:
            return '1'
        elif aqi >= 0:
            return '0'
        else:
            return
    


    def calcAQI(Cp, Ih, Il, BPh, BPl):
        a = Ih - Il
        b = BPh - BPl
        c = Cp - BPl
        return round((a/b)*c + Il)

    with open('Yangon_HO_AQI.csv', mode='w') as SCA_file:
        SCA_writer = csv.writer(SCA_file, delimiter=',', quotechar='"', quoting =csv.QUOTE_MINIMAL)
        SCA_writer.writerow(['Created At','PM2.5 AQI','AQImessage','Risk Factor'])

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                try:
                    pm25_Int = float(row[8])
                    AQI = aqiFromPM(pm25_Int)
                except:
                    AQI = "-"
                AQImessage = getAQImessage(AQI)
                RiskFactor = getRiskFactor(AQI)
                SCA_writer.writerow([row[0], AQI, AQImessage, RiskFactor])
                line_count += 1
            print(f'Processed {line_count} lines.')

