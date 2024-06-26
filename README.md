
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-26 09:00:00 EEST+0300 2024-06-26 10:00:00 EEST+0300               4.408
	          2 2024-06-26 09:00:00 EEST+0300 2024-06-26 11:00:00 EEST+0300              4.3825
	          3 2024-06-26 09:00:00 EEST+0300 2024-06-26 12:00:00 EEST+0300               4.381
	          4 2024-06-26 08:00:00 EEST+0300 2024-06-26 12:00:00 EEST+0300             4.33975

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-26 07:00:00 EEST+0300 2024-06-26 08:00:00 EEST+0300               3.608
	          2 2024-06-26 07:00:00 EEST+0300 2024-06-26 09:00:00 EEST+0300               3.912
	          3 2024-06-26 14:00:00 EEST+0300 2024-06-26 17:00:00 EEST+0300               4.045
	          4 2024-06-26 13:00:00 EEST+0300 2024-06-26 17:00:00 EEST+0300             4.05375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
