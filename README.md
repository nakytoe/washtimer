
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-14 20:00:00 EEST+0300 2023-09-14 21:00:00 EEST+0300              28.555
	          2 2023-09-14 20:00:00 EEST+0300 2023-09-14 22:00:00 EEST+0300              25.797
	          3 2023-09-14 19:00:00 EEST+0300 2023-09-14 22:00:00 EEST+0300              24.349
	          4 2023-09-14 19:00:00 EEST+0300 2023-09-14 23:00:00 EEST+0300            22.39525

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-14 07:00:00 EEST+0300 2023-09-14 08:00:00 EEST+0300               1.886
	          2 2023-09-14 07:00:00 EEST+0300 2023-09-14 09:00:00 EEST+0300              6.5075
	          3 2023-09-14 07:00:00 EEST+0300 2023-09-14 10:00:00 EEST+0300           10.748667
	          4 2023-09-14 13:00:00 EEST+0300 2023-09-14 17:00:00 EEST+0300            11.12125


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
