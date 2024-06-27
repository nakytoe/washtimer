
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-28 09:00:00 EEST+0300 2024-06-28 10:00:00 EEST+0300               3.751
	          2 2024-06-28 09:00:00 EEST+0300 2024-06-28 11:00:00 EEST+0300               3.686
	          3 2024-06-28 08:00:00 EEST+0300 2024-06-28 11:00:00 EEST+0300               3.615
	          4 2024-06-27 17:00:00 EEST+0300 2024-06-27 21:00:00 EEST+0300               3.523

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-29 00:00:00 EEST+0300 2024-06-29 01:00:00 EEST+0300                -0.2
	          2 2024-06-28 23:00:00 EEST+0300 2024-06-29 01:00:00 EEST+0300             -0.1035
	          3 2024-06-28 14:00:00 EEST+0300 2024-06-28 17:00:00 EEST+0300           -0.057333
	          4 2024-06-28 14:00:00 EEST+0300 2024-06-28 18:00:00 EEST+0300             -0.0435


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
