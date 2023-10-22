
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-22 19:00:00 EEST+0300 2023-10-22 20:00:00 EEST+0300               7.256
	          2 2023-10-22 19:00:00 EEST+0300 2023-10-22 21:00:00 EEST+0300               7.192
	          3 2023-10-22 18:00:00 EEST+0300 2023-10-22 21:00:00 EEST+0300            7.086333
	          4 2023-10-22 18:00:00 EEST+0300 2023-10-22 22:00:00 EEST+0300             7.00025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-22 07:00:00 EEST+0300 2023-10-22 08:00:00 EEST+0300               1.694
	          2 2023-10-22 07:00:00 EEST+0300 2023-10-22 09:00:00 EEST+0300               1.741
	          3 2023-10-22 07:00:00 EEST+0300 2023-10-22 10:00:00 EEST+0300            1.865667
	          4 2023-10-22 07:00:00 EEST+0300 2023-10-22 11:00:00 EEST+0300               1.957


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
