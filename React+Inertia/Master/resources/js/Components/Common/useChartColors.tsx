import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { createSelector } from 'reselect';
import getChartColorsArray from './DynamicChartsColor';

const useChartColors = (chartId: any) => {
  const [chartColors, setChartColors] = useState([]);

  const selectLayoutState = (state: any) => state.Layout;
  const selectLayoutProperties = createSelector(
    selectLayoutState,
    (layout: any) => ({
      layoutThemeType: layout.layoutThemeType,
      layoutThemeColorType: layout.layoutThemeColorType
    })
    
  );
  // Inside your component
  const {layoutThemeType, layoutThemeColorType} = useSelector(selectLayoutProperties);

  useEffect(() => {
    const colors = getChartColorsArray(chartId);
    setChartColors(colors);
  }, [chartId, layoutThemeType, layoutThemeColorType]);

  return chartColors;
};

export default useChartColors;
