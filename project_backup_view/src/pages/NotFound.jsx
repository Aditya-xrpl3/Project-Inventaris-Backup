import { useNavigate } from "react-router-dom";

export default function NotFound() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h1>404 - Halaman Tidak Ditemukan</h1>
      <p>Halaman yang Anda cari tidak ada.</p>
      <button onClick={() => navigate("/login")}>Kembali ke Login</button>
    </div>
  );
}
