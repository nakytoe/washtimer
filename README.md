
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-26 12:00:00 EEST+0300 2024-04-26 13:00:00 EEST+0300              25.114
	          2 2024-04-26 12:00:00 EEST+0300 2024-04-26 14:00:00 EEST+0300             24.2185
	          3 2024-04-26 11:00:00 EEST+0300 2024-04-26 14:00:00 EEST+0300               21.93
	          4 2024-04-26 10:00:00 EEST+0300 2024-04-26 14:00:00 EEST+0300             20.0125

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-26 15:00:00 EEST+0300 2024-04-26 16:00:00 EEST+0300               8.106
	          2 2024-04-26 14:00:00 EEST+0300 2024-04-26 16:00:00 EEST+0300               8.315
	          3 2024-04-26 14:00:00 EEST+0300 2024-04-26 17:00:00 EEST+0300            8.433333
	          4 2024-04-26 14:00:00 EEST+0300 2024-04-26 18:00:00 EEST+0300             8.54775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
