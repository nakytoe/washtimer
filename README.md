
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-21 19:00:00 EEST+0300 2023-08-21 20:00:00 EEST+0300              68.194
	          2 2023-08-21 18:00:00 EEST+0300 2023-08-21 20:00:00 EEST+0300             52.6995
	          3 2023-08-21 18:00:00 EEST+0300 2023-08-21 21:00:00 EEST+0300           45.469333
	          4 2023-08-21 18:00:00 EEST+0300 2023-08-21 22:00:00 EEST+0300              40.438

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-23 00:00:00 EEST+0300 2023-08-23 01:00:00 EEST+0300               9.932
	          2 2023-08-22 03:00:00 EEST+0300 2023-08-22 05:00:00 EEST+0300             12.8295
	          3 2023-08-22 02:00:00 EEST+0300 2023-08-22 05:00:00 EEST+0300           12.889333
	          4 2023-08-22 02:00:00 EEST+0300 2023-08-22 06:00:00 EEST+0300              12.948


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
