from tqdm import tqdm
import pandas as pd
import akshare as ak
from sqlalchemy import create_engine

class stock_data_cn(object):

	def init(self, db_user:str="user", db_passwd:str="password", db_addr:str="localhost:3306/stock"):
		'''
		db_user: username 
		db_passwd: password
		df_addr: <IP>:<PORT>/<database>
		'''
		self.db = create_engine("mysql+pymysql://{}:{}@{}".format(db_user, db_passwd, db_addr), echo=False)
		self.cn_stock_list = pd.read_excel("../data/cnstock.xlsx", dtype=str)
		self.cn_stock_list.to_sql("code", self.db, if_exists="replace", index=False)

	def market_data(self):
		print("[+] update market data")
		code = self.cn_stock_list
		for i in tqdm(range(1666, len(code))):
			tmp_data = ak.stock_zh_index_daily(symbol="{}{}".format(code['市场'][i].lower(), code['代码'][i]))
			tmp_data["code"] = [code['代码'][i] for j in range(len(tmp_data))]
			if code['市场'][i] == 'SH':
				tmp_data.to_sql("stock_price_sh", self.db, if_exists="append", index=False)
			elif code['市场'][i] == 'SZ':
				tmp_data.to_sql("stock_price_sz", self.db, if_exists="append", index=False)
			else:
				pass

		print("[:)] Done")

	def market_heat(self):
		print("[+] update breaking info")
		code = self.cn_stock_list
		try:
			stock_hot_xueqiu = ak.stock_hot_follow_xq(symbol="最热门")
			stock_hot_xueqiu[['代码', '市场']] = hot_follow_xueqiu['股票代码'].str.extract('(?:([a-zA-Z]+)?(?:(.*\d)))?')
			stock_hot_xueqiu.drop(['股票代码', '最新价'], axis=1, replace=True)
			stock_hot_xueqiu.to_sql("stock_hot", self.db, if_exists="replace", index=False)
		except:
			pass
		try:
			concept_hot = ak.stock_board_concept_name_em()
			concept_hot.to_sql("concept_board_hot", self.db, if_exists="replace", index=False)
		except:
			pass
		try:
			industry_hot = ak.stock_board_industry_name_em()
			industry_hot.to_sql("industry_board_hot", self.db, if_exists="replace", index=False)
		except:
			pass
	
	def news(self):
		print("[+] news")
		code = self.cn_stock_list
		tmp_data_news_real = ak.js_news(timestamp="{}".format(pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")))
		tmp_data_news_real.to_sql("stock_news_real", self.db, if_exists="replace", index=False)
		for i in tqdm(range(0, len(code))):
			tmp_data = ak.stock_news_em(symbol="{}".format(code['代码'][i]))
			tmp_data.to_sql("stock_news_individual", self.db, if_exists="append", index=False)


if __name__ == "__main__":
	a = stock_data_cn()
	a.init()
	a.market_data()
	a.market_heat()
	a.news()