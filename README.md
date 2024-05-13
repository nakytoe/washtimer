
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-13 08:00:00 EEST+0300 2024-05-13 09:00:00 EEST+0300               49.35
	          2 2024-05-13 07:00:00 EEST+0300 2024-05-13 09:00:00 EEST+0300             40.1755
	          3 2024-05-13 07:00:00 EEST+0300 2024-05-13 10:00:00 EEST+0300           35.413333
	          4 2024-05-13 07:00:00 EEST+0300 2024-05-13 11:00:00 EEST+0300            32.05725

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-14 00:00:00 EEST+0300 2024-05-14 01:00:00 EEST+0300                4.08
	          2 2024-05-13 12:00:00 EEST+0300 2024-05-13 14:00:00 EEST+0300              5.8935
	          3 2024-05-13 12:00:00 EEST+0300 2024-05-13 15:00:00 EEST+0300            5.995667
	          4 2024-05-13 12:00:00 EEST+0300 2024-05-13 16:00:00 EEST+0300              6.5275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
