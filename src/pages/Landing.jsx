import React, { useState, useEffect } from 'react';


export default function Landing() {
  const [categories, setCategories] = useState([]);      // para guardar el array
  const [loading, setLoading] = useState(true);    // para controlar carga
  const [error, setError] = useState(null);    // para posibles errores
  const [selectedCategory, setSelectedCategory] = useState(''); // si quieres manejar selección

  useEffect(() => {
    if (selectedCategory) {
      // hacer algo cuando cambie la categoría
      console.log('Usuario eligió:', selectedCategory);
    }
  }, [selectedCategory]);


  return (
    <div className="container py-4">
      {/* Filtros */}
      <div className="row mb-4 g-3">
        <div className="col-md-3">
          <select className="form-select">
            <option>Temporada</option>
          </select>
        </div>
        <div className="col-md-3">
          {loading ? (
            <p>Cargando categorías…</p>
          ) : error ? (
            <p>Error al cargar categorías</p>
          ) : (
            <select
              className="form-select"
              value={selectedCategory}
              onChange={e => setSelectedCategory(e.target.value)}
            >
              {/* Opción por defecto */}
              <option value="">Todas las Categorías</option>
              {/* Mapea cada categoría a un <option> */}
              {categories.map(cat => (
                <option key={cat} value={cat}>
                  {cat}
                </option>
              ))}
            </select>
          )}
        </div>
        <div className="col-md-3">
          <select className="form-select">
            <option>Todas las regiones</option>
          </select>
        </div>
        <div className="col-md-3">
          <select className="form-select">
            <option>Año</option>
          </select>
        </div>
      </div>

      {/* Gráficas */}
      <div className="row g-4">
        {/* Card 1 */}
        <div className="col-md-6">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Los 5 productos más comprados por Categoría</h5>
              <div className="text-muted text-center py-5">Aquí va la gráfica 1</div>
            </div>
          </div>
        </div>

        {/* Card 2 */}
        <div className="col-md-6">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Las 5 búsquedas más populares por categoría</h5>
              <div className="text-muted text-center py-5">Aquí va la gráfica 2</div>
            </div>
          </div>
        </div>

        {/* Card 3 */}
        <div className="col-md-6">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Las 5 marcas más activas en oferta</h5>
              <div className="text-muted text-center py-5">Aquí va la gráfica 3</div>
            </div>
          </div>
        </div>

        {/* Card 4 */}
        <div className="col-md-6">
          <div className="card h-100 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Las 5 categorías con más publicaciones activas</h5>
              <div className="text-muted text-center py-5">Aquí va la gráfica 4</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
