import * as d3 from "d3";
import { longestYard } from './longest_yard';
import { barChart } from './barchart';

import Chart from './chart';
document.addEventListener("DOMContentLoaded", () => {
  const sample = [
    {
      language: 'Rust',
      value: 78.9,
      color: '#000000'
    },
    {
      language: 'Kotlin',
      value: 75.1,
      color: '#00a2ee'
    },
    {
      language: 'Python',
      value: 68.0,
      color: '#fbcb39'
    },
    {
      language: 'TypeScript',
      value: 67.0,
      color: '#007bc8'
    },
    {
      language: 'Go',
      value: 65.6,
      color: '#65cedb'
    }
  ];

  let chart1 = new Chart(sample);
  chart1.run();
  longestYard();
});
