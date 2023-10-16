
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-17 09:00:00 EEST+0300 2023-10-17 10:00:00 EEST+0300                23.7
	          2 2023-10-17 08:00:00 EEST+0300 2023-10-17 10:00:00 EEST+0300              22.787
	          3 2023-10-17 08:00:00 EEST+0300 2023-10-17 11:00:00 EEST+0300              21.768
	          4 2023-10-17 07:00:00 EEST+0300 2023-10-17 11:00:00 EEST+0300               21.17

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-16 17:00:00 EEST+0300 2023-10-16 18:00:00 EEST+0300               0.304
	          2 2023-10-16 16:00:00 EEST+0300 2023-10-16 18:00:00 EEST+0300              0.3105
	          3 2023-10-16 16:00:00 EEST+0300 2023-10-16 19:00:00 EEST+0300            0.327667
	          4 2023-10-16 21:00:00 EEST+0300 2023-10-17 01:00:00 EEST+0300              0.3685


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
