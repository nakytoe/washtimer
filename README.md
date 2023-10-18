
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-18 09:00:00 EEST+0300 2023-10-18 10:00:00 EEST+0300              19.446
	          2 2023-10-18 09:00:00 EEST+0300 2023-10-18 11:00:00 EEST+0300              16.894
	          3 2023-10-18 09:00:00 EEST+0300 2023-10-18 12:00:00 EEST+0300           14.758667
	          4 2023-10-18 08:00:00 EEST+0300 2023-10-18 12:00:00 EEST+0300              13.285

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-19 00:00:00 EEST+0300 2023-10-19 01:00:00 EEST+0300               0.844
	          2 2023-10-18 23:00:00 EEST+0300 2023-10-19 01:00:00 EEST+0300               0.952
	          3 2023-10-18 22:00:00 EEST+0300 2023-10-19 01:00:00 EEST+0300            1.012333
	          4 2023-10-18 21:00:00 EEST+0300 2023-10-19 01:00:00 EEST+0300              1.0455


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
