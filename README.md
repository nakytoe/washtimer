
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-18 17:00:00 EEST+0300 2023-09-18 18:00:00 EEST+0300               1.199
	          2 2023-09-18 17:00:00 EEST+0300 2023-09-18 19:00:00 EEST+0300              1.1875
	          3 2023-09-18 16:00:00 EEST+0300 2023-09-18 19:00:00 EEST+0300            1.167333
	          4 2023-09-18 16:00:00 EEST+0300 2023-09-18 20:00:00 EEST+0300             1.14175

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-20 00:00:00 EEST+0300 2023-09-20 01:00:00 EEST+0300              -0.196
	          2 2023-09-19 15:00:00 EEST+0300 2023-09-19 17:00:00 EEST+0300              -0.188
	          3 2023-09-19 14:00:00 EEST+0300 2023-09-19 17:00:00 EEST+0300           -0.170667
	          4 2023-09-19 13:00:00 EEST+0300 2023-09-19 17:00:00 EEST+0300             -0.1515


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
