<script>
    import mapStyles from "../../common/data/map-styles"; // optional
    import usimg from "./../../assets/images/flags/us.svg";
    import russiaimg from "./../../assets/images/flags/russia.svg";
    import spainimg from "./../../assets/images/flags/spain.svg";
    import italyimg from "./../../assets/images/flags/italy.svg";
    import germanyimg from "./../../assets/images/flags/germany.svg";
    export let dataColor;
    let map;

    import { onMount } from "svelte";
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

    const vectorMapWorldMarkersColors = getChartColorsArray(dataColor)
    onMount(async () => {

        // if (MapType == "world") {
        map = new jsVectorMap({
            selector: document.querySelector(".full-screen"),
            map: 'world',
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
            markers: [{
                name: "United States",
                coords: [37.0902, 95.7129],
                style: {
                    image: usimg,
                }
            },
            {
                name: "Russia",
                coords: [61.524, 105.3188],
                style: {
                    image: russiaimg,
                }
            },
            {
                name: "Spain",
                coords: [40.4637, 3.7492],
                style: {
                    image: spainimg,
                }
            },
            {
                name: "Italy",
                coords: [41.8719, 12.5674],
                style: {
                    image: italyimg,
                }
            },
            {
                name: "Germany",
                coords: [51.1657, 10.4515],
                style: {
                    image: germanyimg,
                }
            },
            ],
            markerStyle: {
                initial: {
                    fill: vectorMapWorldMarkersColors[1],
                },
                selected: {
                    fill: vectorMapWorldMarkersColors[2]
                }
            },
            labels: {
                markers: {
                    render: function (marker) {
                        return marker.name;
                    },
                },
            },
        })
        // } 
    });
</script>

<div class="full-screen" />

<style>
    .full-screen {
        width: 100%;
        height: 100%;
    }
</style>