
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-23 20:00:00 EEST+0300 2024-04-23 21:00:00 EEST+0300              15.253
	          2 2024-04-23 19:00:00 EEST+0300 2024-04-23 21:00:00 EEST+0300             13.9755
	          3 2024-04-23 19:00:00 EEST+0300 2024-04-23 22:00:00 EEST+0300           13.450667
	          4 2024-04-23 19:00:00 EEST+0300 2024-04-23 23:00:00 EEST+0300              13.187

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-23 00:00:00 EEST+0300 2024-04-23 01:00:00 EEST+0300               4.479
	          2 2024-04-22 23:00:00 EEST+0300 2024-04-23 01:00:00 EEST+0300              4.7495
	          3 2024-04-22 22:00:00 EEST+0300 2024-04-23 01:00:00 EEST+0300               5.058
	          4 2024-04-22 21:00:00 EEST+0300 2024-04-23 01:00:00 EEST+0300                5.31


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
