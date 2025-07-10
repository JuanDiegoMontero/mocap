import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ActiveCategoriesChart from "../components/ActiveCategoriesChart";
import TopOfferBrandsChart from '../components/TopOfferBrandsChart';
import SearchTrendsChart from '../components/SearchTrendsChart';
import TopProductsChart from '../components/TopProductsChart';


const DashboardBootstrap = () => {
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');

  // Cargar categorías al iniciar
  useEffect(() => {
    axios.get('http://localhost:8000/categories/')
      .then(response => {
        setCategories(response.data);
      })
      .catch(error => {
        console.error('Error al cargar categorías:', error);
      });
  }, []);

  return (
    <div className="container py-4">
      {/* Filtros */}
      <div className="row mb-4 g-3">
        

        <div className="col-md-3">
          <select
            className="form-select"
            value={selectedCategory}
            onChange={e => setSelectedCategory(e.target.value)}
          >
            <option value="">Todas las Categorías</option>
            {categories.map((category, index) => (
              <option key={index} value={category}>
                {category}
              </option>
            ))}
          </select>
        </div>

        
      </div>

    

      <div className="row g-4">
        
        {/* Card 1 - Productos más comprados */}
        <div className="col-md-6">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <TopProductsChart selectedCategory={selectedCategory} />
            </div>
          </div>
        </div>


        {/* Card 2 - Gráfica dinámica según categoría */}
        <div className="col-md-6">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <SearchTrendsChart selectedCategory={selectedCategory} />
            </div>
          </div>
        </div>

        {/* Card 3 - Marcas más activas en ofertas */}
        <div className="col-md-6">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <TopOfferBrandsChart />
            </div>
          </div>
        </div>

        {/* Card 4 - Categorías con más publicaciones activas */}
        <div className="col-md-6">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <ActiveCategoriesChart />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardBootstrap;
