from binance.client import Client
import pandas as pd
api_key = "JBLwXP8CwQxAJzIT5ZH8l5iQgxnWeg7TiiQsDYMxP9NcrUEn5P2MKUlMZTNJPwt1"
api_secret = "vHC9cnCEIYq6qRQQRPWqOreGs4PpGF2JrAClezhnZKidDd3R28jLvNuP4foRW3jo"
client = Client(api_key, api_secret)

klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Sep, 2019", "30 Oct, 2019")
dflist=klines
df=pd.DataFrame(dflist)
print (df)
mode1='w'
filename='day'
with open('/home/sf/test/log2/'+filename+'.csv',mode1) as f:
     df.to_csv(f,index=False,header=False)
