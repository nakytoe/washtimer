
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-28 19:00:00 EEST+0300 2023-09-28 20:00:00 EEST+0300               3.721
	          2 2023-09-28 18:00:00 EEST+0300 2023-09-28 20:00:00 EEST+0300              3.7205
	          3 2023-09-28 17:00:00 EEST+0300 2023-09-28 20:00:00 EEST+0300            3.720333
	          4 2023-09-28 16:00:00 EEST+0300 2023-09-28 20:00:00 EEST+0300             3.25525

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-29 00:00:00 EEST+0300 2023-09-29 01:00:00 EEST+0300              -0.065
	          2 2023-09-29 00:00:00 EEST+0300 2023-09-29 02:00:00 EEST+0300             -0.0625
	          3 2023-09-29 00:00:00 EEST+0300 2023-09-29 03:00:00 EEST+0300           -0.061667
	          4 2023-09-29 00:00:00 EEST+0300 2023-09-29 04:00:00 EEST+0300             -0.0605


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
