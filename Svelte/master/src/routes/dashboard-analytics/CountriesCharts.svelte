<script>
	import {onDestroy, onMount} from 'svelte'; 
    import { browser } from "$app/environment";
	import { themeChangeEvent } from "$lib/eventBus";
	export let dataColors;
	let chart;

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
	
	const barchartCountriesColors = getChartColorsArray(dataColors);


	const THEME_CHART_COLORS = {
		default: ["--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-danger", "--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-info"],
		minimal: ["--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary-rgb, 0.45", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary"],
		modern: ["--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-danger", "--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-info"],
		interactive: ["--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-danger", "--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-info"],
		creative: ["--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-danger", "--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-info"],
		corporate: ["--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-danger", "--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-info"],
		saas:["--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-danger", "--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-info"],
		galaxy: ["--vz-primary-rgb, 0.4", "--vz-primary-rgb, 0.4", "--vz-primary-rgb, 0.4", "--vz-primary-rgb, 0.4", "--vz-primary", "--vz-primary-rgb, 0.4", "--vz-primary-rgb, 0.4", "--vz-primary-rgb, 0.4", "--vz-primary-rgb, 0.4", "--vz-primary-rgb, 0.4"], 
		classic: ["--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary-rgb, 0.45", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary"],
		vintage: ["--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-danger", "--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-info"],
		material:["--vz-primary", "--vz-primary", "--vz-info", "--vz-info", "--vz-danger", "--vz-primary", "--vz-primary", "--vz-warning", "--vz-primary", "--vz-primary"]
	};

	// Function to find the index of a key
	function findIndexByKey(key) {
		const keys = Object.keys(THEME_CHART_COLORS);
		return keys.indexOf(key);
	}

	// Subscribe to the theme change event
	const unsubscribeEvent = themeChangeEvent.subscribe((newTheme) => {
		// Handle the theme change event
		if(newTheme == null || newTheme == undefined){
			return;
		}
		let key = findIndexByKey(newTheme);
		let newColors;
		if (key >= 0) {
			newColors = THEME_CHART_COLORS[newTheme];
		}
		if (browser) {
			newColors = ( key >= 0) ? getChartColorsArray(newColors) : dataColors;
			setTimeout(() => {
				chart.updateOptions({
					colors: newColors,
				});
			}, 500);
		}
	});


	var options = {
		chart: {
			type: 'bar',
			height: 436,
			toolbar: {
				show: false
			}
		},
		series: [
			{
				data: [1010, 1640, 490, 1255, 1050, 689, 800, 420, 1085, 589],
				name: 'Sessions'
			}
		],
		plotOptions: {
			bar: {
				borderRadius: 4,
				horizontal: true,
				distributed: true,
				dataLabels: {
					position: 'top'
				}
			}
		},
		colors: barchartCountriesColors,
		dataLabels: {
			enabled: true,
			offsetX: 32,
			style: {
				fontSize: '12px',
				fontWeight: 400,
				colors: ['#adb5bd']
			}
		},

		legend: {
			show: false
		},
		grid: {
			show: false
		},
		xaxis: {
			categories: [
				'India',
				'United States',
				'China',
				'Indonesia',
				'Russia',
				'Bangladesh',
				'Canada',
				'Brazil',
				'Vietnam',
				'UK'
			]
		}
	};
	onMount(() => {
		 chart = new ApexCharts(document.querySelector("#countrieschart"), options)
  		chart.render()
	})

	// Ensure to unsubscribe to avoid memory leaks
	onDestroy(() => {
		unsubscribeEvent();
	});
</script>

<div id="countrieschart" class="apex-charts" dir="ltr"></div>