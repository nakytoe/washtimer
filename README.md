
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-29 09:00:00 EEST+0300 2024-04-29 10:00:00 EEST+0300              11.875
	          2 2024-04-29 08:00:00 EEST+0300 2024-04-29 10:00:00 EEST+0300              10.897
	          3 2024-04-29 08:00:00 EEST+0300 2024-04-29 11:00:00 EEST+0300            9.853333
	          4 2024-04-29 07:00:00 EEST+0300 2024-04-29 11:00:00 EEST+0300             9.24975

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-29 15:00:00 EEST+0300 2024-04-29 16:00:00 EEST+0300               3.121
	          2 2024-04-29 14:00:00 EEST+0300 2024-04-29 16:00:00 EEST+0300              3.1305
	          3 2024-04-29 13:00:00 EEST+0300 2024-04-29 16:00:00 EEST+0300            3.384333
	          4 2024-04-29 13:00:00 EEST+0300 2024-04-29 17:00:00 EEST+0300              3.5505


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
