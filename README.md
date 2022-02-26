# TANet-IP-JSON

## 說明

在臺灣學術網路中，包含學校IP、校名以及校徽URL的JSON檔

## 來源

IP列表來源：[TANet - 維基百科](https://zh.wikipedia.org/wiki/TANet)  
URL來源：透過上述網站取得校名，再連結至維基頁面，擷取HTML中第一張圖片作為校徽

## 可使用的檔案

| file | description |
|-|-|
| TANet_140112_140125.json | 140.112~140.125 |
| TANet.json | 無重疊的IP，有URL，但不確定是否都是校徽 |
| TANet_ranged.json | IP有重疊，有URL |
| TANet_no_url.json | URL查詢回傳-1，無法查詢，可能是維基查詢網址不對 |

## 其他檔案

| file | description |
|-|-|
| raw.txt | 由TANet維基百科網站取得，並擷取其中包含校名及IP的部分 |
| TANet_name_bug.json | 校名異常，目前沒有內容 |
| get_info.py | 取得URL及下載圖片(僅少數成功下載並開啟)的函式 |
| main.py | 各種爬蟲跟測試用的程式碼，完全沒有整理，慎入XD |

## Author's Word

做這個主要是~~228連假太無聊~~為了[場外大大開發的外掛](https://forum.gamer.com.tw/C.php?page=1&bsn=60076&snA=6922106&gothis=82105039#82105039)新增一點小東西  
希望會有用處(?)