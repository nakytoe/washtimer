
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-21 20:00:00 EEST+0300 2024-06-21 21:00:00 EEST+0300                 0.5
	          2 2024-06-21 20:00:00 EEST+0300 2024-06-21 22:00:00 EEST+0300              0.3475
	          3 2024-06-20 20:00:00 EEST+0300 2024-06-20 23:00:00 EEST+0300            0.305667
	          4 2024-06-20 19:00:00 EEST+0300 2024-06-20 23:00:00 EEST+0300             0.27575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-21 04:00:00 EEST+0300 2024-06-21 05:00:00 EEST+0300              -0.658
	          2 2024-06-21 03:00:00 EEST+0300 2024-06-21 05:00:00 EEST+0300             -0.5795
	          3 2024-06-21 03:00:00 EEST+0300 2024-06-21 06:00:00 EEST+0300               -0.47
	          4 2024-06-21 02:00:00 EEST+0300 2024-06-21 06:00:00 EEST+0300            -0.41325


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
