"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
//   export interface HourlyUnits {
//     time: string
//     temperature_2m: string
//   }
//   export interface Hourly {
//     time: string[]
//     temperature_2m: number[]
//   }
const app = (0, express_1.default)();
const port = 3001;
const callApi = async (lat, lon, from, to, type) => {
    try {
        const response = await fetch(`https://api.open-meteo.com/v1/gfs?end_date=${to}&hourly=${type}&latitude=${lat}&longitude=${lon}&start_date=${from}`);
        const data = await response.json();
        //console.log(data)
        let hourly = [];
        for (let i = 0; i < data.hourly.time.length; i++) {
            hourly.push({ time: data.hourly.time[i], value: data.hourly[type][i] });
        }
        //console.log(hourly);
        return hourly;
    }
    catch {
        console.error("Error in fetching data");
        return [];
    }
};
app.get("/", async (req, res) => {
    console.log(req.query.lat);
    console.log(req.query.lon);
    console.log(req.query.from);
    console.log(req.query.to);
    console.log(req.query.type);
    const lat = req.query.lat;
    const lon = req.query.lon;
    const from = req.query.from;
    const to = req.query.to;
    const type = req.query.type;
    console.log(lat);
    // temperature_2m,relative_humidity_2m,rain,cloud_cover,wind_speed_10m
    switch (type) {
        case "temperature":
            const temp_response = await callApi(lat, lon, from, to, "temperature_2m");
            res.send(temp_response);
            break;
        case "humidity":
            const humidity_response = await callApi(lat, lon, from, to, "relative_humidity_2m");
            res.send(humidity_response);
            break;
        case "rain":
            const rain_response = await callApi(lat, lon, from, to, "rain");
            res.send(rain_response);
            break;
        case "cloud":
            const cloud_response = await callApi(lat, lon, from, to, "cloud_cover");
            res.send(cloud_response);
            break;
        case "wind":
            const wind_response = await callApi(lat, lon, from, to, "wind_speed_10m");
            res.send(wind_response);
            break;
        default:
            res.send("Invalid type");
            break;
    }
});
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
