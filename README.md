
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-11 11:00:00 EEST+0300 2023-10-11 12:00:00 EEST+0300               0.308
	          2 2023-10-11 10:00:00 EEST+0300 2023-10-11 12:00:00 EEST+0300              0.2835
	          3 2023-10-11 09:00:00 EEST+0300 2023-10-11 12:00:00 EEST+0300               0.255
	          4 2023-10-11 09:00:00 EEST+0300 2023-10-11 13:00:00 EEST+0300             0.22375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-12 00:00:00 EEST+0300 2023-10-12 01:00:00 EEST+0300              -0.508
	          2 2023-10-11 23:00:00 EEST+0300 2023-10-12 01:00:00 EEST+0300             -0.4145
	          3 2023-10-11 22:00:00 EEST+0300 2023-10-12 01:00:00 EEST+0300              -0.344
	          4 2023-10-11 21:00:00 EEST+0300 2023-10-12 01:00:00 EEST+0300              -0.282


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
