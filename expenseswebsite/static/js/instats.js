const renderChart=(data,labels)=>{
    const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: labels,
    datasets: [{
      label: '6 months of incomes',
      data: data,
      backgroundColor:[
        "rgba(255, 0, 0, 0.45)",
        "rgba(41, 39, 245, 0.45)",
        "rgba(194, 255, 0, 0.45)",
        "rgba(35, 255, 0, 0.45)",
        "rgba(140, 0, 142, 0.45)",
        "rgba(255, 141, 0, 0.45)",
      ],
      borderColor:[
        "rgba(255, 0, 0, 0.45)",
        "rgba(41, 39, 245, 0.45)",
        "rgba(194, 255, 0, 0.45)",
        "rgba(35, 255, 0, 0.45)",
        "rgba(140, 0, 142, 0.45)",
        "rgba(255, 141, 0, 0.45)",
      ],
      borderWidth: 1
    }]
  },
  options: {
    title:{
        display:true,
        text: 'Income by Source',
    }
  }
});
}

const getChartData = () => {
    fetch('income_source_summary')
    .then(res => res.json())
    .then(results => {
        console.log('results', results);
        const source_data = results.income_source_data;
        const [labels, data] = [Object.keys(source_data), Object.values(source_data)];
        renderChart(data, labels);
    })
    .catch(err => {
        console.error('Error fetching chart data:', err);
    });
};

document.onload = getChartData();
