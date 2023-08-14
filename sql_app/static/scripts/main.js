

const myHeading = document.querySelector("h1");
myHeading.textContent = "Hello world!";

const apiUrl = 'http://localhost:8000/passing';

const dropdown = document.getElementById('dropdown');

// Function to populate the dropdown from API response
async function populateDropdown() {
  console.log('In populateDropdown')
  var data1 = await fetchData();
  console.log(data1)
  data1.forEach(item => {
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

      var trace1 = {
        x: data.map(g_item => g_item.ATT),
        y: data.map(g_item => g_item.NAME),
        name: 'Attempts',
        type: 'bar',
        orientation: 'h'
      };
      
      var trace2 = {
        x: data.map(g_item => g_item.COMP),
        y: data.map(g_item => g_item.NAME),
        name: 'Completions',
        type: 'bar',
        orientation: 'h'
      };
      
      var g_data = [trace1, trace2];
      
      var layout = {
        barmode: 'group',
        width: 500,
        height: 700,
        margin: {
            l: 100,
            r: 20,
            t: 70,
            b: 70
          },
        title: "Week 1: Att vs Comp"
      };
      
      Plotly.newPlot('COMPATT', g_data, layout);

      var trace1 = {
        x: data.map(g_item => g_item.TD),
        y: data.map(g_item => g_item.NAME),
        name: 'TDs',
        type: 'bar',
        orientation: 'h'
      };
      
      var trace2 = {
        x: data.map(g_item => g_item.INT),
        y: data.map(g_item => g_item.NAME),
        name: 'Interceptions',
        type: 'bar',
        orientation: 'h'
      };
      
      var g_data = [trace1, trace2];
      
      var layout = {
        barmode: 'group',
        width: 500,
        height: 700,
        margin: {
            l: 100,
            r: 20,
            t: 70,
            b: 70
          },
        title: "Week 1: TD vs INTsp"
      };
      
      Plotly.newPlot('TDINT', g_data, layout);


      var trace1 = {
        x: data.map(g_item => g_item.YDS),
        y: data.map(g_item => g_item.NAME),
        name: 'YDS',
        type: 'bar',
        orientation: 'h'
      };
    
      
      var g_data = [trace1];
      
      var layout = {
        width: 500,
        height: 700,
        margin: {
            l: 100,
            r: 20,
            t: 70,
            b: 70
          },
        title: "Week 1: Passing YDS"
      };
      
      Plotly.newPlot('PassingYDS', g_data, layout);

}

window.onload = populateTable;
console.log("Calling populateDropdown")
populateDropdown;
