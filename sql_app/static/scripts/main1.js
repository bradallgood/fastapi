

const myHeading = document.querySelector("h1");
myHeading.textContent = "Hello world!";

const apiUrl = 'http://localhost:8000/passing';

const dropdown = document.getElementById('dropdown');

// Function to populate the dropdown from API response
async function populateDropdown() {
  console.log('In populateDropdown')
  var data = await fetchData();
  console.log(data)
  data.forEach(item => {
    const option = document.createElement('option');
    option.value = item.NAME; // Assuming the API response contains an 'id' field
    option.textContent = item.NAME; // Assuming the API response contains a 'name' field
    dropdown.appendChild(option);
  });
}

// Function to fetch data from the API
async function fetchData() {
    try {
        const response = await fetch(apiUrl);
        var data = await response.json();
        return data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
}


// Function to populate the table with data
async function populateTable() {
    const data = await fetchData();
    const tableBody = document.getElementById('table-body');
    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${item.RK}</td>
          <td>${item.NAME}</td>
          <td>${item.POSITION}</td>
          <td>${item.TEAM}</td>
          <td>${item.YDS}</td>
        `;
        tableBody.appendChild(row);
        });
}


window.onload =  function() {
    populateDropdown();
    populateTable();
}
//window.onload = populateTable
