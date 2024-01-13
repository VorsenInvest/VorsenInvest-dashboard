<script>
	import {onMount} from 'svelte'; 
    export let dataColors;
    import { browser } from "$app/environment";
    function getChartColorsArray(colors) {
        if (browser) {
            return colors.map(function (value) {
                var newValue = value.replace(" ", "");
                if (newValue.indexOf(",") === -1) {
                    var color = getComputedStyle(
                        document.documentElement
                    ).getPropertyValue(newValue);
                    if (color.indexOf("#") !== -1)
                        color = color.replace(" ", "");
                    if (color) return color;
                    else return newValue;
                } else {
                    var val = value.split(",");
                    if (val.length === 2) {
                        var rgbaColor = getComputedStyle(
                            document.documentElement
                        ).getPropertyValue(val[0]);
                        rgbaColor = "rgba(" + rgbaColor + "," + val[1] + ")";
                        return rgbaColor;
                    } else {
                        return newValue;
                    }
                }
            });
        }
    }
	const revenueExpensesChartsColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 290,
			type: 'area',
			toolbar: 'false'
		},
		series: [
			{
				name: 'Revenue',
				data: [20, 25, 30, 35, 40, 55, 70, 110, 150, 180, 210, 250]
			},
			{
				name: 'Expenses',
				data: [12, 17, 45, 42, 24, 35, 42, 75, 102, 108, 156, 199]
			}
		],
		dataLabels: {
			enabled: false
		},
		stroke: {
			curve: 'smooth',
			width: 2
		},
		xaxis: {
			categories: [
				'Jan',
				'Feb',
				'Mar',
				'Apr',
				'May',
				'Jun',
				'Jul',
				'Aug',
				'Sep',
				'Oct',
				'Nov',
				'Dec'
			]
		},
		yaxis: {
			labels: {
				formatter: function (value) {
					return '$' + value + 'k';
				}
			},
			tickAmount: 5,
			min: 0,
			max: 260
		},
		colors: revenueExpensesChartsColors,
		fill: {
			opacity: 0.06,
			colors: revenueExpensesChartsColors,
			type: 'solid'
		}
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#balanceoverviewchart"), options)
  		chart.render()
	})
</script>

<div id="balanceoverviewchart" class="apex-charts" dir="ltr"></div>
