
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
	          1 2024-06-21 16:00:00 EEST+0300 2024-06-21 17:00:00 EEST+0300                -0.1
	          2 2024-06-21 16:00:00 EEST+0300 2024-06-21 18:00:00 EEST+0300              -0.055
	          3 2024-06-21 16:00:00 EEST+0300 2024-06-21 19:00:00 EEST+0300              -0.037
	          4 2024-06-21 16:00:00 EEST+0300 2024-06-21 20:00:00 EEST+0300             -0.0275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
