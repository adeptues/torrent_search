# Torrent search aggregator to avoid adds

http://nyaa.se

curl 'http://www.nyaa.se/?page=search&cats=0_0&filter=0&term=berserk'
-H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, sdch' -H
'Accept-Language: en-GB,en-US;q=0.8,en;q=0.6' -H
'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux
x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82
Safari/537.36' -H 'Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
-H 'Cache-Control: no-cache' -H 'Cookie:
__cfduid=d4eebb508180693e5509c3d3792fd39031472916813' -H 'Connection:
keep-alive' --compressed

## notes

will need to load a different parser for each domain / url
externalises urls to search to a config file
