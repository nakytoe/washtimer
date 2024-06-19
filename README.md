
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-20 09:00:00 EEST+0300 2024-06-20 10:00:00 EEST+0300               2.856
	          2 2024-06-20 09:00:00 EEST+0300 2024-06-20 11:00:00 EEST+0300              2.5975
	          3 2024-06-20 08:00:00 EEST+0300 2024-06-20 11:00:00 EEST+0300            2.401333
	          4 2024-06-19 16:00:00 EEST+0300 2024-06-19 20:00:00 EEST+0300               2.327

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-20 04:00:00 EEST+0300 2024-06-20 05:00:00 EEST+0300              -0.825
	          2 2024-06-20 03:00:00 EEST+0300 2024-06-20 05:00:00 EEST+0300             -0.6625
	          3 2024-06-20 03:00:00 EEST+0300 2024-06-20 06:00:00 EEST+0300              -0.525
	          4 2024-06-20 02:00:00 EEST+0300 2024-06-20 06:00:00 EEST+0300            -0.43775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
