const searchField = document.querySelector('#searchField');
const tableOutput=document.querySelector('.table-output');
const appTable=document.querySelector('.app-table');
const paginationContainer=document.querySelector('.pagination-container')
const tbody=document.querySelector('.output-body')
paginationContainer.style.display='block'
appTable.style.display='block';
tableOutput.style.display='none';

searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    paginationContainer.style.display='block'
    appTable.style.display='block';
    tableOutput.style.display='none';
    if (searchValue.trim().length > 0) {
        console.log('searchValue', searchValue);
        tbody.innerHTML='';
        fetch('search-expenses/', {
            body: JSON.stringify({ searchText: searchValue }),
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'  // Include CSRF token if required
            }
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            appTable.style.display='none';
            tableOutput.style.display='block';
            paginationContainer.style.display='none'
            if (data.length===0){
                tableOutput.innerHTML='<tr><td colspan="5">No results found</td></tr>';
                return;
            }
            else{
                let tableHtml='';
                data.forEach((expense) => {
                    tableHtml+=`
                    <tr>
                        <td>${expense.amount} </td>
                        <td>${expense.category}</td>
                        <td>${expense.description}</td>
                        <td>${expense.date}</td>
                    </tr>
                    `;
                });
                tbody.innerHTML=tableHtml;
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    } else {
        console.log('Empty search input');
    }
});
