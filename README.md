
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-17 08:00:00 EEST+0300 2024-04-17 09:00:00 EEST+0300               20.57
	          2 2024-04-17 08:00:00 EEST+0300 2024-04-17 10:00:00 EEST+0300              19.675
	          3 2024-04-17 07:00:00 EEST+0300 2024-04-17 10:00:00 EEST+0300              17.638
	          4 2024-04-17 07:00:00 EEST+0300 2024-04-17 11:00:00 EEST+0300            16.35825

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-17 16:00:00 EEST+0300 2024-04-17 17:00:00 EEST+0300               7.357
	          2 2024-04-17 15:00:00 EEST+0300 2024-04-17 17:00:00 EEST+0300               7.378
	          3 2024-04-17 15:00:00 EEST+0300 2024-04-17 18:00:00 EEST+0300            7.486333
	          4 2024-04-17 15:00:00 EEST+0300 2024-04-17 19:00:00 EEST+0300                7.63


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
