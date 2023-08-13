
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-14 08:00:00 EEST+0300 2023-08-14 09:00:00 EEST+0300              12.859
	          2 2023-08-14 08:00:00 EEST+0300 2023-08-14 10:00:00 EEST+0300              12.715
	          3 2023-08-14 08:00:00 EEST+0300 2023-08-14 11:00:00 EEST+0300           12.170333
	          4 2023-08-14 08:00:00 EEST+0300 2023-08-14 12:00:00 EEST+0300              11.608

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-13 16:00:00 EEST+0300 2023-08-13 17:00:00 EEST+0300               0.858
	          2 2023-08-13 16:00:00 EEST+0300 2023-08-13 18:00:00 EEST+0300              1.5005
	          3 2023-08-14 03:00:00 EEST+0300 2023-08-14 06:00:00 EEST+0300               1.776
	          4 2023-08-14 02:00:00 EEST+0300 2023-08-14 06:00:00 EEST+0300              1.7845


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
