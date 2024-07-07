
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-08 19:00:00 EEST+0300 2024-07-08 20:00:00 EEST+0300               2.518
	          2 2024-07-08 19:00:00 EEST+0300 2024-07-08 21:00:00 EEST+0300              2.4725
	          3 2024-07-08 18:00:00 EEST+0300 2024-07-08 21:00:00 EEST+0300            2.414667
	          4 2024-07-08 18:00:00 EEST+0300 2024-07-08 22:00:00 EEST+0300                2.35

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-07 16:00:00 EEST+0300 2024-07-07 17:00:00 EEST+0300               -1.22
	          2 2024-07-08 02:00:00 EEST+0300 2024-07-08 04:00:00 EEST+0300                -1.0
	          3 2024-07-08 02:00:00 EEST+0300 2024-07-08 05:00:00 EEST+0300                -1.0
	          4 2024-07-08 02:00:00 EEST+0300 2024-07-08 06:00:00 EEST+0300             -0.9985


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
