async function makePlot(){
  const defaultURL = "/arrestprispop";
  let data = await d3.json(defaultURL);
  data = [data];
  const layout = { margin: { t: 30, b: 100 } };
  Plotly.plot("fig", data, layout);
}

function updatePlotly(newdata) {
  Plotly.restyle("fig", "x", [newdata.x]);
  Plotly.restyle("fig", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
async function getData(route) {
  console.log(route);
  let data = await d3.json(`/${route}`);
  updatePlotly(data);
}

makePlot();