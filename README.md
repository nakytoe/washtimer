
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-30 19:00:00 EEST+0300 2024-06-30 20:00:00 EEST+0300               4.063
	          2 2024-06-30 19:00:00 EEST+0300 2024-06-30 21:00:00 EEST+0300               4.061
	          3 2024-06-30 19:00:00 EEST+0300 2024-06-30 22:00:00 EEST+0300            4.059333
	          4 2024-06-30 19:00:00 EEST+0300 2024-06-30 23:00:00 EEST+0300             4.05575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-29 16:00:00 EEST+0300 2024-06-29 17:00:00 EEST+0300              -0.229
	          2 2024-06-29 16:00:00 EEST+0300 2024-06-29 18:00:00 EEST+0300             -0.1885
	          3 2024-06-29 16:00:00 EEST+0300 2024-06-29 19:00:00 EEST+0300           -0.129333
	          4 2024-06-29 16:00:00 EEST+0300 2024-06-29 20:00:00 EEST+0300              -0.097


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
