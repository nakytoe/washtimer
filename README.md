
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-22 12:00:00 EEST+0300 2023-08-22 13:00:00 EEST+0300              49.785
	          2 2023-08-22 11:00:00 EEST+0300 2023-08-22 13:00:00 EEST+0300             40.3925
	          3 2023-08-22 11:00:00 EEST+0300 2023-08-22 14:00:00 EEST+0300           36.848333
	          4 2023-08-22 09:00:00 EEST+0300 2023-08-22 13:00:00 EEST+0300             35.1205

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-23 00:00:00 EEST+0300 2023-08-23 01:00:00 EEST+0300               9.932
	          2 2023-08-22 15:00:00 EEST+0300 2023-08-22 17:00:00 EEST+0300             12.9385
	          3 2023-08-22 14:00:00 EEST+0300 2023-08-22 17:00:00 EEST+0300           13.748667
	          4 2023-08-22 14:00:00 EEST+0300 2023-08-22 18:00:00 EEST+0300              14.961


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
