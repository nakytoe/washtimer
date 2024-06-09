
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-10 09:00:00 EEST+0300 2024-06-10 10:00:00 EEST+0300              10.539
	          2 2024-06-10 08:00:00 EEST+0300 2024-06-10 10:00:00 EEST+0300             10.2545
	          3 2024-06-10 08:00:00 EEST+0300 2024-06-10 11:00:00 EEST+0300                9.73
	          4 2024-06-10 08:00:00 EEST+0300 2024-06-10 12:00:00 EEST+0300             8.87625

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-09 16:00:00 EEST+0300 2024-06-09 17:00:00 EEST+0300              -0.658
	          2 2024-06-09 16:00:00 EEST+0300 2024-06-09 18:00:00 EEST+0300             -0.5785
	          3 2024-06-09 16:00:00 EEST+0300 2024-06-09 19:00:00 EEST+0300           -0.405333
	          4 2024-06-09 16:00:00 EEST+0300 2024-06-09 20:00:00 EEST+0300              -0.115


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
