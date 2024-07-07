
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-07 08:00:00 EEST+0300 2024-07-07 09:00:00 EEST+0300              -0.059
	          2 2024-07-07 08:00:00 EEST+0300 2024-07-07 10:00:00 EEST+0300               -0.06
	          3 2024-07-07 07:00:00 EEST+0300 2024-07-07 10:00:00 EEST+0300              -0.067
	          4 2024-07-07 07:00:00 EEST+0300 2024-07-07 11:00:00 EEST+0300              -0.212

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-07 15:00:00 EEST+0300 2024-07-07 16:00:00 EEST+0300               -1.99
	          2 2024-07-07 14:00:00 EEST+0300 2024-07-07 16:00:00 EEST+0300              -1.746
	          3 2024-07-07 13:00:00 EEST+0300 2024-07-07 16:00:00 EEST+0300           -1.613667
	          4 2024-07-07 13:00:00 EEST+0300 2024-07-07 17:00:00 EEST+0300            -1.51525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
