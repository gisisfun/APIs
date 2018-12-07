
library(httr)
library(rjson)   # for fromJSON(...)

key <- "brAKupqRdkXNpkYRhy6SpPe1ErVJiAEc"

full_api_url <- "https://api.psma.com.au/beta/v1/addresses?addressString=1%20bowes%20st%20phillip%20act%202606&stateTerritory=ALL&datum=GDA94&page=1&perPage=10"
getdata<-GET(url=full_api_url, add_headers(Authorization=key))

fromJSON(content(getdata,type="text"))
#output
#$data
#        addressId               addressString                     formattedAddress
#1  GAACT716851937 1 bowes st phillip act 2606         1 BOWES PL, PHILLIP ACT 2606
#2  GAACT716244438 1 bowes st phillip act 2606      1-15 BOWES PL, PHILLIP ACT 2606
#3  GAACT717647705 1 bowes st phillip act 2606 LEVEL 2 1 BOWES PL, PHILLIP ACT 2606
#4  GAACT717647706 1 bowes st phillip act 2606 LEVEL 3 1 BOWES PL, PHILLIP ACT 2606
#5  GAACT717647707 1 bowes st phillip act 2606 LEVEL 4 1 BOWES PL, PHILLIP ACT 2606
#6  GAACT717647708 1 bowes st phillip act 2606 LEVEL 5 1 BOWES PL, PHILLIP ACT 2606
#7  GAACT717647709 1 bowes st phillip act 2606 LEVEL 6 1 BOWES PL, PHILLIP ACT 2606
#8  GAACT717647710 1 bowes st phillip act 2606 LEVEL 7 1 BOWES PL, PHILLIP ACT 2606
#9  GAACT717647711 1 bowes st phillip act 2606 LEVEL 8 1 BOWES PL, PHILLIP ACT 2606
#10 GAACT715695566 1 bowes st phillip act 2606 SUITE 1 1 BOWES PL, PHILLIP ACT 2606
#
#$links
#$links$count
#[1] 21
#
#$links$current
#[1] "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606"
#
#$links$first
#[1] "/v1/addresses?datum=GDA94&page=1&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606"
#
#$links$last
#[1] "/v1/addresses?datum=GDA94&page=3&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606"
#
#$links$`next`
#[1] "/v1/addresses?datum=GDA94&page=2&perPage=10&stateTerritory=ALL&addressString=1+bowes+st+phillip+act+2606"
#
#$links$prev
#NULL



full_api_url <- "https://api.psma.com.au/beta/v1/addresses/GAACT716851937/asgsMain/"
getdata<-GET(url=full_api_url, add_headers(Authorization=key))

fromJSON(content(getdata,type="text"))
#$addressId
#[1] "GAACT716851937"
#
#$asgsMain
#$asgsMain$`2011`
#$asgsMain$`2011`$mbId
#[1] "80036983000"
#
#$asgsMain$`2011`$sa1Id
#[1] "80109110909"
#
#$asgsMain$`2011`$sa2Id
#[1] "801091109"
#
#$asgsMain$`2011`$sa2Name
#[1] "PHILLIP"
#
#$asgsMain$`2011`$sa3Id
#[1] "80109"
#
#$asgsMain$`2011`$sa3Name
#[1] "WODEN"
#
#$asgsMain$`2011`$sa4Id
#[1] "801"
#
#$asgsMain$`2011`$sa4Name
#[1] "AUSTRALIAN CAPITAL TERRITORY"
#
#
#$asgsMain$`2016`
#$asgsMain$`2016`$mbId
#[1] "80036983000"
#
#$asgsMain$`2016`$sa1Id
#[1] "80109110914"
#
#$asgsMain$`2016`$sa2Id
#[1] "801091109"
#
#$asgsMain$`2016`$sa2Name
#[1] "PHILLIP"
#
#$asgsMain$`2016`$sa3Id
#[1] "80109"
#
#$asgsMain$`2016`$sa3Name
#[1] "WODEN VALLEY"
#
#$asgsMain$`2016`$sa4Id
#[1] "801"
#
#$asgsMain$`2016`$sa4Name
#[1] "AUSTRALIAN CAPITAL TERRITORY"


full_api_url <- "https://api.psma.com.au/beta/v1/addresses/GAACT716851937/geo/"
getdata<-GET(url=full_api_url, add_headers(Authorization=key))

fromJSON(content(getdata,type="text"))
#$addressId
#[1] "GAACT716851937"
#
#$geo
#$geo$geoDatumCode
#[1] "GDA94"
#
#$geo$geoFeature
#[1] "FRONTAGE CENTRE SETBACK"
#
#$geo$geometry
$geo$geometry$coordinates
#[1] 149.08605 -35.34404
#
#$geo$geometry$type
#[1] "Point"