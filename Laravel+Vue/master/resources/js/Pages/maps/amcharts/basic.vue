<script>
import * as am5 from "@amcharts/amcharts5";
import * as am5map from "@amcharts/amcharts5/map";
import am5geodata_worldLow from "@amcharts/amcharts5-geodata/worldLow";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";

export default {
    methods: {
        basicChart() {
            // Create a chart instance
            const root = am5.Root.new("basicChartDiv");
            root.setThemes([am5themes_Animated.new(root)]);
            // Set map definition
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

            // Create map polygon series
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

            pointSeries.pushDataItem({ title: "Greenland", latitude: 71.7069, longitude: -42.6043 });
            pointSeries.pushDataItem({ title: "Russia", latitude: 61.5240, longitude: 105.3188 });
            pointSeries.pushDataItem({ title: "Canada", latitude: 56.1304, longitude: -106.3468 });

            // adding zoom control
            chart.set("zoomControl", am5map.ZoomControl.new(root, {}));

        }
    },
    mounted() {
        this.basicChart();
    }
};
</script>

<template>
    <div id="basicChartDiv" style="height: 420px"></div>
</template>
