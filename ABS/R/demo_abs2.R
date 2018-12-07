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
