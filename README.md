
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-24 20:00:00 EEST+0300 2024-07-24 21:00:00 EEST+0300              12.399
	          2 2024-07-24 19:00:00 EEST+0300 2024-07-24 21:00:00 EEST+0300              9.9875
	          3 2024-07-24 18:00:00 EEST+0300 2024-07-24 21:00:00 EEST+0300            8.643667
	          4 2024-07-24 17:00:00 EEST+0300 2024-07-24 21:00:00 EEST+0300               8.374

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-24 01:00:00 EEST+0300 2024-07-24 02:00:00 EEST+0300               1.938
	          2 2024-07-24 01:00:00 EEST+0300 2024-07-24 03:00:00 EEST+0300               1.956
	          3 2024-07-24 01:00:00 EEST+0300 2024-07-24 04:00:00 EEST+0300            2.089333
	          4 2024-07-24 01:00:00 EEST+0300 2024-07-24 05:00:00 EEST+0300             2.14875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
