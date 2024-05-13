
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-13 20:00:00 EEST+0300 2024-05-13 21:00:00 EEST+0300              29.759
	          2 2024-05-13 19:00:00 EEST+0300 2024-05-13 21:00:00 EEST+0300              27.298
	          3 2024-05-13 18:00:00 EEST+0300 2024-05-13 21:00:00 EEST+0300           24.660333
	          4 2024-05-13 18:00:00 EEST+0300 2024-05-13 22:00:00 EEST+0300              23.145

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-15 00:00:00 EEST+0300 2024-05-15 01:00:00 EEST+0300              -0.101
	          2 2024-05-14 23:00:00 EEST+0300 2024-05-15 01:00:00 EEST+0300              -0.054
	          3 2024-05-14 22:00:00 EEST+0300 2024-05-15 01:00:00 EEST+0300              -0.026
	          4 2024-05-14 21:00:00 EEST+0300 2024-05-15 01:00:00 EEST+0300             0.03325


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
