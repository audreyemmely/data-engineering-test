# Raízen Data Engineering Test

## [The Problem](https://github.com/audreyemmely/data-engineering-test/blob/master/TEST.md)

<img src="https://media.giphy.com/media/3oEjHWzZQaCrZW2aWs/giphy.gif" />

## The Solution

<img src="https://media.giphy.com/media/BpGWitbFZflfSUYuZ9/giphy.gif" width="350" height="280" />
<img align = "right" src="https://media.giphy.com/media/VEsfbW0pBu145PPhOi/giphy.gif" width="350" height="280" />

<br/>

I thought about doing the test using the Pentaho tool, but I wanted to challenge myself by trying to do everything using only python[^1] and pandas library[^2], so I programmed it as if I built the data pipeline through Pentaho.

I did a quick data exploration in the dataset and tested most of my theories in [this notebook](https://github.com/audreyemmely/data-engineering-test/blob/master/solution/exploring_data.ipynb).

First I renamed the columns (Select values step), then I unpivoted the table[^3] (Normaliser step), with that I concatenated the year column with the month column (Concat fields step), after that I deleted some values and columns that will no longer be used and renamed it to the naming pattern that was requested, formatted[^4][^5] the "combustivel" and "estado" columns, and reordered[^6] the columns (Select values step), added the "unit" column (Add constants step), finally, I saved the file in csv format (Text file output step).

<br/>
<br/>

<img src="https://media.giphy.com/media/GfaZNzU42Snz6dlGhN/giphy.gif" width="350" height="280"/> 

### And what about the choosed database? 

PostgreSQL continues to be more efficient than some databases in many ways. It has a sophisticated locking mechanism (MVCC), supports unlimited sizes of rows, databases and tables (up to 16TB), accepts several types of sub-queries, has more data types and has a good FAILSAVE mechanism (Failsafe, e.g. sudden system shutdown). For very large, complex databases that require reliability and scalability, PostgreSQL is worth using. In addition to being offered many modern features, such as:

* complex commands
* foreign keys
* triggers
* visions
* transactional integrity
* multiversion concurrency control

Due to its liberal license, PostgreSQL can be used, modified and distributed by anyone for any purpose, whether private, commercial or academic, free of charge.

Obviously I don't know all this off the top of my head, but I did a brief google search to bring this information up. But I already use this database in my private projects at university.

### And what were the difficulties?

<img src="https://media.giphy.com/media/l0K3Z4QU2TLMsw4sE/giphy.gif" width="400" height="250"/>


When I tried to read the xls file, I couldn't see the cache pages, I tried to convert to xlsx and it didn't work either, in the end I decided to convert to ods and I could see everything.
To solve this I typed the following command in terminal[^7]:

```
soffice --headless --convert-to ods /assets/vendas-combustiveis-m3.xls --outdir /assets
```
[^1]: [Python 3.8 Documentation](https://docs.python.org/3.8/).
[^2]: [Pandas Documentation](https://pandas.pydata.org/docs/).
[^3]: [How to Unpivot a Pandas DataFrame (With Example)](https://www.statology.org/pandas-unpivot/#:~:text=In%20pandas%2C%20you%20can%20use,col3'%2C%20...%5D).
[^4]: [Removing characters from columns in Pandas DataFrame](https://www.skytowner.com/explore/removing_characters_from_columns_in_pandas_dataframe).
[^5]: [How to remove accents from values in columns?](https://stackoverflow.com/questions/37926248/how-to-remove-accents-from-values-in-columns).
[^6]: [Como mudar a ordem das colunas Pandas DataFrame](https://www.delftstack.com/pt/howto/python-pandas/how-to-change-the-order-of-dataframe-columns/).
[^7]: [Convert-to command line parameter](https://ask.libreoffice.org/t/convert-to-command-line-parameter/840).
