
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-04 19:00:00 EEST+0300 2024-04-04 20:00:00 EEST+0300              12.091
	          2 2024-04-04 19:00:00 EEST+0300 2024-04-04 21:00:00 EEST+0300              11.492
	          3 2024-04-04 18:00:00 EEST+0300 2024-04-04 21:00:00 EEST+0300              10.558
	          4 2024-04-04 18:00:00 EEST+0300 2024-04-04 22:00:00 EEST+0300            10.01975

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-05 17:00:00 EEST+0300 2024-04-05 18:00:00 EEST+0300               3.424
	          2 2024-04-05 16:00:00 EEST+0300 2024-04-05 18:00:00 EEST+0300              3.6365
	          3 2024-04-05 15:00:00 EEST+0300 2024-04-05 18:00:00 EEST+0300            3.956667
	          4 2024-04-05 15:00:00 EEST+0300 2024-04-05 19:00:00 EEST+0300             4.20725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
