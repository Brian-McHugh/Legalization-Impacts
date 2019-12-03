async function makePlot(){
    //const defaultURL = "/emoji_char";
    //let data = await d3.json(defaultURL);
    //data = [data];
    var chart = c3.generate({
        bindto: '#chart',
        data: {
            x: 'State',
            columns: [
                ['State', 1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56],
                ['Total_under18', 3578, 1687, 20478, 7697, 42958, 17906, 7106, 2851, 505, 48213, 15400, 1762, 5993, 7366, 8831, 1639, 2985, 16533, 2845, 17825, 4508, 13267, 19391, 2453, 15560, 3722, 6985, 10026, 3283, 11513, 3203, 14434, 11088, 4009, 20003, 7701, 8618, 36034, 2373, 10803, 4886, 19692, 55458, 12307, 702, 15864, 10996, 496, 35109, 3191],
                ['drug_violations_under18', 130, 183, 3239, 925, 2967, 2257, 489, 279, 10, 5399, 2053, 337, 928, 834, 1155, 202, 257, 1496, 304, 2046, 132, 1668, 1698, 190, 2018, 358, 1006, 1244, 344, 2769, 472, 2643, 1414, 429, 1675, 1146, 1653, 3231, 104, 1957, 819, 2380, 9893, 2258, 38, 2132, 1053, 67, 3150, 580],
                ['Total_all_ages', 126404, 30620, 256785, 120240, 1093080, 193216, 95709, 28742, 13682, 715424, 200643, 24487, 52292, 86947, 125536, 126404, 30620, 256785, 120240, 1093080, 193216, 95709, 28742, 13682, 715424, 200643, 24487, 52292, 86947, 125536],
                ['drug_violations_allages', 8217, 1046, 32272, 17954, 219251, 16172, 8087, 3707, 290, 134142, 37291, 1873, 8777, 17060, 25058, 2242, 19355, 30437, 3692, 31914, 7125, 30320, 20404, 8003, 32982, 2732, 8993, 11238, 6522, 48008, 5375, 69571, 26936, 5448, 39708, 17766, 13605, 61934, 2049, 34105, 8108, 47876, 139188, 19562, 902, 45409, 11283, 6044, 31066, 4895],
            ],
            axis: {
                x: {
                    type: 'category',
                    categories: ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'DC', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
                }
            },
            type: 'bar',
            types: {
                Total_under18: 'line',
                Total_all_ages: 'spline',
            },
            groups: [
                ['drug_violations_allages','drug_violations_under18']
            ]
        }
    });
}

//function updatePlotly(newdata) {
//    Plotly.restyle("bar", "x", [newdata.x]);
//    Plotly.restyle("bar", "y", [newdata.y]);
//}

// Get new data whenever the dropdown selection changes
//async function getData(route) {
//    console.log(route);
//    let data = await d3.json(`/${route}`);
//    updatePlotly(data);
//}

makePlot();
  