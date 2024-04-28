
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-28 21:00:00 EEST+0300 2024-04-28 22:00:00 EEST+0300               10.05
	          2 2024-04-28 21:00:00 EEST+0300 2024-04-28 23:00:00 EEST+0300              9.7785
	          3 2024-04-28 17:00:00 EEST+0300 2024-04-28 20:00:00 EEST+0300                9.47
	          4 2024-04-28 19:00:00 EEST+0300 2024-04-28 23:00:00 EEST+0300              9.4085

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-28 07:00:00 EEST+0300 2024-04-28 08:00:00 EEST+0300               1.875
	          2 2024-04-28 07:00:00 EEST+0300 2024-04-28 09:00:00 EEST+0300              2.5345
	          3 2024-04-28 07:00:00 EEST+0300 2024-04-28 10:00:00 EEST+0300               2.914
	          4 2024-04-28 07:00:00 EEST+0300 2024-04-28 11:00:00 EEST+0300               3.188


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
