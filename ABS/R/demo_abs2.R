#generate url here: http://stat.data.abs.gov.au/
library(rsdmx)
myUrl <- "http://stat.data.abs.gov.au/restsdmx/sdmx.ashx/GetData/ABS_SEIFA2016_SA2/101051540+101051539.IRSAD.SCORE+RWA+RWAR+RWAD+RWAP+RWST+RWSR+RWSD+RWSP+MINS+MAXS+URP/all?startTime=2016&endTime=2016"
dataset <- readSDMX(myUrl)
stats <- as.data.frame(dataset)
stats
#ASGS_2016 SEIFAINDEXTYPE SEIFA_MEASURE TIME_FORMAT obsTime obsValue
#1  101051540          IRSAD          MINS         P1Y    2016      879
#2  101051540          IRSAD          RWAR         P1Y    2016      965
#3  101051539          IRSAD          RWSD         P1Y    2016        3
#4  101051540          IRSAD          RWAP         P1Y    2016       45
#5  101051539          IRSAD         SCORE         P1Y    2016      933
#6  101051540          IRSAD           URP         P1Y    2016    12670
#7  101051539          IRSAD          RWAR         P1Y    2016      481
#8  101051539          IRSAD          RWAP         P1Y    2016       23
#9  101051540          IRSAD          RWSR         P1Y    2016      262
#10 101051539          IRSAD          MINS         P1Y    2016      696
#11 101051540          IRSAD          RWSP         P1Y    2016       47
#12 101051539          IRSAD           URP         P1Y    2016    22890
#13 101051540          IRSAD          MAXS         P1Y    2016     1076
#14 101051540          IRSAD          RWAD         P1Y    2016        5
#15 101051539          IRSAD          RWSR         P1Y    2016      125
#16 101051539          IRSAD          RWSP         P1Y    2016       23
#17 101051539          IRSAD          MAXS         P1Y    2016     1115
#18 101051540          IRSAD          RWSD         P1Y    2016        5
#19 101051540          IRSAD         SCORE         P1Y    2016      984
#20 101051539          IRSAD          RWAD         P1Y    2016        3
myUrl <- "http://stat.data.abs.gov.au/restsdmx/sdmx.ashx/GetData/ABS_C16_T01_SA/3+1+2.TT.1.SA2.101051540+101051539/all?startTime=2016&endTime=2016"
dataset <- readSDMX(myUrl)
stats <- as.data.frame(dataset)
stats
#SEX_ABS AGE STATE REGIONTYPE ASGS_2016 TIME_FORMAT obsTime obsValue
#1       1  TT     1        SA2 101051539         P1Y    2016    11447
#2       2  TT     1        SA2 101051539         P1Y    2016    11441
#3       3  TT     1        SA2 101051539         P1Y    2016    22890
#4       1  TT     1        SA2 101051540         P1Y    2016     6543
#5       2  TT     1        SA2 101051540         P1Y    2016     6127
#6       3  TT     1        SA2 101051540         P1Y    2016    12670

library(jsonlite)
full_api_url <- 'http://stat.data.abs.gov.au/sdmx-json/data/ABS_C16_T01_SA/1+3+2.TT.1.SA2.101061541+101051539+101051540/all?detail=Full&dimensionAtObservation=AllDimensions&startPeriod=2016&endPeriod=2016'

fromJSON(full_api_url)
#$header
#$header$id
#[1] "d536c16b-28c7-4646-91e9-b2411c67ee90"
#
#$header$test
#[1] FALSE
#
#$header$prepared
#[1] "2020-03-22T07:17:54.9026565Z"
#
#$header$sender
#$header$sender$id
#[1] "ABS"
#
#$header$sender$name
#[1] "Australian Bureau of Statistics"
#
#
#$header$links
#                                                                                                                                                                                            href
#1 http://stat.data.abs.gov.au:80/sdmx-json/data/ABS_C16_T01_SA/1+3+2.TT.1.SA2.101061541+101051539+101051540/all?detail=Full&dimensionAtObservation=AllDimensions&startPeriod=2016&endPeriod=2016
#      rel
#1 request
#
#
#$dataSets
#       action observations.0:0:0:0:0:0 observations.1:0:0:0:0:0 observations.2:0:0:0:0:0
#1 Information             11447, 0, NA             11441, 0, NA             22890, 0, NA
#  observations.0:0:0:0:1:0 observations.1:0:0:0:1:0 observations.2:0:0:0:1:0 observations.0:0:0:0:2:0
#1              6543, 0, NA              6127, 0, NA             12670, 0, NA              3118, 0, NA
#  observations.1:0:0:0:2:0 observations.2:0:0:0:2:0
#1              3385, 0, NA              6506, 0, NA
#
#$structure
#$structure$links
#                                                               href      rel
#1 http://stat.data.abs.gov.au/sdmx-json/dataflow/ABS_C16_T01_SA/all dataflow
#
#$structure$name
#[1] "Census 2016, Age by Sex (SA2+)"
#
#$structure$description
#[1] "Census 2016, Age by Sex (SA2+)"
#
#$structure$dimensions
#$structure$dimensions$observation
#  keyPosition          id            name                                                           values
#1           0     SEX_ABS             Sex                                 1, 2, 3, Males, Females, Persons
#2           1         AGE             Age                                                     TT, All ages
#3           2       STATE           State                                               1, New South Wales
#4           3  REGIONTYPE Geography Level                                    SA2, Statistical Area Level 2
#5           4   ASGS_2016          Region 101051539, 101051540, 101061541, Goulburn, Goulburn Region, Yass
#6          NA TIME_PERIOD     Census year                                                       2016, 2016
#         role
#1        <NA>
#2        <NA>
#3        <NA>
#4        <NA>
#5        <NA>
#6 TIME_PERIOD
#
#
#$structure$attributes
#$structure$attributes$dataSet
#list()
#
#$structure$attributes$series
#list()
#
#$structure$attributes$observation
#           id               name      values
#1 TIME_FORMAT        Time Format P1Y, Annual
#2  OBS_STATUS Observation Status        NULL
#
#
#$structure$annotations
#                      title uri
#1 Statistical usage warning    
#                                                                                                                                       text
#1 ABS.Stat beta is continuing to be developed.  Data will be updated as soon as possible following its 11:30 am release on the ABS website.

