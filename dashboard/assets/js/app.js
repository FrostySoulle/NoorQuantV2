fetch("/data/research_data.csv")
.then(response => response.text())
.then(csv => {

    const rows = csv.trim().split("\n");
    const dataRows = rows.slice(1);
    
    const tbody = document.getElementById("research-table-body");

    let bestRS = -999;
    let bestStock = "";

    let worstRS = 999;
    let worstStock = "";

    let totalRS = 0;
    let countRS = 0;

    dataRows.forEach(row => {

        const cols = row.split(",");

        const rs = parseFloat(cols[8]);

        if (rs > bestRS) {
            bestRS = rs;
            bestStock = cols[1];
        }

        if (rs < worstRS) {
            worstRS = rs;
            worstStock = cols[1];
        }

        totalRS += rs;
        countRS++;

        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${cols[0]}</td>
            <td>${cols[1]}</td>
            <td>${cols[6]}</td>
            <td>${cols[7]}</td>
            <td>${cols[8]}</td>
            <td>${cols[9]}</td>  
            <td>${cols[10]}</td>
        `;

        tbody.appendChild(tr);

    });

    const avgRS = totalRS / countRS;

    document.getElementById("summary-content").innerHTML = `

      <div class="summary-stat">
          <span>Rows:</span>
          <strong>${countRS}</strong>
      </div>
      
      <div class="summary-stat">
          <span>Best RS:</span>
          <strong>${bestStock} (${bestRS.toFixed(2)})</strong>
      </div>
      
      <div class="summary-stat">
          <span>Worst RS:</span>
          <strong>${worstStock} (${worstRS.toFixed(2)})</strong>
      </div>
      
      <div class="summary-stat">
          <span>Avg RS:</span>
          <strong>${avgRS.toFixed(2)}</strong>
      </div>
      
      `;
    
    const sortDropdown = 
    document.getElementById("sortRank");
    sortDropdown.addEventListener("change", () => {

    if(sortDropdown.value === "asc"){

        dataRows.sort((a,b) => {
            return Number(a.split(",")[10]) -
                   Number(b.split(",")[10]);
        });

    }else{

        dataRows.sort((a,b) => {
            return Number(b.split(",")[10]) -
                   Number(a.split(",")[10]);
        });

    }

    tbody.innerHTML = "";

    dataRows.forEach(row => {

        const cols = row.split(",");

        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${cols[0]}</td>
            <td>${cols[1]}</td>
            <td>${cols[6]}</td>
            <td>${cols[7]}</td>
            <td>${cols[8]}</td>
            <td>${cols[9]}</td>
            <td>${cols[10]}</td>
        `;

        tbody.appendChild(tr);

    });

});
});