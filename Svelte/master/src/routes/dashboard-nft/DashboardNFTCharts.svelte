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

    var MarketplaceChartColors = getChartColorsArray(dataColors);

    const THEME_CHART_COLORS = {
		default: ["--vz-primary","--vz-success", "--vz-light"],
		corporate: ["--vz-primary","--vz-secondary", "--vz-light"],
		galaxy: ["--vz-primary","--vz-success", "--vz-secondary"], 
		classic: ["--vz-primary","--vz-light", "--vz-secondary"],
		minimal: ["--vz-primary","--vz-success", "--vz-light"],
		creative: ["--vz-primary","--vz-success", "--vz-light"],
		modern: ["--vz-primary","--vz-success", "--vz-light"],
		interactive: ["--vz-primary","--vz-success", "--vz-light"],
		vintage: ["--vz-primary","--vz-success", "--vz-light"],
		saas: ["--vz-primary","--vz-success", "--vz-light"],
		material: ["--vz-primary","--vz-success", "--vz-light"],
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
            id:"dashboardnftcharts",
            height: 350,
            type: "line",
            zoom: {
                enabled: false,
            },
            toolbar: {
                show: false,
            },
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 3,
        },
        series: [{
            name: "Artwork",
            data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
        },
        {
            name: "Auction",
            data: [40, 120, 83, 45, 31, 74, 35, 34, 78]
        },
        {
            name: "Creators",
            data: [95, 35, 20, 130, 64, 22, 43, 45, 31]
        }],
        colors: MarketplaceChartColors,
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
                "Sep",
            ],
        },
    };

    onMount(() => {
        chart = new ApexCharts(document.querySelector("#dashboardnftcharts"),options);
        chart.render();
    });
</script>

<div id="dashboardnftcharts" class="apex-charts" dir="ltr" />
