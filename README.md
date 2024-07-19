
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-19 20:00:00 EEST+0300 2024-07-19 21:00:00 EEST+0300               2.833
	          2 2024-07-19 19:00:00 EEST+0300 2024-07-19 21:00:00 EEST+0300               2.804
	          3 2024-07-19 18:00:00 EEST+0300 2024-07-19 21:00:00 EEST+0300            2.766333
	          4 2024-07-19 18:00:00 EEST+0300 2024-07-19 22:00:00 EEST+0300               2.734

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-20 00:00:00 EEST+0300 2024-07-20 01:00:00 EEST+0300               2.081
	          2 2024-07-19 23:00:00 EEST+0300 2024-07-20 01:00:00 EEST+0300               2.222
	          3 2024-07-19 22:00:00 EEST+0300 2024-07-20 01:00:00 EEST+0300            2.319667
	          4 2024-07-19 21:00:00 EEST+0300 2024-07-20 01:00:00 EEST+0300               2.399


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
