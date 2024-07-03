
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-03 11:00:00 EEST+0300 2024-07-03 12:00:00 EEST+0300               4.874
	          2 2024-07-03 11:00:00 EEST+0300 2024-07-03 13:00:00 EEST+0300              4.8625
	          3 2024-07-03 11:00:00 EEST+0300 2024-07-03 14:00:00 EEST+0300            4.811667
	          4 2024-07-03 11:00:00 EEST+0300 2024-07-03 15:00:00 EEST+0300             4.80225

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-04 00:00:00 EEST+0300 2024-07-04 01:00:00 EEST+0300               3.964
	          2 2024-07-03 23:00:00 EEST+0300 2024-07-04 01:00:00 EEST+0300              4.0695
	          3 2024-07-03 22:00:00 EEST+0300 2024-07-04 01:00:00 EEST+0300            4.161333
	          4 2024-07-03 21:00:00 EEST+0300 2024-07-04 01:00:00 EEST+0300             4.22025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
