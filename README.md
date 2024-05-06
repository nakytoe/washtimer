
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-07 08:00:00 EEST+0300 2024-05-07 09:00:00 EEST+0300              25.922
	          2 2024-05-07 07:00:00 EEST+0300 2024-05-07 09:00:00 EEST+0300              20.044
	          3 2024-05-07 07:00:00 EEST+0300 2024-05-07 10:00:00 EEST+0300           18.019333
	          4 2024-05-07 07:00:00 EEST+0300 2024-05-07 11:00:00 EEST+0300            16.35875

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-08 00:00:00 EEST+0300 2024-05-08 01:00:00 EEST+0300                 3.1
	          2 2024-05-07 23:00:00 EEST+0300 2024-05-08 01:00:00 EEST+0300               3.589
	          3 2024-05-07 02:00:00 EEST+0300 2024-05-07 05:00:00 EEST+0300            4.323333
	          4 2024-05-07 02:00:00 EEST+0300 2024-05-07 06:00:00 EEST+0300              4.3335


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
