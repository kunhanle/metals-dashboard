import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import { Activity, LayoutDashboard, LineChart } from 'lucide-react';
import MetalsDashboard from './pages/MetalsDashboard';
import CorrelationAnalysis from './pages/CorrelationAnalysis';

const NavBar = () => {
  const location = useLocation();

  const linkClass = (path) => `flex items-center gap-2 px-4 py-2 rounded-lg transition-colors ${location.pathname === path
      ? 'bg-emerald-600 text-white shadow-lg'
      : 'text-gray-400 hover:text-white hover:bg-gray-800'
    }`;

  return (
    <nav className="bg-gray-800 border-b border-gray-700 sticky top-0 z-50">
      <div className="max-w-[95%] mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center gap-3">
            <Activity className="w-8 h-8 text-emerald-400" />
            <span className="text-xl font-bold text-gray-100">Market<span className="text-emerald-400">Sight</span></span>
          </div>

          <div className="flex gap-4">
            <Link to="/" className={linkClass('/')}>
              <LayoutDashboard className="w-4 h-4" />
              Dashboard
            </Link>
            <Link to="/correlation" className={linkClass('/correlation')}>
              <LineChart className="w-4 h-4" />
              Correlation Analysis
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-900 text-white font-sans">
        <NavBar />
        <Routes>
          <Route path="/" element={<MetalsDashboard />} />
          <Route path="/correlation" element={<CorrelationAnalysis />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
