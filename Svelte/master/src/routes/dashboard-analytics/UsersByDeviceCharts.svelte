<script>
    import { onMount } from "svelte";
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

    const dountchartUserDeviceColors = getChartColorsArray(dataColors);

    const THEME_CHART_COLORS = {
		default: ["--vz-primary", "--vz-warning", "--vz-info"],
		minimal: ["--vz-primary", "--vz-primary-rgb, 0.60", "--vz-primary-rgb, 0.75"],
		modern: ["--vz-primary", "--vz-warning", "--vz-info"],
		interactive: ["--vz-primary", "--vz-warning", "--vz-info"],
		creative: ["--vz-primary", "--vz-warning", "--vz-info"],
		corporate: ["--vz-primary", "--vz-warning", "--vz-info"],
		galaxy: ["--vz-primary", "--vz-primary-rgb, .75", "--vz-primary-rgb, 0.60"], 
		classic: ["--vz-primary", "--vz-warning", "--vz-info"],
		vintage: ["--vz-primary", "--vz-warning", "--vz-info"],
		saas: ["--vz-primary", "--vz-warning", "--vz-info"]
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


    const options = {
        labels: ["Desktop", "Mobile", "Tablet"],
        chart: {
            type: "donut",
            height: 219,
        },
        series: [78.56, 105.02, 42.89],
        plotOptions: {
            pie: {
                size: 100,
                donut: {
                    size: "76%",
                },
            },
        },
        dataLabels: {
            enabled: false,
        },
        legend: {
            show: false,
            position: "bottom",
            horizontalAlign: "center",
            offsetX: 0,
            offsetY: 0,
            markers: {
                width: 20,
                height: 6,
                radius: 2,
            },
            itemMargin: {
                horizontal: 12,
                vertical: 0,
            },
        },
        stroke: {
            width: 0,
        },
        yaxis: {
            labels: {
                formatter: function (value) {
                    return value + "k Users";
                },
            },
            tickAmount: 4,
            min: 0,
        },
        colors: dountchartUserDeviceColors,
    };
    onMount(() => {
            chart = new ApexCharts(
            document.querySelector("#userbtdevicechart"),
            options
        );
        chart.render();
    });
</script>

<div id="userbtdevicechart" class="apex-charts" dir="ltr" />
