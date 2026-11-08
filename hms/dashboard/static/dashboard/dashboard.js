document.addEventListener('DOMContentLoaded', function () {
  const root = document.body;
  const toggle = document.getElementById('themeToggle');
  const search = document.getElementById('dashboardSearch');
  const table = document.getElementById('appointmentTable');

  const applyTheme = (isDark) => {
    root.classList.toggle('dark-mode', isDark);
    if (toggle) {
      toggle.textContent = isDark ? 'Light mode' : 'Dark mode';
    }
    localStorage.setItem('care-sync-theme', isDark ? 'dark' : 'light');
  };

  const savedTheme = localStorage.getItem('care-sync-theme');
  if (savedTheme === 'dark') {
    applyTheme(true);
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      applyTheme(!root.classList.contains('dark-mode'));
    });
  }

  if (search && table) {
    const rows = Array.from(table.querySelectorAll('tbody tr'));

    search.addEventListener('input', function () {
      const q = search.value.trim().toLowerCase();

      rows.forEach((row) => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(q) ? '' : 'none';
      });
    });
  }

  const chartCanvas = document.getElementById('analyticsChart');
  if (chartCanvas && window.Chart) {
    const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'];
    const data = [18, 25, 30, 40, 35, 52, 58];

    new Chart(chartCanvas, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Consultations',
          data: data,
          borderColor: '#2d6df6',
          backgroundColor: 'rgba(45, 109, 246, 0.08)',
          borderWidth: 3,
          pointRadius: 4,
          pointBackgroundColor: '#2d6df6',
          tension: 0.35,
          fill: true,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            grid: { color: 'rgba(148,163,184,0.15)' },
            ticks: { color: '#6b7a90' }
          },
          x: {
            grid: { display: false },
            ticks: { color: '#6b7a90' }
          }
        },
        plugins: {
          legend: { display: false }
        }
      }
    });
  }
});
