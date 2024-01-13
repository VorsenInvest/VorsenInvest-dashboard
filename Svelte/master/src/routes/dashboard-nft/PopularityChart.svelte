<script>
    import { onMount } from "svelte";
    import { browser } from "$app/environment";
    export let dataColors;
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
		default: ["--vz-success", "--vz-warning"],
		minimal: ["--vz-gray-200", "--vz-primary"],
		corporate: ["--vz-success", "--vz-secondary"],
		galaxy: ["--vz-primary-rgb, 0.65", "--vz-primary"], 
		creative: ["--vz-success", "--vz-warning"],
		classic: ["--vz-success", "--vz-warning"],
		modern: ["--vz-success", "--vz-warning"],
		interactive: ["--vz-success", "--vz-warning"],
		vintage: ["--vz-success", "--vz-warning"],
		saas: ["--vz-success", "--vz-warning"],
		material: ["--vz-success", "--vz-warning"],
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

    var PopularityChartColors = getChartColorsArray(dataColors);

    const options = {
        chart: {
            type: "bar",
            height: 260,
            stacked: true,
            toolbar: {
                show: false,
            },
        },
        series: [
            {
                name: "Like",
                data: [12.45, 16.2, 8.9, 11.42, 12.6, 18.1, 18.2, 14.16],
            },
            {
                name: "Share",
                data: [
                    -11.45, -15.42, -7.9, -12.42, -12.6, -18.1, -18.2, -14.16,
                ],
            },
        ],
        plotOptions: {
            bar: {
                columnWidth: "20%",
                borderRadius: [4, 4],
            },
        },
        dataLabels: {
            enabled: false,
            textAnchor: "top",
        },
        colors: PopularityChartColors,

        fill: {
            opacity: 1,
        },
        legend: {
            position: "top",
            horizontalAlign: "right",
        },
        yaxis: {
            labels: {
                show: false,
                formatter: function (y) {
                    return y.toFixed(0) + "%";
                },
            },
        },
        xaxis: {
            categories: [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
            ],
            labels: {
                rotate: -90,
            },
        },
    };

    onMount(() => {
        chart = new ApexCharts(
            document.querySelector("#populariychartcharts"),
            options
        );
        chart.render();
    });
</script>

<div id="populariychartcharts" class="apex-charts mt-n4" dir="ltr" />
