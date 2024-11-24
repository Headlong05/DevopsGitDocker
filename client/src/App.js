import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [results, setResults] = useState([]);

    // Функция для выполнения запроса и получения данных
    const fetchData = async () => {
        try {
            const response = await axios.get('http://localhost:8000/search?query='); // Укажите нужный запрос, если требуется
            setResults(response.data);
            console.log(response.data);
        } catch (error) {
            if (error.response) {
                console.error("Server error:", error.response.status, error.response.data);
            } else if (error.request) {
                console.error("No response from server. Please check your connection.");
            } else {
                console.error("Error setting up request:", error.message);
            }
            setResults([]);
        }
    };

    // Использование useEffect для получения данных при монтировании компонента
    useEffect(() => {
        fetchData();
    }, []);

    return (
        <div className="App">
            <h1>Поиск по списку</h1>
            <ul className="results-list">
                {results.map((item, index) => (
                    <li key={index} className="result-item">Имя: {item.name} | Возраст: {item.age} | Направление: {item.major}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
