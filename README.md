
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-08 08:00:00 EEST+0300 2023-08-08 09:00:00 EEST+0300              -0.013
	          2 2023-08-08 08:00:00 EEST+0300 2023-08-08 10:00:00 EEST+0300             -0.0355
	          3 2023-08-08 07:00:00 EEST+0300 2023-08-08 10:00:00 EEST+0300               -0.08
	          4 2023-08-08 07:00:00 EEST+0300 2023-08-08 11:00:00 EEST+0300            -0.12575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-08 16:00:00 EEST+0300 2023-08-08 17:00:00 EEST+0300               -1.16
	          2 2023-08-08 15:00:00 EEST+0300 2023-08-08 17:00:00 EEST+0300             -1.0805
	          3 2023-08-08 14:00:00 EEST+0300 2023-08-08 17:00:00 EEST+0300           -0.946333
	          4 2023-08-08 13:00:00 EEST+0300 2023-08-08 17:00:00 EEST+0300            -0.86525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
