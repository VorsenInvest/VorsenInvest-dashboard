<script>
	import {onMount} from 'svelte'; 
    export let dataColors;
    import { browser } from "$app/environment";
    import { themeChangeEvent } from "$lib/eventBus";
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

    const THEME_CHART_COLORS = {
		default: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
		minimal: ["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.70", "--vz-primary-rgb, 0.50"],
		galaxy: ["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.70", "--vz-primary-rgb, 0.50"], 
		creative: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
		corporate: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
		classic: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
		modern: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
		interactive: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
		vintage: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
		saas: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
		material: ["--vz-success", "--vz-primary", "--vz-warning", "--vz-danger"],
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

    const donutchartProjectsStatusColors = getChartColorsArray(dataColors);
    var options = {
        labels: ["Completed", "In Progress", "Yet to Start", "Cancelled"],
        chart: {
            type: "donut",
            height: 230,
        },
        series : [125, 42, 58, 89],
        plotOptions: {
            pie: {
                size: 100,
                offsetX: 0,
                offsetY: 0,
                donut: {
                    size: "90%",
                    labels: {
                        show: false,
                    }
                },
            },
        },
        dataLabels: {
            enabled: false,
        },
        legend: {
            show: false,
        },
        stroke: {
            lineCap: "round",
            width: 0
        },
        colors: donutchartProjectsStatusColors,
    };
	onMount(() => {
		 chart = new ApexCharts(document.querySelector("#prjectstatuscharts"), options)
  		chart.render()
	})
</script>

<div id="prjectstatuscharts" class="apex-charts" dir="ltr"></div>