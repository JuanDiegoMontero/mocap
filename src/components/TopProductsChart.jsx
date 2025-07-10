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

// Registrar componentes de ChartJS
ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const TopProductsChart = ({ selectedCategory }) => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    if (!selectedCategory) {
      setChartData(null);
      return;
    }

    axios.get('http://localhost:8000/products-by-category/')
      .then(response => {
        const allProducts = response.data;

        // Filtrar por la categoría seleccionada
        const filtered = allProducts.filter(
          item => item.category_name === selectedCategory
        );

        // Tomar solo los primeros 5 productos
        const top5 = filtered.slice(0, 5);

        // Asignar valores ficticios de cantidad comprada
        const fakeValues = top5.map(() => Math.floor(Math.random() * (10000 - 3000) + 3000));

        // Eje X: títulos de productos
        const labels = top5.map(item => item.product_title);

        setChartData({
          labels,
          datasets: [
            {
              label: 'Compras',
              data: fakeValues,
              backgroundColor: 'rgba(255, 99, 132, 0.6)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1,
              borderRadius: 4
            }
          ]
        });
      })
      .catch(error => {
        console.error('Error al obtener productos por categoría:', error);
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
        Los 5 productos más comprados por categoría
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

export default TopProductsChart;
