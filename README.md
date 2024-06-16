
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-17 20:00:00 EEST+0300 2024-06-17 21:00:00 EEST+0300              16.736
	          2 2024-06-17 19:00:00 EEST+0300 2024-06-17 21:00:00 EEST+0300               14.86
	          3 2024-06-17 18:00:00 EEST+0300 2024-06-17 21:00:00 EEST+0300           13.217333
	          4 2024-06-17 12:00:00 EEST+0300 2024-06-17 16:00:00 EEST+0300             11.8225

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-16 16:00:00 EEST+0300 2024-06-16 17:00:00 EEST+0300                 0.0
	          2 2024-06-16 16:00:00 EEST+0300 2024-06-16 18:00:00 EEST+0300              0.4155
	          3 2024-06-16 16:00:00 EEST+0300 2024-06-16 19:00:00 EEST+0300               1.277
	          4 2024-06-16 16:00:00 EEST+0300 2024-06-16 20:00:00 EEST+0300             2.03775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
