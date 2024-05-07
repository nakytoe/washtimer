
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-08 08:00:00 EEST+0300 2024-05-08 09:00:00 EEST+0300               37.02
	          2 2024-05-08 08:00:00 EEST+0300 2024-05-08 10:00:00 EEST+0300             34.0095
	          3 2024-05-08 07:00:00 EEST+0300 2024-05-08 10:00:00 EEST+0300           31.890667
	          4 2024-05-08 07:00:00 EEST+0300 2024-05-08 11:00:00 EEST+0300            28.85175

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-08 01:00:00 EEST+0300 2024-05-08 02:00:00 EEST+0300               3.032
	          2 2024-05-08 00:00:00 EEST+0300 2024-05-08 02:00:00 EEST+0300               3.066
	          3 2024-05-08 00:00:00 EEST+0300 2024-05-08 03:00:00 EEST+0300            3.261333
	          4 2024-05-07 23:00:00 EEST+0300 2024-05-08 03:00:00 EEST+0300              3.4655


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
