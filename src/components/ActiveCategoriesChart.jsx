import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

// Registrar módulos de Chart.js
ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const ActiveCategoriesChart = () => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/active-listenings/?limit=1000')
      .then(response => {
        const data = response.data.active_listenings;

        // Ordenar por publicaciones activas y tomar top 5
        const top5 = data
          .sort((a, b) => b.active_listings - a.active_listings)
          .slice(0, 5);

        // Preparar datos para Chart.js
        const labels = top5.map(item => item.category_name);
        const values = top5.map(item => item.active_listings);

        setChartData({
          labels,
          datasets: [
            {
              label: 'Publicaciones activas',
              data: values,
              backgroundColor: 'rgba(54, 162, 235, 0.6)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1,
              borderRadius: 4
            }
          ]
        });
      })
      .catch(error => {
        console.error('Error al obtener publicaciones activas:', error);
      });
  }, []);

  const options = {
    responsive: true,
    plugins: {
      legend: { display: false }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: { stepSize: 1000000 }
      }
    }
  };

  return (
    <div>
      <h5 className="card-title mb-4">Las 5 categorías con publicaciones más activas</h5>
      {chartData ? (
        <Bar data={chartData} options={options} />
      ) : (
        <p className="text-center text-muted">Cargando gráfica...</p>
      )}
    </div>
  );
};

export default ActiveCategoriesChart;
