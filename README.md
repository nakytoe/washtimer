
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-18 08:00:00 EEST+0300 2024-06-18 09:00:00 EEST+0300              15.701
	          2 2024-06-18 08:00:00 EEST+0300 2024-06-18 10:00:00 EEST+0300              14.674
	          3 2024-06-18 08:00:00 EEST+0300 2024-06-18 11:00:00 EEST+0300           12.898333
	          4 2024-06-18 08:00:00 EEST+0300 2024-06-18 12:00:00 EEST+0300              11.607

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-19 00:00:00 EEST+0300 2024-06-19 01:00:00 EEST+0300               3.778
	          2 2024-06-18 23:00:00 EEST+0300 2024-06-19 01:00:00 EEST+0300              4.0055
	          3 2024-06-18 22:00:00 EEST+0300 2024-06-19 01:00:00 EEST+0300            4.209667
	          4 2024-06-18 21:00:00 EEST+0300 2024-06-19 01:00:00 EEST+0300             4.37175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
