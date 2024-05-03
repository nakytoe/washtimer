
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-03 20:00:00 EEST+0300 2024-05-03 21:00:00 EEST+0300              12.028
	          2 2024-05-03 19:00:00 EEST+0300 2024-05-03 21:00:00 EEST+0300              11.002
	          3 2024-05-03 18:00:00 EEST+0300 2024-05-03 21:00:00 EEST+0300            9.073667
	          4 2024-05-03 17:00:00 EEST+0300 2024-05-03 21:00:00 EEST+0300             8.10725

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-04 15:00:00 EEST+0300 2024-05-04 16:00:00 EEST+0300               1.654
	          2 2024-05-04 14:00:00 EEST+0300 2024-05-04 16:00:00 EEST+0300               1.728
	          3 2024-05-04 02:00:00 EEST+0300 2024-05-04 05:00:00 EEST+0300            2.135333
	          4 2024-05-04 01:00:00 EEST+0300 2024-05-04 05:00:00 EEST+0300             2.20825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
