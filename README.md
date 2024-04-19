
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-20 22:00:00 EEST+0300 2024-04-20 23:00:00 EEST+0300               7.852
	          2 2024-04-20 21:00:00 EEST+0300 2024-04-20 23:00:00 EEST+0300              7.8455
	          3 2024-04-20 21:00:00 EEST+0300 2024-04-21 00:00:00 EEST+0300               7.831
	          4 2024-04-20 20:00:00 EEST+0300 2024-04-21 00:00:00 EEST+0300             7.80825

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-20 15:00:00 EEST+0300 2024-04-20 16:00:00 EEST+0300               1.308
	          2 2024-04-20 14:00:00 EEST+0300 2024-04-20 16:00:00 EEST+0300              1.4185
	          3 2024-04-20 14:00:00 EEST+0300 2024-04-20 17:00:00 EEST+0300            1.703333
	          4 2024-04-20 13:00:00 EEST+0300 2024-04-20 17:00:00 EEST+0300              2.1755


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
