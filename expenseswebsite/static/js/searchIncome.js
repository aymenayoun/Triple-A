const searchField = document.querySelector('#searchField');
const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');
const paginationContainer = document.querySelector('.pagination-container');
const tbody = document.querySelector('.output-body');

paginationContainer.style.display = 'block';
appTable.style.display = 'block';
tableOutput.style.display = 'none';

searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    paginationContainer.style.display = 'block';
    appTable.style.display = 'block';
    tableOutput.style.display = 'none';

    if (searchValue.trim().length > 0) {
        tbody.innerHTML = '';
        fetch('search-income/', {
            body: JSON.stringify({ searchText: searchValue }),
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            }
        })
        .then((res) => res.json())
        .then((data) => {
            appTable.style.display = 'none';
            tableOutput.style.display = 'block';
            paginationContainer.style.display = 'none';

            if (data.length === 0) {
                tableOutput.innerHTML = '<tr><td colspan="5">No results found</td></tr>';
                return;
            }

            let tableHtml = '';
            data.forEach((income) => {
                tableHtml += `
                    <tr>
                        <td>${income.amount}</td>
                        <td>${income['source__name']}</td> <!-- Access source name -->
                        <td>${income.description}</td>
                        <td>${income.date}</td>
                    </tr>
                `;
            });
            tbody.innerHTML = tableHtml;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    } else {
        console.log('Empty search input');
    }
});
