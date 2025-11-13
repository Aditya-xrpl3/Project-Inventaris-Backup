import { Navigate } from "react-router-dom";
import useAuthStore from "../store/authStore";

export default function RootRedirect() {
  const { user } = useAuthStore();

  // Jika user sudah login dan admin, arahkan ke admin dashboard
  if (user && (user.is_staff || user.role === "admin")) {
    return <Navigate to="/admin" replace />;
  }

  // User biasa atau belum login, arahkan ke scan (tidak perlu login)
  return <Navigate to="/scan" replace />;
}
