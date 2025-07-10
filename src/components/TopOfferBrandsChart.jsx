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

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const TopOfferBrandsChart = () => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/ofertas-mercado-libre/?limit=1000')
      .then(response => {
        const offers = response.data;

        // Agrupar por marca y contar ocurrencias
        const brandCounts = {};
        offers.forEach(offer => {
          const brand = offer.Marca?.trim() || 'Sin marca';
          brandCounts[brand] = (brandCounts[brand] || 0) + 1;
        });

        // Convertir en array, ordenar y tomar top 5
        const top5 = Object.entries(brandCounts)
          .sort((a, b) => b[1] - a[1])
          .slice(0, 5);

        const labels = top5.map(([brand]) => brand);
        const values = top5.map(([, count]) => count);

        setChartData({
          labels,
          datasets: [
            {
              label: 'Cantidad de Ofertas',
              data: values,
              backgroundColor: 'rgba(255, 99, 132, 0.6)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              borderRadius: 4,
            }
          ]
        });
      })
      .catch(error => {
        console.error('Error al obtener las ofertas:', error);
      });
  }, []);

  const options = {
    responsive: true,
    plugins: {
      legend: { display: false }
    },
    scales: {
      y: {
        beginAtZero: true
      }
    }
  };

  return (
    <div>
      <h5 className="card-title mb-4">Las 5 marcas más activas en ofertas</h5>
      {chartData ? (
        <Bar data={chartData} options={options} />
      ) : (
        <p className="text-center text-muted">Cargando gráfica...</p>
      )}
    </div>
  );
};

export default TopOfferBrandsChart;
