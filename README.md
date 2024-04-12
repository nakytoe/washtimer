
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-12 19:00:00 EEST+0300 2024-04-12 20:00:00 EEST+0300               5.612
	          2 2024-04-12 18:00:00 EEST+0300 2024-04-12 20:00:00 EEST+0300               5.249
	          3 2024-04-12 18:00:00 EEST+0300 2024-04-12 21:00:00 EEST+0300               4.775
	          4 2024-04-12 17:00:00 EEST+0300 2024-04-12 21:00:00 EEST+0300             4.47975

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-13 15:00:00 EEST+0300 2024-04-13 16:00:00 EEST+0300              -0.021
	          2 2024-04-13 14:00:00 EEST+0300 2024-04-13 16:00:00 EEST+0300             -0.0135
	          3 2024-04-13 14:00:00 EEST+0300 2024-04-13 17:00:00 EEST+0300           -0.009333
	          4 2024-04-13 12:00:00 EEST+0300 2024-04-13 16:00:00 EEST+0300             -0.0075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
