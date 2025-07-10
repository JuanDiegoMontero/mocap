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

// Registrar módulos
ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const SearchTrendsChart = ({ selectedCategory }) => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    if (!selectedCategory) return;

    axios.get('http://localhost:8000/search-trends-by-category/')
      .then(response => {
        const allTrends = response.data;

        // Filtrar por categoría seleccionada
        const filtered = allTrends.filter(item => item.category_name === selectedCategory);

        // Tomar las primeras 5 keywords
        const top5 = filtered.slice(0, 5);

        // Crear datos ficticios únicos por categoría (puedes ajustarlos más si quieres)
        const fakeValues = top5.map((_, i) => Math.floor(Math.random() * (5000 - 1000) + 1000));

        const labels = top5.map(item => item.keyword);
        const values = fakeValues;

        setChartData({
          labels,
          datasets: [
            {
              label: 'Popularidad',
              data: values,
              backgroundColor: 'rgba(255, 206, 86, 0.6)',
              borderColor: 'rgba(255, 206, 86, 1)',
              borderWidth: 1,
              borderRadius: 4
            }
          ]
        });
      })
      .catch(error => {
        console.error('Error al obtener tendencias de búsqueda:', error);
      });
  }, [selectedCategory]);

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
      <h5 className="card-title mb-4">
        Las 5 búsquedas más populares por categoría
      </h5>
      {selectedCategory ? (
        chartData ? (
          <Bar data={chartData} options={options} />
        ) : (
          <p className="text-center text-muted">Cargando gráfica...</p>
        )
      ) : (
        <p className="text-center text-muted">Selecciona una categoría para ver la gráfica</p>
      )}
    </div>
  );
};

export default SearchTrendsChart;
