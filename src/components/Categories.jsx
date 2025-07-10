import React, { useState, useEffect } from 'react';

export default function Categories() {
  // 1) Iniciar siempre como array vacío
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch('/categories/')  // tu endpoint para obtener categorías
      .then(res => {
        if (!res.ok) throw new Error(res.statusText);
        return res.json();
      })
      .then(json => {
        setCategories(json); // tu endpoint devuelve ya un array de strings
        setError(null);
      })
      .catch(err => {
        console.error(err);
        setError(err);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Cargando…</p>;
  if (error)   return <p>Error: {error.message}</p>;

  // 3) Protección extra
  if (!Array.isArray(categories)) {
    return <p>Formato de datos inesperado</p>;
  }

  return (
    <div>
      <h2>Categorías</h2>
      <ul>
        {categories.map((cat, idx) => (
          <li key={idx}>{cat}</li>
        ))}
      </ul>
    </div>
  );
}
