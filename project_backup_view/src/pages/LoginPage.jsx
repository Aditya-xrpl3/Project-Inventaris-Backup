import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";
import useAuthStore from "../store/authStore";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const login = useAuthStore((state) => state.login);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const tokenResponse = await api.post("/token/", {
        username: username,
        password: password,
      });

      const tokens = tokenResponse.data;

      // PENTING: Simpan token ke store DULU sebelum request user data
      // Agar interceptor bisa menambahkan header Authorization
      login(tokens, null); // null karena belum ada user data

      const userResponse = await api.get("/user/me/");
      const userData = userResponse.data;

      // Update dengan data user yang lengkap
      login(tokens, userData);

      const isAdmin = userData.groups.some(
        (group) => group.name === "Admin Inventaris"
      );

      if (isAdmin) {
        navigate("/admin");
      } else {
        navigate("/scan");
      }
    } catch (err) {
      setError("Username atau password salah.");
      console.error("Login error:", err);
    }
  };

  return (
    <div>
      <h1>Halaman Login</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
      {/* Tampilkan pesan error jika ada */}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}
