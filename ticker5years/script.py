import twint
import nest_asyncio
nest_asyncio.apply()
five_years_weekly_dates = ['2016-11-20', '2016-11-27', '2016-12-04', '2016-12-11', '2016-12-18', '2016-12-25', '2017-01-01', '2017-01-08', '2017-01-15', '2017-01-22', '2017-01-29', '2017-02-05', '2017-02-12', '2017-02-19', '2017-02-26', '2017-03-05', '2017-03-12', '2017-03-19', '2017-03-26', '2017-04-02', '2017-04-09', '2017-04-16', '2017-04-23', '2017-04-30', '2017-05-07', '2017-05-14', '2017-05-21', '2017-05-28', '2017-06-04', '2017-06-11', '2017-06-18', '2017-06-25', '2017-07-02', '2017-07-09', '2017-07-16', '2017-07-23', '2017-07-30', '2017-08-06', '2017-08-13', '2017-08-20', '2017-08-27', '2017-09-03', '2017-09-10', '2017-09-17', '2017-09-24', '2017-10-01', '2017-10-08', '2017-10-15', '2017-10-22', '2017-10-29', '2017-11-05', '2017-11-12', '2017-11-19', '2017-11-26', '2017-12-03', '2017-12-10', '2017-12-17', '2017-12-24', '2017-12-31', '2018-01-07', '2018-01-14', '2018-01-21', '2018-01-28', '2018-02-04', '2018-02-11', '2018-02-18', '2018-02-25', '2018-03-04', '2018-03-11', '2018-03-18', '2018-03-25', '2018-04-01', '2018-04-08', '2018-04-15', '2018-04-22', '2018-04-29', '2018-05-06', '2018-05-13', '2018-05-20', '2018-05-27', '2018-06-03', '2018-06-10', '2018-06-17', '2018-06-24', '2018-07-01', '2018-07-08', '2018-07-15', '2018-07-22', '2018-07-29', '2018-08-05', '2018-08-12', '2018-08-19', '2018-08-26', '2018-09-02', '2018-09-09', '2018-09-16', '2018-09-23', '2018-09-30', '2018-10-07', '2018-10-14', '2018-10-21', '2018-10-28', '2018-11-04', '2018-11-11', '2018-11-18', '2018-11-25', '2018-12-02', '2018-12-09', '2018-12-16', '2018-12-23', '2018-12-30', '2019-01-06', '2019-01-13', '2019-01-20', '2019-01-27', '2019-02-03', '2019-02-10', '2019-02-17', '2019-02-24', '2019-03-03', '2019-03-10', '2019-03-17', '2019-03-24', '2019-03-31', '2019-04-07', '2019-04-14', '2019-04-21', '2019-04-28', '2019-05-05', '2019-05-12', '2019-05-19', '2019-05-26', '2019-06-02', '2019-06-09', '2019-06-16', '2019-06-23', '2019-06-30', '2019-07-07', '2019-07-14', '2019-07-21', '2019-07-28', '2019-08-04', '2019-08-11', '2019-08-18', '2019-08-25', '2019-09-01', '2019-09-08', '2019-09-15', '2019-09-22', '2019-09-29', '2019-10-06', '2019-10-13', '2019-10-20', '2019-10-27', '2019-11-03', '2019-11-10', '2019-11-17', '2019-11-24', '2019-12-01', '2019-12-08', '2019-12-15', '2019-12-22', '2019-12-29', '2020-01-05', '2020-01-12', '2020-01-19', '2020-01-26', '2020-02-02', '2020-02-09', '2020-02-16', '2020-02-23', '2020-03-01', '2020-03-08', '2020-03-15', '2020-03-22', '2020-03-29', '2020-04-05', '2020-04-12', '2020-04-19', '2020-04-26', '2020-05-03', '2020-05-10', '2020-05-17', '2020-05-24', '2020-05-31', '2020-06-07', '2020-06-14', '2020-06-21', '2020-06-28', '2020-07-05', '2020-07-12', '2020-07-19', '2020-07-26', '2020-08-02', '2020-08-09', '2020-08-16', '2020-08-23', '2020-08-30', '2020-09-06', '2020-09-13', '2020-09-20', '2020-09-27', '2020-10-04', '2020-10-11', '2020-10-18', '2020-10-25', '2020-11-01', '2020-11-08', '2020-11-15', '2020-11-22', '2020-11-29', '2020-12-06', '2020-12-13', '2020-12-20', '2020-12-27', '2021-01-03', '2021-01-10', '2021-01-17', '2021-01-24', '2021-01-31', '2021-02-07', '2021-02-14', '2021-02-21', '2021-02-28', '2021-03-07', '2021-03-14', '2021-03-21', '2021-03-28', '2021-04-04', '2021-04-11', '2021-04-18', '2021-04-25', '2021-05-02', '2021-05-09', '2021-05-16', '2021-05-23', '2021-05-30', '2021-06-06', '2021-06-13', '2021-06-20', '2021-06-27', '2021-07-04', '2021-07-11', '2021-07-18', '2021-07-25', '2021-08-01', '2021-08-08', '2021-08-15', '2021-08-22', '2021-08-29', '2021-09-05', '2021-09-12', '2021-09-19', '2021-09-26', '2021-10-03', '2021-10-10', '2021-10-17', '2021-10-24', '2021-10-31', '2021-11-07', '2021-11-14']
for i in range(len(five_years_weekly_dates)-1):
    filename = five_years_weekly_dates[i]+"_"+five_years_weekly_dates[i+1]+".csv"
    config = twint.Config()
    config.Search = '$TSLA'
    config.Lang = 'en'
    config.Limit = 1000
    config.Filter_retweets = True
    config.Since = five_years_weekly_dates[i]
    config.Until = five_years_weekly_dates[i+1]
    config.Custom['tweet'] = ['id', 'date', 'time', 'tweet', 'likes_count', 'replies_count', 'retweets_count', 'hashtags']
    config.Store_json = True
    config.Output = filename
    twint.run.Search(config)