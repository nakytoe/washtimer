
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-13 08:00:00 EEST+0300 2024-06-13 09:00:00 EEST+0300              37.153
	          2 2024-06-13 07:00:00 EEST+0300 2024-06-13 09:00:00 EEST+0300             29.7415
	          3 2024-06-13 07:00:00 EEST+0300 2024-06-13 10:00:00 EEST+0300              25.969
	          4 2024-06-13 19:00:00 EEST+0300 2024-06-13 23:00:00 EEST+0300             24.0945

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-14 00:00:00 EEST+0300 2024-06-14 01:00:00 EEST+0300               5.013
	          2 2024-06-13 23:00:00 EEST+0300 2024-06-14 01:00:00 EEST+0300              6.2285
	          3 2024-06-13 22:00:00 EEST+0300 2024-06-14 01:00:00 EEST+0300              10.888
	          4 2024-06-13 21:00:00 EEST+0300 2024-06-14 01:00:00 EEST+0300            13.34975


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
