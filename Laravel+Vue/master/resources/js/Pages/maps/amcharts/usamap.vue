<script>
import * as am5 from "@amcharts/amcharts5";
import * as am5map from "@amcharts/amcharts5/map";
import am5geodata_worldLow from "@amcharts/amcharts5-geodata/worldLow";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";

export default {
    methods: {
        usaMapChart() {
            // Set usa amchart
            let USARoot = am5.Root.new("usaMapChartDiv");

            USARoot.setThemes([am5themes_Animated.new(USARoot)]);


            let USAChart = USARoot.container.children.push(
                am5map.MapChart.new(USARoot, {
                    panX: "none",
                    panY: "none",
                    opacity: 1,
                    projection: am5map.geoAlbersUsa(),
                })
            );

            USAChart.series.push(
                am5map.MapPolygonSeries.new(USARoot, {
                    geoJSON: am5geodata_worldLow,
                    include: ["US"],
                    fill: am5.color("rgb(222, 226, 232)"),
                    // stroke: am5.color("#fff"),
                })
            );


            // Create series for labels
            var pointSeries = USAChart.series.push(
                am5map.MapPointSeries.new(USARoot, {
                    polygonIdField: "polygonId"
                })
            );

            pointSeries.bullets.push(function () {
                return am5.Bullet.new(root, {
                    sprite: am5.Label.new(root, {
                        fontSize: 10,
                        centerX: am5.p50,
                        centerY: am5.p50,
                        text: "{name}",
                        populateText: true
                    })
                });
            });
        }
    },
    mounted() {
        this.usaMapChart();
    }
};
</script>

<template>
    <div id="usaMapChartDiv" style="height: 420px"></div>
</template>
