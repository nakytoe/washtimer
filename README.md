
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-22 19:00:00 EEST+0300 2024-06-22 20:00:00 EEST+0300               4.537
	          2 2024-06-22 19:00:00 EEST+0300 2024-06-22 21:00:00 EEST+0300              4.5125
	          3 2024-06-22 19:00:00 EEST+0300 2024-06-22 22:00:00 EEST+0300            4.480667
	          4 2024-06-22 18:00:00 EEST+0300 2024-06-22 22:00:00 EEST+0300               4.448

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-22 14:00:00 EEST+0300 2024-06-22 15:00:00 EEST+0300               0.012
	          2 2024-06-22 14:00:00 EEST+0300 2024-06-22 16:00:00 EEST+0300              0.0195
	          3 2024-06-22 13:00:00 EEST+0300 2024-06-22 16:00:00 EEST+0300            0.125333
	          4 2024-06-22 12:00:00 EEST+0300 2024-06-22 16:00:00 EEST+0300              0.2085


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
