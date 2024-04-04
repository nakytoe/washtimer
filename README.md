
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-04 09:00:00 EEST+0300 2024-04-04 10:00:00 EEST+0300              30.995
	          2 2024-04-04 08:00:00 EEST+0300 2024-04-04 10:00:00 EEST+0300             30.9915
	          3 2024-04-04 08:00:00 EEST+0300 2024-04-04 11:00:00 EEST+0300           23.967333
	          4 2024-04-04 07:00:00 EEST+0300 2024-04-04 11:00:00 EEST+0300            20.36025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-05 00:00:00 EEST+0300 2024-04-05 01:00:00 EEST+0300               6.944
	          2 2024-04-04 23:00:00 EEST+0300 2024-04-05 01:00:00 EEST+0300               7.019
	          3 2024-04-04 22:00:00 EEST+0300 2024-04-05 01:00:00 EEST+0300               7.157
	          4 2024-04-04 21:00:00 EEST+0300 2024-04-05 01:00:00 EEST+0300               7.469


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
