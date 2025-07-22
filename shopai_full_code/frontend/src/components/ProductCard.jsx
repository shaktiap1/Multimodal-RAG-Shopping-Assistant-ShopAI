import React from "react";

function ProductCard({ product }) {
  return (
    <div className="p-4 border rounded-lg">
      <h3 className="font-semibold">{product.name}</h3>
      <p>${product.price}</p>
      <a href={product.link} target="_blank" rel="noopener noreferrer" className="text-blue-600 underline">
        View
      </a>
    </div>
  );
}

export default ProductCard;
