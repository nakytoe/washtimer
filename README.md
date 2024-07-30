
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-30 10:00:00 EEST+0300 2024-07-30 11:00:00 EEST+0300               2.905
	          2 2024-07-30 09:00:00 EEST+0300 2024-07-30 11:00:00 EEST+0300              2.8915
	          3 2024-07-30 08:00:00 EEST+0300 2024-07-30 11:00:00 EEST+0300            2.835333
	          4 2024-07-30 08:00:00 EEST+0300 2024-07-30 12:00:00 EEST+0300              2.7465

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-30 14:00:00 EEST+0300 2024-07-30 15:00:00 EEST+0300               0.001
	          2 2024-07-30 14:00:00 EEST+0300 2024-07-30 16:00:00 EEST+0300               0.053
	          3 2024-07-30 13:00:00 EEST+0300 2024-07-30 16:00:00 EEST+0300            0.080333
	          4 2024-07-30 12:00:00 EEST+0300 2024-07-30 16:00:00 EEST+0300             0.30325


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
