
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-19 08:00:00 EEST+0300 2024-06-19 09:00:00 EEST+0300               13.46
	          2 2024-06-19 08:00:00 EEST+0300 2024-06-19 10:00:00 EEST+0300              12.986
	          3 2024-06-19 07:00:00 EEST+0300 2024-06-19 10:00:00 EEST+0300           10.174667
	          4 2024-06-19 07:00:00 EEST+0300 2024-06-19 11:00:00 EEST+0300              8.5225

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-20 00:00:00 EEST+0300 2024-06-20 01:00:00 EEST+0300              -0.179
	          2 2024-06-19 23:00:00 EEST+0300 2024-06-20 01:00:00 EEST+0300             -0.0895
	          3 2024-06-19 22:00:00 EEST+0300 2024-06-20 01:00:00 EEST+0300               0.035
	          4 2024-06-19 21:00:00 EEST+0300 2024-06-20 01:00:00 EEST+0300             0.45075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
