
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-21 21:00:00 EEST+0300 2024-04-21 22:00:00 EEST+0300              11.812
	          2 2024-04-21 21:00:00 EEST+0300 2024-04-21 23:00:00 EEST+0300             11.5525
	          3 2024-04-21 20:00:00 EEST+0300 2024-04-21 23:00:00 EEST+0300           11.395333
	          4 2024-04-21 20:00:00 EEST+0300 2024-04-22 00:00:00 EEST+0300               11.17

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-20 16:00:00 EEST+0300 2024-04-20 17:00:00 EEST+0300               2.273
	          2 2024-04-20 16:00:00 EEST+0300 2024-04-20 18:00:00 EEST+0300               3.456
	          3 2024-04-20 16:00:00 EEST+0300 2024-04-20 19:00:00 EEST+0300            4.089333
	          4 2024-04-20 16:00:00 EEST+0300 2024-04-20 20:00:00 EEST+0300              4.5335


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
