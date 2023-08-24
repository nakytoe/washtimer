
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-24 20:00:00 EEST+0300 2023-08-24 21:00:00 EEST+0300               32.06
	          2 2023-08-24 19:00:00 EEST+0300 2023-08-24 21:00:00 EEST+0300             28.8455
	          3 2023-08-24 19:00:00 EEST+0300 2023-08-24 22:00:00 EEST+0300           27.742667
	          4 2023-08-24 18:00:00 EEST+0300 2023-08-24 22:00:00 EEST+0300            25.61675

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-26 00:00:00 EEST+0300 2023-08-26 01:00:00 EEST+0300               5.528
	          2 2023-08-25 02:00:00 EEST+0300 2023-08-25 04:00:00 EEST+0300               9.919
	          3 2023-08-25 02:00:00 EEST+0300 2023-08-25 05:00:00 EEST+0300               9.998
	          4 2023-08-25 01:00:00 EEST+0300 2023-08-25 05:00:00 EEST+0300             10.0905


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
