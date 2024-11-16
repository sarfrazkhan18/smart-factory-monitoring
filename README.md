# Smart Factory Monitoring System

A real-time monitoring system for industrial equipment using Python, Dash, and machine learning for predictive maintenance.

## Features

- Real-time sensor data visualization
- Machine status monitoring
- Interactive dashboard
- System controls
- Simulated sensor data (temperature, vibration, pressure)

## Setup Instructions

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:8050
```

## Project Structure

- `app.py`: Main application file with dashboard implementation
- `requirements.txt`: Project dependencies
- `README.md`: Documentation

## Technologies Used

- Python 3.8+
- Dash (for web interface)
- Plotly (for data visualization)
- Pandas & NumPy (for data processing)
- Flask (backend server)
- Bootstrap (styling)

## Future Enhancements

1. Machine Learning Integration
   - Anomaly detection
   - Predictive maintenance
   - Pattern recognition

2. Additional Features
   - Historical data storage
   - Alert system
   - User authentication
   - Custom sensor configuration

3. Hardware Integration
   - Real sensor data integration
   - IoT device support
   - Multiple machine monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
