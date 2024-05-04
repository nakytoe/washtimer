
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-05 20:00:00 EEST+0300 2024-05-05 21:00:00 EEST+0300               4.772
	          2 2024-05-05 19:00:00 EEST+0300 2024-05-05 21:00:00 EEST+0300               4.724
	          3 2024-05-05 19:00:00 EEST+0300 2024-05-05 22:00:00 EEST+0300               4.584
	          4 2024-05-05 19:00:00 EEST+0300 2024-05-05 23:00:00 EEST+0300             4.46375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-05 15:00:00 EEST+0300 2024-05-05 16:00:00 EEST+0300               0.236
	          2 2024-05-05 14:00:00 EEST+0300 2024-05-05 16:00:00 EEST+0300               0.242
	          3 2024-05-05 13:00:00 EEST+0300 2024-05-05 16:00:00 EEST+0300            0.296333
	          4 2024-05-05 12:00:00 EEST+0300 2024-05-05 16:00:00 EEST+0300               0.337


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
