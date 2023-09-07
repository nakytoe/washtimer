
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-07 10:00:00 EEST+0300 2023-09-07 11:00:00 EEST+0300              19.287
	          2 2023-09-07 09:00:00 EEST+0300 2023-09-07 11:00:00 EEST+0300             17.4555
	          3 2023-09-07 08:00:00 EEST+0300 2023-09-07 11:00:00 EEST+0300           17.010333
	          4 2023-09-07 08:00:00 EEST+0300 2023-09-07 12:00:00 EEST+0300             15.9135

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-08 00:00:00 EEST+0300 2023-09-08 01:00:00 EEST+0300               1.603
	          2 2023-09-07 23:00:00 EEST+0300 2023-09-08 01:00:00 EEST+0300              1.7705
	          3 2023-09-07 22:00:00 EEST+0300 2023-09-08 01:00:00 EEST+0300            2.031667
	          4 2023-09-07 21:00:00 EEST+0300 2023-09-08 01:00:00 EEST+0300                 2.4


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
