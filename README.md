
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-09 20:00:00 EEST+0300 2024-07-09 21:00:00 EEST+0300               4.455
	          2 2024-07-09 19:00:00 EEST+0300 2024-07-09 21:00:00 EEST+0300              4.4535
	          3 2024-07-09 19:00:00 EEST+0300 2024-07-09 22:00:00 EEST+0300            4.429667
	          4 2024-07-09 18:00:00 EEST+0300 2024-07-09 22:00:00 EEST+0300               4.397

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-11 00:00:00 EEST+0300 2024-07-11 01:00:00 EEST+0300                 0.0
	          2 2024-07-10 23:00:00 EEST+0300 2024-07-11 01:00:00 EEST+0300               0.309
	          3 2024-07-10 22:00:00 EEST+0300 2024-07-11 01:00:00 EEST+0300            0.955333
	          4 2024-07-10 21:00:00 EEST+0300 2024-07-11 01:00:00 EEST+0300               1.413


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
