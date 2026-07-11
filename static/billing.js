window.onload = function () {
  fetch("http://127.0.0.1:5000/billing")
    .then(res => res.json())
    .then(data => {
      document.getElementById("total-kwh").innerText = data.total_kwh;
      document.getElementById("total-cost").innerText = data.total_cost;
    });

  fetch("http://127.0.0.1:5000/history")
    .then(res => res.json())
    .then(data => {
      const ctx = document.getElementById("billingChart").getContext("2d");
      new Chart(ctx, {
        type: "line",
        data: {
          labels: data.dates,
          datasets: [{
            label: "Energy Usage (kWh)",
            data: data.usages,
            fill: true,
            borderColor: "cyan",
            backgroundColor: "rgba(0,255,255,0.1)"
          }]
        },
        options: {
          responsive: true,
          scales: {
            y: { beginAtZero: true }
          }
        }
      });
    });
};

