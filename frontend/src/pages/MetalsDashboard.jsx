import { useState, useEffect } from 'react';
import axios from 'axios';
import CandlestickChart from '../components/CandlestickChart';
import { Activity } from 'lucide-react';

const MetalsDashboard = () => {
    const [metalsData, setMetalsData] = useState({});
    const [loading, setLoading] = useState(true);

    const metals = [
        'Gold', 'Silver', 'Copper', 'Nickel', 'Zinc', 'Lead', 'Tin', 'Aluminium'
    ];

    const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

    useEffect(() => {
        const fetchMetals = async () => {
            try {
                const response = await axios.get(`${API_BASE_URL}/api/metals`);
                setMetalsData(response.data);
            } catch (error) {
                console.error("Failed to fetch metals data", error);
            } finally {
                setLoading(false);
            }
        };

        fetchMetals();
    }, []);

    // Helper to filter data for the last 3 months
    const get3MonthData = (data) => {
        if (!data || data.length === 0) return [];
        // Approximate 3 months as roughly 63 trading days, or date logic
        // Let's use date logic
        const threeMonthsAgo = new Date();
        threeMonthsAgo.setMonth(threeMonthsAgo.getMonth() - 3);

        return data.filter(item => new Date(item.x) >= threeMonthsAgo);
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-[calc(100vh-100px)] text-emerald-400">
                <Activity className="w-10 h-10 animate-spin" />
            </div>
        );
    }

    return (
        <div className="w-full max-w-[95%] mx-auto py-8">
            <header className="mb-8 flex flex-col items-center">
                <h1 className="text-4xl font-bold bg-gradient-to-r from-yellow-400 to-orange-500 bg-clip-text text-transparent flex items-center gap-3">
                    Global Metals Dashboard
                </h1>
                <p className="text-gray-400 mt-2">Real-time market insights</p>
            </header>

            <div className="space-y-8">
                <section>
                    <h2 className="text-2xl font-bold mb-4 text-gray-200 border-b border-gray-700 pb-2">Base Metals</h2>
                    <div className="space-y-8">
                        {metals.map(metal => (
                            <div key={metal} className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                                <CandlestickChart
                                    title={`${metal} - 3 Years`}
                                    data={metalsData[metal] || []}
                                />
                                <CandlestickChart
                                    title={`${metal} - 3 Months`}
                                    data={get3MonthData(metalsData[metal])}
                                />
                            </div>
                        ))}
                    </div>
                </section>

                <section>
                    <h2 className="text-2xl font-bold mb-4 text-gray-200 border-b border-gray-700 pb-2">Steel & Iron Indices</h2>
                    <div className="space-y-8">
                        {['CRU Index', 'DJUSST', 'HRC Futures', 'SGX Iron Ore'].map(item => (
                            <div key={item} className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                                <CandlestickChart
                                    title={`${item} - 3 Years`}
                                    data={metalsData[item] || []}
                                />
                                <CandlestickChart
                                    title={`${item} - 3 Months`}
                                    data={get3MonthData(metalsData[item])}
                                />
                            </div>
                        ))}
                    </div>
                </section>
            </div>
        </div>
    );
};

export default MetalsDashboard;
