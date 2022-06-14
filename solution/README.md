# Raízen Data Engineering Test

## [The Problem](https://github.com/audreyemmely/data-engineering-test/blob/master/TEST.md)

<img src="https://media.giphy.com/media/3oEjHWzZQaCrZW2aWs/giphy.gif" />

## [The Solution](https://github.com/audreyemmely/data-engineering-test/blob/master/solution/main.py)
<img src="https://media.giphy.com/media/BpGWitbFZflfSUYuZ9/giphy.gif" width="350" height="280" />
<img align = "right" src="https://media.giphy.com/media/VEsfbW0pBu145PPhOi/giphy.gif" width="350" height="280" />

I thought about doing the test using Pentaho tool, but I wanted to challenge myself by trying to do everything using only python[^1] and pandas library[^2], so I programmed it as if I built the data pipeline through Pentaho.

I did a quick data exploration in the dataset and tested most of my theories in [this notebook](https://github.com/audreyemmely/data-engineering-test/blob/master/solution/exploring_data.ipynb).

First I renamed the columns (Select values step), then I unpivoted the table[^3] (Row Normaliser step), with that I concatenated the year column with the month column (Concat fields step), after that I deleted some values and columns that will no longer be used and renamed it to the naming pattern that was requested, changed states names to uf abbreviation, formatted[^4][^5] the "combustivel" column, and reordered[^6] the columns (Select values step), added the "unit" column (Add constants step), finally, I saved the file in csv format (Text file output step).

<br/>

<img src="https://media.giphy.com/media/GfaZNzU42Snz6dlGhN/giphy.gif" width="350" height="280"/> 

### What about the choosed database? 

PostgreSQL continues to be more efficient than some databases in many ways. It has a sophisticated locking mechanism (MVCC), supports unlimited sizes of rows, databases and tables (up to 16TB), accepts several types of sub-queries, has more data types and has a good FAILSAVE mechanism (Failsafe, e.g. sudden system shutdown). For very large, complex databases that require reliability and scalability, PostgreSQL is worth using. In addition to being offered many modern features, such as:

* complex commands
* foreign keys
* triggers
* visions
* transactional integrity
* multiversion concurrency control

Due to its liberal license, PostgreSQL can be used, modified and distributed by anyone for any purpose, whether private, commercial or academic, free of charge.

Obviously I don't know all this off the top of my head, but I did a brief google search to bring this information up. But I already use this database in my private projects at university.

<br/>

### And what were the difficulties?

<img align = 'right' src="https://media.giphy.com/media/l0K3Z4QU2TLMsw4sE/giphy.gif" width="400" height="220"/>

1. When I tried to read the xls file, I couldn't see the cache pages, I tried to convert to xlsx and it didn't work either, in the end I decided to convert to ods and I could see everything.
To solve this I googled how to covert from xls to ods and I found [this tutorial](https://ask.libreoffice.org/t/convert-to-command-line-parameter/840).

2. When processing the data I didn't know how to unpivot through python, but doing research I found the ```melt``` [function](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) in the pandas library that can perform this operation.

<br/>

### Let's go to the point... how do you run this on your machine?
First of all, [download](https://www.python.org/downloads/) and install python (preferably the [same one](#version) I used) on your machine.

Now clone this repository by typing the following command in your terminal:

```
git clone https://github.com/audreyemmely/data-engineering-test.git
```

Create a database with a schema called ```anp``` or change the settings inside the file ```create_insert_sql.py```, which is in the ```solution``` folder, to whatever you want.

Inside the ```data-engineering-test``` folder create an ```.env``` file with the following variables from your database:

```
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_PORT=
```

After that, open the folder ```data-engineering-test/solution``` in your terminal and run the command ```pip install -r requirements.txt``` to install the required libraries.

Finally, run the program using the following command:

```
python3 main.py
```

Now you can access your database and see the data in the ```dim_anp_diesel``` and ```dim_anp_fuel``` tables.

![table1](https://github.com/audreyemmely/data-engineering-test/blob/master/images/prints/dados%20diesel.png?raw=true)

![table2](https://github.com/audreyemmely/data-engineering-test/blob/master/images/prints/dados%20fuel.png?raw=true)

<p align='center'>
<img src="https://media.giphy.com/media/l4JySAWfMaY7w88sU/giphy.gif"/>
</p>

If you want, [here](https://github.com/audreyemmely/data-engineering-test/tree/master/images/prints) are some screenshots of my screen to compare with your results!

### <a name="version"></a> 🛠️ Technologies used:

Python 3.9.12

PostgreSQL 14.3

DBeaver 22.0.5

Anaconda Navigator 2.1.4

[^1]: [Python 3.9 Documentation](https://docs.python.org/3.9/).
[^2]: [Pandas Documentation](https://pandas.pydata.org/docs/).
[^3]: [How to Unpivot a Pandas DataFrame (With Example)](https://www.statology.org/pandas-unpivot/#:~:text=In%20pandas%2C%20you%20can%20use,col3'%2C%20...%5D).
[^4]: [Removing characters from columns in Pandas DataFrame](https://www.skytowner.com/explore/removing_characters_from_columns_in_pandas_dataframe).
[^5]: [How to remove accents from values in columns?](https://stackoverflow.com/questions/37926248/how-to-remove-accents-from-values-in-columns).
[^6]: [Como mudar a ordem das colunas Pandas DataFrame](https://www.delftstack.com/pt/howto/python-pandas/how-to-change-the-order-of-dataframe-columns/).
