<script>
import * as am5 from "@amcharts/amcharts5";
import * as am5map from "@amcharts/amcharts5/map";
import am5geodata_worldLow from "@amcharts/amcharts5-geodata/worldLow";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";

export default {
    methods: {
        pacificMap() {
            // Set canada amchart
            let pacificRoot = am5.Root.new("pacificMapDiv");

            pacificRoot.setThemes([am5themes_Animated.new(pacificRoot)]);


            let pacificChart = pacificRoot.container.children.push(
                am5map.MapChart.new(pacificRoot, {
                    panX: "rotateX",
                    panY: "none",
                    opacity: 1,
                    projection: am5map.geoNaturalEarth1(),
                })
            );

            let polygonSeries = pacificChart.series.push(
                am5map.MapPolygonSeries.new(pacificRoot, {
                    geoJSON: am5geodata_worldLow,
                })
            );

            let colorset = am5.ColorSet.new(pacificRoot, {});
            let i = 0;
            polygonSeries.mapPolygons.template.adapters.add("fill", function (fill, target) {
                if (i < 10) {
                    i++;
                }
                else {
                    i = 0;
                }
                let dataContext = target.dataItem.dataContext;
                if (!dataContext.colorWasSet) {
                    dataContext.colorWasSet = true;
                    let color = am5.Color.saturate(colorset.getIndex(i), 0.3);
                    target.setRaw("fill", color);
                    return color;
                }
                else {
                    return fill;
                }
            })

            polygonSeries.mapPolygons.template.states.create("hover", { fillOpacity: 1 });


            polygonSeries.mapPolygons.template.setAll({
                tooltipText: "{name}",
                fillOpacity: 0.8,
            })

            var graticuleSeries = pacificChart.series.insertIndex(0,
                am5map.GraticuleSeries.new(pacificRoot, {})
            );

            graticuleSeries.mapLines.template.setAll({
                stroke: am5.color('#74788d'),
                strokeOpacity: 0.2
            });

            var backgroundSeries = pacificChart.series.unshift(
                am5map.MapPolygonSeries.new(pacificRoot, {})
            );

            backgroundSeries.mapPolygons.template.setAll({
                fill: am5.color('#fff'),
                stroke: am5.color('#fff'),
            });

            backgroundSeries.data.push({
                geometry: am5map.getGeoRectangle(90, 180, -90, -180)
            });
        }
    },
    mounted() {
        this.pacificMap();
    }
};
</script>

<template>
    <div id="pacificMapDiv" style="height: 420px"></div>
</template>
