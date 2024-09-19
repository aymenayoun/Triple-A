const renderChart=(data,labels)=>{
    const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: labels,
    datasets: [{
      label: '6 months of expenses',
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
        text: 'Expenses by category',
    }
  }
});
}

const getChartData=()=>{
    fetch('expense_category_summary').then(res=>res.json()).then(results=>{
        console.log('results',results)
        const category_data=results.expense_category_data
        const [labels,data] = [Object.keys(category_data),Object.values(category_data)]
        renderChart(data,labels)
    })
}
document.onload=getChartData()