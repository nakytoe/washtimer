
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-09 08:00:00 EEST+0300 2024-04-09 09:00:00 EEST+0300              10.655
	          2 2024-04-09 08:00:00 EEST+0300 2024-04-09 10:00:00 EEST+0300              10.155
	          3 2024-04-09 08:00:00 EEST+0300 2024-04-09 11:00:00 EEST+0300               9.489
	          4 2024-04-09 07:00:00 EEST+0300 2024-04-09 11:00:00 EEST+0300             8.93975

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-10 00:00:00 EEST+0300 2024-04-10 01:00:00 EEST+0300               0.619
	          2 2024-04-09 23:00:00 EEST+0300 2024-04-10 01:00:00 EEST+0300              2.3485
	          3 2024-04-09 22:00:00 EEST+0300 2024-04-10 01:00:00 EEST+0300            3.139667
	          4 2024-04-09 21:00:00 EEST+0300 2024-04-10 01:00:00 EEST+0300             3.59075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
