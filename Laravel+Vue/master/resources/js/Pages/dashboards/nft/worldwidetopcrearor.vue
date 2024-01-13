<script>

import * as am5 from "@amcharts/amcharts5";
import * as am5map from "@amcharts/amcharts5/map";
import am5geodata_worldLow from "@amcharts/amcharts5-geodata/worldLow";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";

export default {
    mounted() {
        this.initialMap();
    },
    methods: {
        initialMap() {
            // Create a chart instance
            const root = am5.Root.new("users-by-country");
            root.setThemes([am5themes_Animated.new(root)]);
            let chart = root.container.children.push(
                am5map.MapChart.new(root, {
                    panX: "none",
                    panY: "none",
                    opacity: 1,
                    projection: am5map.geoMercator(),
                })
            );

            chart.series.push(
                am5map.MapPolygonSeries.new(root, {
                    geoJSON: am5geodata_worldLow,
                    exclude: ["AQ"],
                    fill: am5.color("rgb(222, 226, 232)"),
                    stroke: am5.color("#fff"),
                })
            );

            let colorset = am5.ColorSet.new(root, {});
            // Create point series
            var pointSeries = chart.series.push(
                am5map.MapPointSeries.new(root, {})
            );

            pointSeries.bullets.push(function () {
                return am5.Bullet.new(root, {
                    sprite: am5.Circle.new(root, {
                        radius: 4,
                        stroke: colorset.next(),
                        strokeWidth: 6,
                        strokeOpacity: 0.5,
                        fill: colorset.next(),
                        fillOpacity: 1,
                        tooltipText: "{title}",
                        cursorOverStyle: 'pointer',
                    }),
                });
            });

            pointSeries.pushDataItem({ title: "United States", latitude: 37.0902, longitude: -95.7129 });
            pointSeries.pushDataItem({ title: "Russia", latitude: 61.5240, longitude: 105.3188 });
            pointSeries.pushDataItem({ title: "Spain", latitude: 40.4637, longitude: -3.7492 });
            pointSeries.pushDataItem({ title: "Italy", latitude: 41.8719, longitude: 12.5674 });
            pointSeries.pushDataItem({ title: "Germany", latitude: 51.1657, longitude: 10.4515 });


            // adding zoom control
            // chart.set("zoomControl", am5map.ZoomControl.new(root, {}));
        },
    },
};
</script>
<template>
    <BCard no-body>
        <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Worldwide Top Creators</BCardTitle>
            <div class="flex-shrink-0">
                <BButton type="button" variant="soft-primary" size="sm" class="material-shadow-none"> 
                    Export Report
                </BButton>
            </div>
        </BCardHeader>

        <BCardBody>

            <!-- <div id="users-by-country" style="height: 269px"></div> -->
            <div id="users-by-country" class="chart-container" style="height: 269px; width:auto"></div>
            <div class="mt-1">
                <p class="mb-1 d-flex bd-highlight"><img src="@assets/images/flags/us.svg" alt="" height="15" class="rounded bd-highlight me-2"> United
                    States <span class="ms-auto bd-highlight">34%</span></p>
                <p class="mb-1 d-flex bd-highlight"><img src="@assets/images/flags/russia.svg" alt="" height="15" class="rounded bd-highlight me-2">
                    Russia <span class="ms-auto bd-highlight">27%</span></p>
                <p class="mb-1 d-flex bd-highlight"><img src="@assets/images/flags/spain.svg" alt="" height="15" class="rounded bd-highlight me-2">
                    Spain
                    <span class="ms-auto bd-highlight">21%</span>
                </p>
                <p class="mb-1 d-flex bd-highlight"><img src="@assets/images/flags/italy.svg" alt="" height="15" class="rounded bd-highlight me-2">
                    Italy
                    <span class="ms-auto bd-highlight">13%</span>
                </p>
                <p class="mb-0 d-flex bd-highlight"><img src="@assets/images/flags/germany.svg" alt="" height="15" class="rounded bd-highlight me-2">
                    Germany <span class="ms-auto bd-highlight">5%</span></p>
            </div>
        </BCardBody>
    </BCard>
</template>