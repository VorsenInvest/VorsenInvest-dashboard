<script>
    import { themeChangeEvent } from "$lib/eventBus";
    export let latitude;
    export let longitude;
    export let dataColor;
    export let MapType;
    let map;
    let center = { lat: latitude, lng: longitude };

    import { onMount } from "svelte";
    import { browser } from "$app/environment";

    function getChartColorsArray(colors) {
        if (browser) {
            return colors.map(function (value) {
                var newValue = value.replace(" ", "");
                if (newValue.indexOf(",") === -1) {
                    var color = getComputedStyle(
                        document.documentElement,
                    ).getPropertyValue(newValue);
                    if (color.indexOf("#") !== -1)
                        color = color.replace(" ", "");
                    if (color) return color;
                    else return newValue;
                } else {
                    var val = value.split(",");
                    if (val.length === 2) {
                        var rgbaColor = getComputedStyle(
                            document.documentElement,
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

    let vectorMapWorldMarkersColors = getChartColorsArray(dataColor);

    const THEME_CHART_COLORS = {
        default: ["--vz-light", "--vz-success", "--vz-primary"],
        interactive: ["--vz-light", "--vz-info", "--vz-primary"],
        minimal: ["--vz-light", "--vz-success", "--vz-primary"],
        creative: ["--vz-light", "--vz-success", "--vz-primary"],
        corporate: ["--vz-light", "--vz-success", "--vz-primary"],
        galaxy: ["--vz-light", "--vz-success", "--vz-primary"],
        classic: ["--vz-light", "--vz-success", "--vz-primary"],
        modern: ["--vz-light", "--vz-success", "--vz-primary"],
        vintage: ["--vz-light", "--vz-success", "--vz-primary"],
        saas: ["--vz-light", "--vz-success", "--vz-primary"],
        material: ["--vz-light", "--vz-success", "--vz-primary"],
    };

    // Function to find the index of a key
    function findIndexByKey(key) {
        const keys = Object.keys(THEME_CHART_COLORS);
        return keys.indexOf(key);
    }

    // Subscribe to the theme change event
    const unsubscribeEvent = themeChangeEvent.subscribe((newTheme) => {
        // Handle the theme change event
        if (newTheme == null || newTheme == undefined) {
            return;
        }
        let key = findIndexByKey(newTheme);
        let newColors;
        if (key >= 0) {
            newColors = THEME_CHART_COLORS[newTheme];
        }
        if (browser) {
            newColors = key >= 0 ? getChartColorsArray(newColors) : dataColor;
            setTimeout(() => {
                vectorMapWorldMarkersColors = newColors;
                loadChart();
            }, 500);
        }
    });

    function loadChart() {
        if (MapType == "world") {
            document.querySelector(".full-screen").innerHTML = "";
            map = new jsVectorMap({
                selector: document.querySelector(".full-screen"),
                map: "world",
                zoomOnScroll: false,
                zoomButtons: false,
                showTooltip: false,
                regionStyle: {
                    initial: {
                        stroke: "#9599ad",
                        strokeWidth: 0.25,
                        fill: vectorMapWorldMarkersColors[0],
                        fillOpacity: 1,
                    },
                },
                markersSelectable: true,
                selectedMarkers: [0, 5],
                markers: [
                    {
                        name: "Palestine",
                        coords: [31.9474, 35.2272],
                    },
                    {
                        name: "Russia",
                        coords: [61.524, 105.3188],
                    },
                    {
                        name: "Canada",
                        coords: [56.1304, -106.3468],
                    },
                    {
                        name: "Greenland",
                        coords: [71.7069, -42.6043],
                    },
                ],
                markerStyle: {
                    initial: {
                        fill: vectorMapWorldMarkersColors[1],
                    },
                    selected: {
                        fill: vectorMapWorldMarkersColors[2],
                    },
                },
                labels: {
                    markers: {
                        render: function (marker) {
                            return marker.name;
                        },
                    },
                },
            });
        } else if (MapType == "world_merc") {
            document.querySelector(".full-screen").innerHTML = "";
            map = new jsVectorMap({
                selector: document.querySelector(".full-screen"),
                map: "world",
                zoomOnScroll: false,
                zoomButtons: false,
                showTooltip: false,
                regionStyle: {
                    initial: {
                        stroke: "#9599ad",
                        strokeWidth: 0.25,
                        fill: vectorMapWorldMarkersColors[0],
                        fillOpacity: 1,
                    },
                },
                markers: [
                    {
                        name: "Greenland",
                        coords: [72, -42],
                    },
                    {
                        name: "Canada",
                        coords: [56.1304, -106.3468],
                    },
                    {
                        name: "Brazil",
                        coords: [-14.235, -51.9253],
                    },
                    {
                        name: "Egypt",
                        coords: [26.8206, 30.8025],
                    },
                    {
                        name: "Russia",
                        coords: [61, 105],
                    },
                    {
                        name: "China",
                        coords: [35.8617, 104.1954],
                    },
                    {
                        name: "United States",
                        coords: [37.0902, -95.7129],
                    },
                    {
                        name: "Norway",
                        coords: [60.472024, 8.468946],
                    },
                    {
                        name: "Ukraine",
                        coords: [48.379433, 31.16558],
                    },
                ],
                lines: [
                    {
                        from: "Canada",
                        to: "Egypt",
                    },
                    {
                        from: "Russia",
                        to: "Egypt",
                    },
                    {
                        from: "Greenland",
                        to: "Egypt",
                    },
                    {
                        from: "Brazil",
                        to: "Egypt",
                    },
                    {
                        from: "United States",
                        to: "Egypt",
                    },
                    {
                        from: "China",
                        to: "Egypt",
                    },
                    {
                        from: "Norway",
                        to: "Egypt",
                    },
                    {
                        from: "Ukraine",
                        to: "Egypt",
                    },
                ],
                lineStyle: {
                    animation: true,
                    strokeDasharray: "6 3 6",
                },
            });
        }
    }

    onMount(async () => {
        loadChart();
    });
</script>

<div class="full-screen" />

<style>
    .full-screen {
        width: 100%;
        height: 100%;
    }
</style>
