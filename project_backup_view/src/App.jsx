import React from 'react';
import { Outlet } from 'react-router-dom';

function App() {
  return (
    <div>
      <header>
        <h1>Aplikasi Inventaris</h1>
        <hr />
      </header>

      <main>
        <Outlet />
      </main>

      <footer>
        {/* Footer */}
      </footer>
    </div>
  )
}

export default App;