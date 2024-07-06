
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-06 21:00:00 EEST+0300 2024-07-06 22:00:00 EEST+0300                0.83
	          2 2024-07-06 07:00:00 EEST+0300 2024-07-06 09:00:00 EEST+0300              0.6875
	          3 2024-07-06 07:00:00 EEST+0300 2024-07-06 10:00:00 EEST+0300            0.602333
	          4 2024-07-06 07:00:00 EEST+0300 2024-07-06 11:00:00 EEST+0300             0.46175

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-06 16:00:00 EEST+0300 2024-07-06 17:00:00 EEST+0300              -0.271
	          2 2024-07-06 15:00:00 EEST+0300 2024-07-06 17:00:00 EEST+0300             -0.2445
	          3 2024-07-06 15:00:00 EEST+0300 2024-07-06 18:00:00 EEST+0300              -0.183
	          4 2024-07-06 14:00:00 EEST+0300 2024-07-06 18:00:00 EEST+0300            -0.14025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
