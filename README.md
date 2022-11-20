# hackathon-2022

## TOPIC

> 峰悦交易看板选题背景：资本市场瞬息万变，从**宏观经济、行业动态到公司财务信息、重大变动**等各种情况均会对交易产生影响。
> 题目要求：做一个“峰悦交易看板”，能实时的将全球各市场的财经信息抓取-分类-可视化呈现；或能针对峰悦资本投资方向，将全球行业动态、市场规模预测、相关科技突破等投资人关注信息进行**抓取-分类-可视化呈现**。分类板块不低于3个板块评价重点：**分类准确度、看板可视化效果、操作流畅度、实用性**等。

## Idea

Basically, this topic is focusing on macro/micro-economic data, financial data, and news(text information). Three main components:

1. Market information:
	* Market Data 
	* Related News: Named Entity Recognition, WordCloud, Sentiment Analysis
2. Sectors Information:
	* Indicators
	* Related News: Named Entity Recognition, WordCloud, Sentiment Analysis
3. Main economic performance:
	* Indicators
	* Economic Calendar 

## Tech-Stack

* Data Crawling: `python` For the data crawling and sorting
* Data Storage: `MySQL`
* Frontend (Visualization Dashboard): Grafana 
