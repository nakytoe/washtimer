
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-25 10:00:00 EEST+0300 2024-07-25 11:00:00 EEST+0300               3.119
	          2 2024-07-25 10:00:00 EEST+0300 2024-07-25 12:00:00 EEST+0300              3.1175
	          3 2024-07-25 09:00:00 EEST+0300 2024-07-25 12:00:00 EEST+0300               3.103
	          4 2024-07-25 09:00:00 EEST+0300 2024-07-25 13:00:00 EEST+0300             3.08175

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-26 00:00:00 EEST+0300 2024-07-26 01:00:00 EEST+0300               2.687
	          2 2024-07-25 14:00:00 EEST+0300 2024-07-25 16:00:00 EEST+0300              2.7895
	          3 2024-07-25 14:00:00 EEST+0300 2024-07-25 17:00:00 EEST+0300               2.817
	          4 2024-07-25 14:00:00 EEST+0300 2024-07-25 18:00:00 EEST+0300              2.8415


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
