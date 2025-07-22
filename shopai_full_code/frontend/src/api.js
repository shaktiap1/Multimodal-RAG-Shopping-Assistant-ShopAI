import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000/api",
});

export const uploadFile = (file) => {
  const form = new FormData();
  form.append("file", file);
  return API.post("/upload", form);
};

export const getCaption = (image_path) => API.post("/caption", { image_path });

export const transcribeAudio = (audioFile) => {
  const form = new FormData();
  form.append("audio", audioFile);
  return API.post("/transcribe", form);
};

export const askRAG = (question) => API.post("/query", { question });

export const getRecommendations = (query) => API.post("/recommend", { query });
