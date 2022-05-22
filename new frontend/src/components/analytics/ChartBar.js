import { useEffect } from 'react';
import Chart from 'chart.js/auto';
import Card from '@material-tailwind/react/Card';
import CardHeader from '@material-tailwind/react/CardHeader';
import CardBody from '@material-tailwind/react/CardBody';


export default function ChartBar({
    h,o,c
}) {
    useEffect(() =>{
        let config = {
            type: 'bar',
            data: {
                labels: [
                    'hate',
                    'offensive',
                    'clean'
                ],
                datasets: [
                    {
                        label: 'No. of tweets',
                        data: [h,o,c],
                        backgroundColor:['rgb(255, 99, 132)','rgb(255, 205, 86)','rgb(54, 162, 235)'],
                        fill:false,
                        borderWidth: 8
                    }
                ],
            },
        };
        let ctx = document.getElementById('bar-chart').getContext('2d');
        window.myBar = new Chart(ctx, config);
    }, []);
    return (
        <Card>
            <CardHeader color="blue" contentPosition="left">
                <h2 className="text-white text-2xl">HOC Values</h2>
            </CardHeader>
            <CardBody>
                <div className="relative h-30">
                    <canvas id="bar-chart"></canvas>
                </div>
            </CardBody>
        </Card>
    );
}
