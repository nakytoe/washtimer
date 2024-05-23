
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-24 09:00:00 EEST+0300 2024-05-24 10:00:00 EEST+0300                8.06
	          2 2024-05-24 09:00:00 EEST+0300 2024-05-24 11:00:00 EEST+0300              7.5895
	          3 2024-05-24 09:00:00 EEST+0300 2024-05-24 12:00:00 EEST+0300            6.332667
	          4 2024-05-24 09:00:00 EEST+0300 2024-05-24 13:00:00 EEST+0300             5.56425

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-24 02:00:00 EEST+0300 2024-05-24 03:00:00 EEST+0300              -0.249
	          2 2024-05-24 01:00:00 EEST+0300 2024-05-24 03:00:00 EEST+0300             -0.2475
	          3 2024-05-24 01:00:00 EEST+0300 2024-05-24 04:00:00 EEST+0300           -0.239667
	          4 2024-05-24 01:00:00 EEST+0300 2024-05-24 05:00:00 EEST+0300              -0.229


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
