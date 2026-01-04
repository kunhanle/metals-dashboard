import Chart from 'react-apexcharts';

const CandlestickChart = ({ data, title, height = 350 }) => {
    if (!data || data.length === 0) {
        return (
            <div className="w-full h-[350px] bg-gray-800 flex items-center justify-center text-gray-400 rounded-lg border border-gray-700">
                No Data for {title}
            </div>
        );
    }

    const series = [{
        data: data
    }];

    const options = {
        chart: {
            type: 'candlestick',
            height: height,
            toolbar: {
                show: false
            },
            background: 'transparent'
        },
        title: {
            text: title,
            align: 'left',
            style: {
                color: '#e5e7eb',
                fontSize: '16px'
            }
        },
        xaxis: {
            type: 'datetime',
            labels: {
                style: {
                    colors: '#9ca3af'
                }
            },
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: false
            }
        },
        yaxis: {
            tooltip: {
                enabled: true
            },
            labels: {
                style: {
                    colors: '#9ca3af'
                },
                formatter: (value) => {
                    return value.toFixed(2);
                }
            }
        },
        grid: {
            borderColor: '#374151',
            strokeDashArray: 3
        },
        theme: {
            mode: 'dark'
        },
        plotOptions: {
            candlestick: {
                colors: {
                    upward: '#34d399',
                    downward: '#f87171'
                }
            }
        }
    };

    return (
        <div className="bg-gray-800 p-4 rounded-lg shadow-lg border border-gray-700">
            <Chart options={options} series={series} type="candlestick" height={height} />
        </div>
    );
};

export default CandlestickChart;
