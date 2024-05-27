
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-28 09:00:00 EEST+0300 2024-05-28 10:00:00 EEST+0300               1.936
	          2 2024-05-28 09:00:00 EEST+0300 2024-05-28 11:00:00 EEST+0300              1.8385
	          3 2024-05-28 08:00:00 EEST+0300 2024-05-28 11:00:00 EEST+0300               1.752
	          4 2024-05-28 08:00:00 EEST+0300 2024-05-28 12:00:00 EEST+0300              1.5675

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-28 04:00:00 EEST+0300 2024-05-28 05:00:00 EEST+0300              -0.201
	          2 2024-05-28 03:00:00 EEST+0300 2024-05-28 05:00:00 EEST+0300             -0.2005
	          3 2024-05-28 02:00:00 EEST+0300 2024-05-28 05:00:00 EEST+0300           -0.191333
	          4 2024-05-28 01:00:00 EEST+0300 2024-05-28 05:00:00 EEST+0300            -0.16925


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
