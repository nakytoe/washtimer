
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-03 09:00:00 EEST+0300 2024-05-03 10:00:00 EEST+0300              14.259
	          2 2024-05-03 08:00:00 EEST+0300 2024-05-03 10:00:00 EEST+0300              13.685
	          3 2024-05-03 07:00:00 EEST+0300 2024-05-03 10:00:00 EEST+0300           11.934333
	          4 2024-05-03 07:00:00 EEST+0300 2024-05-03 11:00:00 EEST+0300              10.729

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-04 00:00:00 EEST+0300 2024-05-04 01:00:00 EEST+0300               3.192
	          2 2024-05-03 23:00:00 EEST+0300 2024-05-04 01:00:00 EEST+0300              3.5715
	          3 2024-05-03 22:00:00 EEST+0300 2024-05-04 01:00:00 EEST+0300               3.914
	          4 2024-05-03 21:00:00 EEST+0300 2024-05-04 01:00:00 EEST+0300               4.168


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
