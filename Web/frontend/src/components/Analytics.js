// Import necessary modules
import React, { useEffect, useState } from 'react';
import { Bar, Pie } from 'react-chartjs-2';
import axios from 'axios';
import { Chart, CategoryScale, LinearScale, BarElement, ArcElement, Title, Tooltip, Legend } from 'chart.js';
import './css/Analytics.css'; // Import the new CSS file for styling

Chart.register(CategoryScale, LinearScale, BarElement, ArcElement, Title, Tooltip, Legend);

const Analytics = () => {
    const [sourceIpCounts, setSourceIpCounts] = useState({});
    const [destinationIpCounts, setDestinationIpCounts] = useState({});
    const [protocolCounts, setProtocolCounts] = useState({});

    useEffect(() => {
        // Fetch logs data
        axios.get('http://127.0.0.1:5000/api/logs')
            .then(response => {
                const logs = response.data;
                parseLogData(logs);
            })
            .catch(error => console.error("Error fetching logs: ", error));
    }, []);

    const parseLogData = (logs) => {
        const sourceIpCounts = {};
        const destinationIpCounts = {};
        const protocolCounts = {};

        logs.forEach(log => {
            const match = log.message.match(/source_ip':\s'([\d.]+)'[^]*destination_ip':\s'([\d.]+)'[^]*protocol':\s'(\w+)'/);
            if (match) {
                const sourceIp = match[1];
                const destinationIp = match[2];
                const protocol = match[3];

                sourceIpCounts[sourceIp] = (sourceIpCounts[sourceIp] || 0) + 1;
                destinationIpCounts[destinationIp] = (destinationIpCounts[destinationIp] || 0) + 1;
                protocolCounts[protocol] = (protocolCounts[protocol] || 0) + 1;
            }
        });

        setSourceIpCounts(sourceIpCounts);
        setDestinationIpCounts(destinationIpCounts);
        setProtocolCounts(protocolCounts);
    };

    // Generate a random color
    const generateRandomColor = () => {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    };

    // Generate an array of random colors
    const generateColors = (count) => Array.from({ length: count }, generateRandomColor);

    // Prepare data for charts
    const ipChartData = {
        labels: Object.keys(sourceIpCounts),
        datasets: [
            {
                label: 'Source IP Counts',
                data: Object.values(sourceIpCounts),
                backgroundColor: generateColors(Object.keys(sourceIpCounts).length) // Random colors
            }
        ]
    };

    const destinationIpChartData = {
        labels: Object.keys(destinationIpCounts),
        datasets: [
            {
                label: 'Destination IP Counts',
                data: Object.values(destinationIpCounts),
                backgroundColor: generateColors(Object.keys(destinationIpCounts).length) // Random colors
            }
        ]
    };

    const protocolChartData = {
        labels: Object.keys(protocolCounts),
        datasets: [
            {
                label: 'Protocol Counts',
                data: Object.values(protocolCounts),
                backgroundColor: generateColors(Object.keys(protocolCounts).length) // Random colors
            }
        ]
    };

    return (
        <div className="analytics-container">
            <h2>Log Analytics</h2>
            <div className="chart-container">
                <h3>Source IP Distribution</h3>
                <Bar data={ipChartData} />
            </div>
            <div className="chart-container">
                <h3>Destination IP Distribution</h3>
                <Bar data={destinationIpChartData} />
            </div>
            <div className="chart-container">
                <h3>Protocol Distribution</h3>
                <Pie data={protocolChartData} />
            </div>
        </div>
    );
};

export default Analytics;
