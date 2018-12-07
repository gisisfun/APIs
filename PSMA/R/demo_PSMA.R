library(httr)
library(jsonlite)
## 
## Attaching package: 'jsonlite'
## 
## The following object is masked from 'package:utils':
## 
##     View

key <- 'brAKupqRdkXNpkYRhy6SpPe1ErVJiAEc'
full_api_url <- 'https://api.psma.com.au/beta/v1/addresses?addressString=1%20bowes%20st%20phillip%20act%202606&stateTerritory=ALL&datum=GDA94&page=1&perPage=10'

header <- '{"Authorization": key,"Accept": "application/json"}'

