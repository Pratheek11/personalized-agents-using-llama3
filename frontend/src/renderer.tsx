import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import 'primereact/resources/themes/lara-light-blue/theme.css'; // or any other theme
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';

const container = document.getElementById('root');

const root = createRoot(container!); // createRoot(container!) if using TypeScript

root.render(
    <BrowserRouter>
        <App/>
    </BrowserRouter>
);