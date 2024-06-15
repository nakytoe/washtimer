
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-16 20:00:00 EEST+0300 2024-06-16 21:00:00 EEST+0300               4.693
	          2 2024-06-16 20:00:00 EEST+0300 2024-06-16 22:00:00 EEST+0300              4.6795
	          3 2024-06-16 20:00:00 EEST+0300 2024-06-16 23:00:00 EEST+0300            4.652667
	          4 2024-06-16 20:00:00 EEST+0300 2024-06-17 00:00:00 EEST+0300               4.609

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-16 13:00:00 EEST+0300 2024-06-16 14:00:00 EEST+0300              -0.089
	          2 2024-06-16 13:00:00 EEST+0300 2024-06-16 15:00:00 EEST+0300             -0.0845
	          3 2024-06-16 13:00:00 EEST+0300 2024-06-16 16:00:00 EEST+0300               -0.06
	          4 2024-06-16 12:00:00 EEST+0300 2024-06-16 16:00:00 EEST+0300             -0.0475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
