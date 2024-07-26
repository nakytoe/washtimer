
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-26 19:00:00 EEST+0300 2024-07-26 20:00:00 EEST+0300               3.098
	          2 2024-07-26 19:00:00 EEST+0300 2024-07-26 21:00:00 EEST+0300               3.049
	          3 2024-07-26 18:00:00 EEST+0300 2024-07-26 21:00:00 EEST+0300            3.002667
	          4 2024-07-26 17:00:00 EEST+0300 2024-07-26 21:00:00 EEST+0300             2.97425

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-27 15:00:00 EEST+0300 2024-07-27 16:00:00 EEST+0300               2.169
	          2 2024-07-27 14:00:00 EEST+0300 2024-07-27 16:00:00 EEST+0300              2.2515
	          3 2024-07-27 14:00:00 EEST+0300 2024-07-27 17:00:00 EEST+0300            2.337667
	          4 2024-07-27 00:00:00 EEST+0300 2024-07-27 04:00:00 EEST+0300             2.36275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
