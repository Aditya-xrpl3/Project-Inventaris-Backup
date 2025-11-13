import React from "react";
import ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import App from "./App.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import AdminDashboard from "./pages/AdminDashboard.jsx";
import LaporPage from "./pages/LaporPage.jsx";
import ScanPage from "./pages/ScanPage.jsx";
import NotFound from "./pages/NotFound.jsx";
import ProtectedRoute from "./components/ProtectedRoute.jsx";
import RootRedirect from "./components/RootRedirect.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <NotFound />,
    children: [
      {
        index: true,
        element: <RootRedirect />,
      },
      {
        path: "/login",
        element: <LoginPage />,
      },
      {
        path: "/scan",
        element: <ScanPage />,
      },
      {
        path: "/lapor/:barangId",
        element: <LaporPage />,
      },
      {
        element: <ProtectedRoute />,
        children: [
          {
            path: "/admin",
            element: <AdminDashboard />,
          },
        ],
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
