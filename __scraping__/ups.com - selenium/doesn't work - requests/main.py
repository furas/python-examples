import requests

s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"})

r = s.get('https://wwwapps.ups.com/WebTracking/OnlineTool')
print(r.text)

# ---- ----

payload = {
	"loc": "en_PL",
	"HTMLVersion": "5.0",
	"USER_HISTORY_LIST": "",
	"trackNums": "1zwa87086796163221",
	"track.x": "Track"
}

r = s.post('https://wwwapps.ups.com/WebTracking/track', data=payload)
print(r.text)

# ---- ----

#r = s.get('https://www.ups.com/track?loc=en_PL&tracknum=1zwa87086796163221&requester=WT/

# ---- ----

headers = {
    "Accept": "application/json, text/plain, */*",
#    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
#    "Content-Length": "92",
#    "Content-Type": "application/json",
    "Cookie": "sharedsession=acfc8af0-b20f-40f2-9a43-8e4f51068fab:m; ups_language_preference=en_PL; _abck=AEB542A468041A4B2253D18A851FDCEB~0~YAAQlawQAnkccWp3AQAAnSojdQVZ/rq140+2xjFAEPeorAlX8cD2YMGA4yX3RykSLy1wn7umhdO8v9jQblwenMBUeH9dsFdQzg6vTCnugyxXnYT2kYNI2nGJD2CP4Egcm82g11ch7VJZI9YbDSxBeChRwGS228YxjZqVPFnuNRZFWDYj4MmjGaxVXtbTZ9dAE4tfWL7XFXuvPJaVuKgKgU/27N/IyNtH6cV520ai/u/n8X8lxc2W06rXJ4ZdVB1oC25HMM/FfVk1X66VSO4sBo3wYeuU+6f6ml192PZ410A7TnANA9acf48j9hpMVPde9qdzR7zjXizTj99OyIe2zPpp7w==~-1~-1~-1; JSESSIONID=A7AA8C83F7CC67A9B47C9B92C9F99BF8; ak_bmsc=A7C1C100ED560BE876FCDAE73710841F0210AC95A747000097271F60DFE8AA1E~pl68DgIEfR2l9IkGxKD6UaertDEVywbFEx7CsigyMajudxYJXKwYAYqw7qwMt2fqmuqDfLZUBVCsDjdWwSQbeD7QvZRwa0CUmoVj3pGiakfaB13qqQU/hUq07XERw/zQgdxLBueXf42bNWiFRXIx5fSBGw99QZUJ9s2RQKTNVsuXSfDMfjqEDLQuEUowWe7c4j64exWYghPkWnGdseIKAlsCQGM2JTcDDZIiHI4bXsLkQ=; bm_sz=D3DCB6E4AB36B1178B7C685BC63512CE~YAAQlawQAo/hfmp3AQAAKaiyeQqgpQhOZl6Do12IzX/tjZsmPeczLqt2uPPjYmQsk/ed6okn8xHxfOY0uWG4pdRV6dS4sxC9HEXJZgJTY+JLbZ1YtFpKIPq3pxkT5jyDO4Wfqv6Go/xqmgqTlKlLSuApQCNaVNbcgEK8HsXd3bGxw7fqFTZdl4ZzOzVZ; X-CSRF-TOKEN=CfDJ8Jcj9GhlwkdBikuRYzfhrpKysqIEn8MO5u8x9DF4w3Ao6blGmse8gpH-3ALW2cTA7CFa3sJ2CrpkDtb717Ol9gAKYIxU8g3RD67QXVZLvs6WrtT26bNB-RjCKlg5RNfgO8cLZXmxAOM4DTLCcaylx8k; X-XSRF-TOKEN-ST=CfDJ8Jcj9GhlwkdBikuRYzfhrpIxpKQQdNg_5EBUQHz9XiJOkD-ERsDbVNO_jDh6AxZEeQ14MPvRF3iLuHQbjY4wi3vp-ncXV9AERxM1TrsjgfN2l_cn5dJcxV_fcHIeH3SsCLqU5WXPWfESe_b6d_Tf74Y; st_cur_page=st_trackdetails",
    "DNT": "1",
#    "Host": "www.ups.com",
#    "Origin": "https://www.ups.com",
    "Pragma": "no-cache",
    "Referer": "https://www.ups.com/track?loc=en_PL&tracknum=1ZWA87086796163221&requester=WT/trackdetails",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
#    "X-XSRF-TOKEN": "CfDJ8Jcj9GhlwkdBikuRYzfhrpIxpKQQdNg_5EBUQHz9XiJOkD-ERsDbVNO_jDh6AxZEeQ14MPvRF3iLuHQbjY4wi3vp-ncXV9AERxM1TrsjgfN2l_cn5dJcxV_fcHIeH3SsCLqU5WXPWfESe_b6d_Tf74Y",
}

payload = {
	"consumerHub": "",
	"Locale": "en_GB",
	"Requester": "wt",
	"TrackingNumber": [
		"1zwa87086796163221"
	]
}

url = 'https://www.ups.com/track/api/Track/GetStatus?loc=en_GB'

r = s.post(url, data=payload)
data = r.text
#data = r.json() 
print(data)
