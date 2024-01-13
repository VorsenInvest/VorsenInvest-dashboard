<script>
    import mapStyles from "../../common/data/map-styles"; // optional
    export let latitude;
    export let longitude;
    export let dataColor;
    export let MapType;
    let container;
    let map;
    let zoom = 8;
    let center = { lat: latitude, lng: longitude };

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
        // console.log(MapType)
        // map = new google.maps.Map(container, {
        //     zoom,
        //     center,
        //     styles: mapStyles, // optional
        // });
        if (MapType == "world") {
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
        } else if (MapType == "world_merc") {
           
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
                markers: [{
                    name: "Greenland",
                    coords: [72, -42]
                },
                {
                    name: "Canada",
                    coords: [56.1304, -106.3468]
                },
                {
                    name: "Brazil",
                    coords: [-14.2350, -51.9253]
                },
                {
                    name: "Egypt",
                    coords: [26.8206, 30.8025]
                },
                {
                    name: "Russia",
                    coords: [61, 105]
                },
                {
                    name: "China",
                    coords: [35.8617, 104.1954]
                },
                {
                    name: "United States",
                    coords: [37.0902, -95.7129]
                },
                {
                    name: "Norway",
                    coords: [60.472024, 8.468946]
                },
                {
                    name: "Ukraine",
                    coords: [48.379433, 31.16558]
                },
                ],
                lines: [{
                    from: "Canada",
                    to: "Egypt"
                },
                {
                    from: "Russia",
                    to: "Egypt"
                },
                {
                    from: "Greenland",
                    to: "Egypt"
                },
                {
                    from: "Brazil",
                    to: "Egypt"
                },
                {
                    from: "United States",
                    to: "Egypt"
                },
                {
                    from: "China",
                    to: "Egypt"
                },
                {
                    from: "Norway",
                    to: "Egypt"
                },
                {
                    from: "Ukraine",
                    to: "Egypt"
                },
                ],
                lineStyle: {
                    animation: true,
                    strokeDasharray: "6 3 6",
                },
            })
        }
    });
</script>

<div class="full-screen" />

<style>
    .full-screen {
        width: 100%;
        height: 100%;
    }
</style>