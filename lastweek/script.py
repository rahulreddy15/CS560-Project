import twint
import nest_asyncio
nest_asyncio.apply()

last_week = ['2021-11-30','2021-12-01', '2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05', '2021-12-06','2021-12-07']
for i in range(len(last_week)-1):
    	filename = last_week[i]+"_"+last_week[i+1]+".csv"
    	config = twint.Config()
    	config.Search = "tsla"
    	config.Lang = 'en'
    	config.Limit = 500
    	config.Filter_retweets = True
    	config.Since = last_week[i]
    	config.Until = last_week[i+1]
    	config.Custom['tweet'] = ['id', 'date', 'time', 'tweet', 'likes_count', 'replies_count', 'retweets_count', 'hashtags']
    	config.Store_json = True
    	config.Output = filename
    	twint.run.Search(config)
