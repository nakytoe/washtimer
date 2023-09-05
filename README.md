
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-06 20:00:00 EEST+0300 2023-09-06 21:00:00 EEST+0300              23.502
	          2 2023-09-06 20:00:00 EEST+0300 2023-09-06 22:00:00 EEST+0300             22.0455
	          3 2023-09-06 19:00:00 EEST+0300 2023-09-06 22:00:00 EEST+0300           20.724667
	          4 2023-09-06 18:00:00 EEST+0300 2023-09-06 22:00:00 EEST+0300             18.8255

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-06 04:00:00 EEST+0300 2023-09-06 05:00:00 EEST+0300              -0.442
	          2 2023-09-06 03:00:00 EEST+0300 2023-09-06 05:00:00 EEST+0300             -0.3375
	          3 2023-09-06 03:00:00 EEST+0300 2023-09-06 06:00:00 EEST+0300           -0.293667
	          4 2023-09-06 02:00:00 EEST+0300 2023-09-06 06:00:00 EEST+0300             -0.2715


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
