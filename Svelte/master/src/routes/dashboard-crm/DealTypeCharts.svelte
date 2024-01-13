<script>
	import {onMount} from 'svelte'; 
	import { themeChangeEvent } from "$lib/eventBus";
    import { browser } from "$app/environment";
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
	const dealTypeChartsColors = getChartColorsArray(dataColors);

	const THEME_CHART_COLORS = {
		default: ["--vz-warning", "--vz-danger", "--vz-success"],
		minimal: ["--vz-primary-rgb, 0.15", "--vz-primary-rgb, 0.35", "--vz-primary-rgb, 0.45"],
		modern: ["--vz-warning", "--vz-secondary", "--vz-success"],
		interactive: ["--vz-warning", "--vz-info", "--vz-primary"],
		corporate: ["--vz-secondary", "--vz-info", "--vz-success"],
		classic: ["--vz-secondary", "--vz-danger", "--vz-success"],
		creative: ["--vz-warning", "--vz-danger", "--vz-success"],
		galaxy: ["--vz-warning", "--vz-danger", "--vz-success"], 
		vintage: ["--vz-warning", "--vz-danger", "--vz-success"],
		saas: ["--vz-warning", "--vz-danger", "--vz-success"],
		material:["--vz-warning", "--vz-danger", "--vz-success"]
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
			height: 341,
			type: 'radar',
			dropShadow: {
				enabled: true,
				blur: 1,
				left: 1,
				top: 1
			},
			toolbar: {
				show: false
			}
		},
		series: [
			{
				name: 'Pending',
				data: [80, 50, 30, 40, 100, 20]
			},
			{
				name: 'Loss',
				data: [20, 30, 40, 80, 20, 80]
			},
			{
				name: 'Won',
				data: [44, 76, 78, 13, 43, 10]
			}
		],
		stroke: {
			width: 2
		},
		fill: {
			opacity: 0.2
		},
		legend: {
			show: true,
			fontWeight: 500,
			offsetX: 0,
			offsetY: -8,
			markers: {
				width: 8,
				height: 8,
				radius: 6
			},
			itemMargin: {
				horizontal: 10,
				vertical: 0
			}
		},
		markers: {
			size: 0
		},
		colors: dealTypeChartsColors,
		xaxis: {
			categories: ['2016', '2017', '2018', '2019', '2020', '2021']
		}
	};
	onMount(() => {
		chart = new ApexCharts(document.querySelector("#dealtypechart"), options)
  		chart.render()
	})
</script>

<div id="dealtypechart" class="apex-charts" dir="ltr"></div>