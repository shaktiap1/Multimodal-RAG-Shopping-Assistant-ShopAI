import React, { useState } from "react";
import { uploadFile, getCaption } from "../api";

function ImageUpload() {
  const [caption, setCaption] = useState("");

  const handleChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const { data } = await uploadFile(file);
    const res = await getCaption(data.filename);
    setCaption(res.data.caption);
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <input type="file" accept="image/*" onChange={handleChange} />
      {caption && <p className="mt-2 text-green-600">Caption: {caption}</p>}
    </div>
  );
}

export default ImageUpload;
